import pytimbr_api as timbr

# For http connections
response = timbr.executeQuery(hostname='<TIMBR_IP/HOST>', port='<TIMBR_PORT>', ontology='<ONTOLOGY_NAME>', token='<USER_TOKEN>', query='<TIMBR_QUERY>', nested='<true/false>')

# For https connections
response = timbr.securedExecuteQuery(hostname='<TIMBR_IP/HOST>', port='<TIMBR_PORT>', ontology='<ONTOLOGY_NAME>', token='<USER_TOKEN>', query='<TIMBR_QUERY>', nested='<true/false>')

# hostname - The IP / Hostname of the Timbr platform.
# port - Timbr default port 443
# ontology - the ontology / knowledge graph to connect to.
# token - Timbr token value.
# query - The query that you want to execute.
# nested - Change to true if nested flag needs to be enabled.

print(response)