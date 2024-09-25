# use for pip installation
import pytimbr_api as timbr

# use for repository installation
import pytimbr_api.timbr_http_connector as timbr

# General example for query execution
response = timbr.advancedQueryExecute(
  hostname = "<TIMBR_IP/HOST>",
  port = "<TIMBR_PORT>",
  ontology = "<ONTOLOGY_NAME>",
  token = "<USER_TOKEN>",
  query = "<TIMBR_QUERY>",
  enabled_ssl = <True/False>,
  verify_ssl = <True/False>,
  nested = "<true/false>",
  enableIPv6 = <True/False>,
  datasource = "<DATASOURCE_NAME>",
)

# hostname - Required - String - The IP / Hostname of the Timbr platform.
# port - Required - String - Timbr's default port with enabled_ssl is 443 without SSL is 11000.
# ontology - Required - String - The ontology / knowledge graph to connect to.
# token - Required - String - Timbr token value.
# query - Required - String - The query that you want to execute.
# enabled_ssl - Optional - Boolean - Use True for HTTPS connection and False for HTTP connection.
# verify_ssl - Optional - Boolean - Verifying the target server's SSL Certificate, use False to disable this process.
# nested - Optional - String - Change to 'true' if nested flag needs to be enabled. make sure this flag contains string value not bool value.
# enableIPv6 - Optional - Boolean - Change to 'true' if you are using IPv6 connection.
# datasource - Optional - String - Add the specific datasource name that you want to query from, the default value is the current active datasource of your ontology.

# HTTP example
response = timbr.advancedQueryExecute(
  hostname = "mytimbrenv.com",
  port = "443",
  ontology = "my_ontology",
  token = "tk_mytimbrtoken",
  query = "SELECT * FROM timbr.sys_concepts",
  enabled_ssl = False,
  verify_ssl = False,
  nested = "false",
)

# HTTPS example
response = timbr.advancedQueryExecute(
  hostname = "mytimbrenv.com",
  port = "443",
  ontology = "my_ontology",
  token = "tk_mytimbrtoken",
  query = "SELECT * FROM timbr.sys_concepts",
  enabled_ssl = True,
  verify_ssl = True,
  nested = "false",
)

print(response)
