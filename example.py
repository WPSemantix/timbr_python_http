import pytimbr_api as timbr

response = timbr.executeQuery(hostname='<TIMBR_IP/HOST>', port='<TIMBR_PORT>', ontology='<ONTOLOGY_NAME>', token='<USER_TOKEN>', query='<TIMBR_QUERY>', enabled_ssl=<True/False>, verify_ssl=<True/False>, nested='<true/false>')

# hostname - string - The IP / Hostname of the Timbr platform.
# port - string - Timbr default port 443.
# ontology - string - The ontology / knowledge graph to connect to.
# token - string - Timbr token value.
# query - string - The query that you want to execute.
# enabled_ssl - boolean - Use True for https connection and False for http connection.
# verify_ssl - boolean - Verifying the target server's SSL Certificate, use False to disable this process.
# nested - string - Change to 'true' if nested flag needs to be enabled. make sure this flag contains string value not bool value.

print(response)
