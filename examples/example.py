# use for pip installation
import pytimbr_api as timbr

# use for repository installation
import pytimbr_api.timbr_http_connector as timbr

# General example for query execution
response = timbr.run_query(
  url = "<TIMBR_URL>",
  ontology = "<ONTOLOGY_NAME>",
  token = "<USER_TOKEN>",
  query = "<TIMBR_QUERY>",
  datasource = "<DATASOURCE_NAME>",
  nested = "<true/false>",
  verify_ssl = <True/False>,
  enable_IPv6 = <True/False>,
  is_jwt = <True/False>,
  jwt_tenant_id = "<JWT_TENANT_ID>",
  additional_headers = <{ "x-api-impersonate-user": "<user to impersonate>" }>,
)

  # url                 - Required - String - The IP / Hostname of the Timbr platform.
  # ontology            - Required - String - The ontology / knowledge graph to connect to.
  # token               - Required - String - Timbr token value or JWT token value. Note: If you are using JWT token, you need to set the is_jwt parameter to True.
  # query               - Required - String - The query that you want to execute.
  # datasource          - Optional - String - Add the specific datasource name that you want to query from, the default value is the current active datasource of your ontology.
  # nested              - Optional - String - Change to 'true' if nested flag needs to be enabled. make sure this flag contains string value not bool value.
  # verify_ssl          - Optional - Boolean - Verifying the target server's SSL Certificate, use False to disable this process.
  # enable_IPv6         - Optional - Boolean - Change to 'true' if you are using IPv6 connection.
  # is_jwt              - Optional - Boolean - Set to True if you are using JWT token, otherwise set to False.
  # jwt_tenant_id       - Optional - String - The tenant ID for JWT authentication
  # additional_headers  - Optional - Dict - Extra Timbr connection parameters sent with every request (e.g., 'x-api-impersonate-user').

# HTTP example
response = timbr.run_query(
  url = "http://mytimbrenv.com:11000",
  ontology = "my_ontology",
  token = "tk_mytimbrtoken",
  query = "SELECT * FROM timbr.sys_concepts",
  datasource = "my_datasource",
  nested = "false",
  verify_ssl = False,
  enable_IPv6 = False,
)

print(response)


# Example for JWT token usage
response = timbr.run_query(
  url = "https://mytimbrenv.com:443",
  ontology = "my_ontology",
  token = "my_jwt_token",
  query = "SELECT * FROM timbr.sys_concepts",
  datasource = "my_datasource",
  nested = "false",
  verify_ssl = True,
  enable_IPv6 = False,
  is_jwt = True,
  jwt_tenant_id = "my_tenant_id",
)

print(response)


# HTTPS example
response = timbr.simpleQueryExecution(
  url = "https://mytimbrenv.com:443",
  ontology = "my_ontology",
  token = "tk_mytimbrtoken",
  query = "SELECT * FROM timbr.sys_concepts",
  datasource = "my_datasource",
  nested = "false",
  verify_ssl = True,
  enable_IPv6 = False,
)

print(response)
