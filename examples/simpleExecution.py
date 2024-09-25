# use for pip installation
import pytimbr_api as timbr

# use for repository installation
import pytimbr_api.timbr_http_connector as timbr

# General example for query execution
response = timbr.simpleQueryExecution(
  url = "<TIMBR_URL>",
  ontology = "<ONTOLOGY_NAME>",
  token = "<USER_TOKEN>",
  query = "<TIMBR_QUERY>",
  datasource = "<DATASOURCE_NAME>",
  nested = "<true/false>",
)

# url - Required - String - The IP / Hostname of the Timbr platform.
# ontology - Required - String - The ontology / knowledge graph to connect to.
# token - Required - String - Timbr token value.
# query - Required - String - The query that you want to execute.
# datasource - Optional - String - Add the specific datasource name that you want to query from, the default value is the current active datasource of your ontology.
# nested - Optional - String - Change to 'true' if nested flag needs to be enabled. make sure this flag contains string value not bool value.

# HTTP example
response = timbr.simpleQueryExecution(
  url = "http://mytimbrenv.com:443",
  ontology = "my_ontology",
  token = "tk_mytimbrtoken",
  query = "SELECT * FROM timbr.sys_concepts",
)

# HTTPS example
response = timbr.simpleQueryExecution(
  url = "https://mytimbrenv.com:443",
  ontology = "my_ontology",
  token = "tk_mytimbrtoken",
  query = "SELECT * FROM timbr.sys_concepts",
)

print(response)
