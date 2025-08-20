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


def _parse_response(response):
    if response.status_code != 200:
        raise Exception(f'Error: {response.text}')

    response_json = None
    try:
        response_json = response.json()
    except Exception as e:
        raise Exception(f'Could not parse response from timbr server: {e}')
    return response_json


def run_query(
    url: str,
    ontology: str,
    token: str,
    query: str,
    datasource: str = None,
    nested: str = 'false',
    verify_ssl: bool = True,
    enable_IPv6: bool = False,
    is_jwt: bool = False,
    jwt_tenant_id: str = None,
    additional_headers: dict = None,
):
    datasource_addition = ''
    if datasource:
      datasource_addition = f'?datasource={datasource}'
    
    base_url = url
    if not base_url.endswith('/'):
      base_url = base_url + '/'
    
    headers = {
      'Content-Type': 'application/text',
      'nested': nested,
      'Connection': 'close',
    }

    if is_jwt:
      headers['x-jwt-token'] = token
      if jwt_tenant_id:
        headers['x-jwt-tenant-id'] = jwt_tenant_id
    else:
      headers['x-api-key'] = token

    if additional_headers:
       for key, value in additional_headers.items():
           headers[key.replace('_', '-')] = value

    requests.packages.urllib3.util.connection.HAS_IPV6 = enable_IPv6
    response = requests.post(
      f'{base_url}timbr/openapi/ontology/{ontology}/query{datasource_addition}',
      headers = headers,
      data = query,
      verify = verify_ssl,
    )
    return _parse_response(response)


# Deprecated - Backward compatibility
def executeTimbrQuery(url, ontology, token, query, override_datasource, nested, verify, enableIPv6):
  datasource_addition = ''
  if override_datasource:
    datasource_addition = f'?datasource={override_datasource}'
  headers = {'Content-Type': 'application/text', 'x-api-key': token, 'nested': nested, 'Connection': 'close'}
  requests.packages.urllib3.util.connection.HAS_IPV6 = enableIPv6
  response = requests.post(f'{url}timbr/openapi/ontology/{ontology}/query{datasource_addition}', headers = headers, data = query, verify = verify)
  return _parse_response(response)

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
  baseUrl = "http"
  if enabled_ssl == True:
    baseUrl = baseUrl + "s"
  baseUrl = f"{baseUrl}://{hostname}:{port}/"
  return legacyExecuteTimbrQuery(baseUrl, ontology, token, query, nested, verify_ssl)

def legacyExecuteTimbrQuery(url, ontology, token, query, nested, verify):
  post_data = {'ontology_name': ontology, 'query': query}
  headers = {'Content-Type': 'application/json', 'x-api-key': token, 'nested': nested}
  response = requests.post(url + "timbr/api/query/", headers = headers, json = post_data, verify = verify)
  return _parse_response(response)