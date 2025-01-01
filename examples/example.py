# use for pip installation
import pytimbr_api as timbr

# use for repository installation
import pytimbr_api.timbr_http_connector as timbr

# General example for query execution
response = timbr.run_query(
  hostname = "<TIMBR_HOSTNAME>",
  ontology = "<ONTOLOGY_NAME>",
  token = "<USER_TOKEN>",
  query = "<TIMBR_QUERY>",
  datasource = "<DATASOURCE_NAME>",
  port = <TIMBR_PORT_NUMBER>,
  nested = "<true/false>",
  verify_ssl = <True/False>,
  enable_IPv6 = <True/False>,
)

# hostname    - Required - String - The IP / Hostname of the Timbr platform.
# ontology    - Required - String - The ontology / knowledge graph to connect to.
# token       - Required - String - Timbr token value.
# query       - Required - String - The query that you want to execute.
# datasource  - Optional - String - Add the specific datasource name that you want to query from, the default value is the current active datasource of your ontology.
# port        - Optional - Number - Timbr's default port with verify_ssl is 443 without SSL is 80.
# nested      - Optional - String - Change to 'true' if nested flag needs to be enabled. make sure this flag contains string value not bool value.
# verify_ssl  - Optional - Boolean - Verifying the target server's SSL Certificate, use False to disable this process.
# enable_IPv6 - Optional - Boolean - Change to 'true' if you are using IPv6 connection.

# HTTP example
response = timbr.run_query(
  hostname = "mytimbrenv.com",
  ontology = "my_ontology",
  token = "tk_mytimbrtoken",
  query = "SELECT * FROM timbr.sys_concepts",
  datasource = "my_datasource",
  port = 80,
  nested = "false",
  verify_ssl = False,
  enable_IPv6 = False,
)

print(response)

# HTTPS example
response = timbr.simpleQueryExecution(
  hostname = "mytimbrenv.com",
  ontology = "my_ontology",
  token = "tk_mytimbrtoken",
  query = "SELECT * FROM timbr.sys_concepts",
  datasource = "my_datasource",
  port = 443
  nested = "false",
  verify_ssl = True,
  enable_IPv6 = False,
)

print(response)
