#
#             *###              .,              @%             
#       *%##  `#// %%%*  *@     ``              @%             
#        #*.    * .%%%`  @@@@*  @@   @@@@,@@@@  @&@@@@   .&@@@*
#            #%%#   ..   *@     @@  @`  @@` ,@  @%   #@  @@  
#      ,, .,%(##/./%%#,  *@     @@  @`  @@` ,@  @%   #@  @@   
#    ,%##%          ``   `/@@*  @@  @`  @@` ,@  (/@@@#/  @@   
#      ``                                                     
#  ``````````````````````````````````````````````````````````````
#  Copyright (C) 2018-2024 timbr.ai

import requests

def executeTimbrQuery(url, ontology, token, query, override_datasource, nested, verify, enableIPv6):
  datasource_addition = ''
  if override_datasource:
    datasource_addition = f'?datasource={override_datasource}'
  headers = {'Content-Type': 'application/text', 'x-api-key': token, 'nested': nested, 'Connection': 'close'}
  requests.packages.urllib3.util.connection.HAS_IPV6 = enableIPv6
  response = requests.post(f'{url}timbr/openapi/ontology/{ontology}/query{datasource_addition}', headers = headers, data = query, verify = verify)
  return response.json()

def advancedQueryExecute(hostname, port, ontology, token, query, enabled_ssl=True, verify_ssl=True, nested = 'false', enableIPv6 = False, datasource = None):
  baseUrl = "http"
  if enabled_ssl == True:
    baseUrl = baseUrl + "s"
  baseUrl = f"{baseUrl}://{hostname}:{port}/"
  return executeTimbrQuery(baseUrl, ontology, token, query, datasource, nested, verify_ssl, enableIPv6)

def simpleQueryExecution(url, ontology, token, query, datasource = None, nested = 'false'):
  base_url = url
  if not base_url.endswith('/'):
    base_url = f'{url}/'
  return executeTimbrQuery(base_url, ontology, token, query, datasource, nested, True, False)

# Backward compatibility 
def executeQuery(hostname, port, ontology, token, query, enabled_ssl=True, verify_ssl=True, nested = 'false'):
  return advancedQueryExecute(
    hostname = hostname,
    port = port,
    ontology = ontology,
    token = token,
    query = query,
    enabled_ssl = enabled_ssl,
    verify_ssl = verify_ssl,
    nested = nested
  )