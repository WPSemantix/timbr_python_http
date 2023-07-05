#
#             *###              .,              @%             
#       *%##  `#// %%%*  *@     ``              @%             
#        #*.    * .%%%`  @@@@*  @@   @@@@,@@@@  @&@@@@   .&@@@*
#            #%%#   ..   *@     @@  @`  @@` ,@  @%   #@  @@  
#      ,, .,%(##/./%%#,  *@     @@  @`  @@` ,@  @%   #@  @@   
#    ,%##%          ``   `/@@*  @@  @`  @@` ,@  (/@@@#/  @@   
#      ``                                                     
#  ``````````````````````````````````````````````````````````````
#  Copyright (C) 2018-2023 timbr.ai
#
import requests

def executeTimbrQuery(url, ontology, query, token, nested, verify):
  post_data = {'ontology_name': ontology, 'query': query}
  headers = {'Content-Type': 'application/json', 'x-api-key': token, 'nested': nested}
  response = requests.post(url + "timbr/api/query/", headers = headers, json = post_data, verify = verify)
  return response.json()

def executeQuery(hostname, port, ontology, token, query, enabled_ssl=False, verify_ssl=True, nested = 'false'):
  baseUrl = "http"
  if enabled_ssl == True:
    baseUrl = baseUrl + "s"
  baseUrl = f"{baseUrl}://{hostname}:{port}/"
  print(baseUrl)
  return executeTimbrQuery(baseUrl, ontology, query, token, nested, verify_ssl)