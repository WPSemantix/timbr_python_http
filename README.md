![Timbr logo description](https://timbr.ai/wp-content/uploads/2023/06/timbr-ai-l-5-226x60-1.png)

# timbr REST API connector sample file
This project is a sample connecting to timbr using REST API from Python.

## Dependencies
- Python 3.7.13+ or 3.8.x or 3.9.x

## Installation
- Install as clone repository:
  - Install Python: https://www.python.org/downloads/release/python-3713/

- Install using pip and git:
  - `pip install git+https://github.com/WPSemantix/timbr_python_http`

- Install using pip:
  - `pip install pytimbr-api`

## Sample usage
- For an example of how to use the simple execution method REST API connector for Timbr, follow this [Simple execution example file](examples/simpleExecution.py)
- For an example of how to use the advanced execution method REST API connector for Timbr, follow this [Advanced execution example file](examples/advancedExecution.py)

## Connection parameters examples

### Simple execute parameters
 ```python
  pytimbr_api.simpleQueryExecution(
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
 ```

### Advanced execute parameters
 ```python
  pytimbr_api.advancedQueryExecute(
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
 ```

## Execute query examples
### Simple execution
#### HTTP connection
 ```python
  # Example with dummy data for HTTP connections
  response = pytimbr_api.simpleQueryExecution(
    url = "http://mytimbrenv.com:443",
    ontology = "my_ontology",
    token = "tk_mytimbrtoken",
    query = "SELECT * FROM timbr.sys_concepts",
  )
  print(response)
```

#### HTTPS connection
 ```python
  # Example with dummy data for HTTPS connections
  response = pytimbr_api.simpleQueryExecution(
    url = "https://mytimbrenv.com:443",
    ontology = "my_ontology",
    token = "tk_mytimbrtoken",
    query = "SELECT * FROM timbr.sys_concepts",
  )
  print(response)
```

### Advanced execution
#### HTTP connection
 ```python
  # Example with dummy data for HTTP connections
  response = pytimbr_api.advancedQueryExecute(
    hostname = "mytimbrenv.com",
    port = "443",
    ontology = "my_ontology",
    token = "tk_mytimbrtoken",
    query = "SELECT * FROM timbr.sys_concepts",
    enabled_ssl = False,
    verify_ssl = False,
    nested = "false",
  )
  print(response)
```

#### HTTPS connection
 ```python
  # Example with dummy data for HTTPS connections
  response = pytimbr_api.advancedQueryExecute(
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
```