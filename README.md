![Timbr logo description](https://timbr.ai/wp-content/uploads/2023/06/timbr-ai-l-5-226x60-1.png)

# timbr REST API connector using Python
This project is a pure python connector to timbr (no dependencies required).

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
- For an example of how to use the REST API connector for Timbr, follow this [Example file](examples/example.py)

## Connection parameters examples

### Generic example and explanation for each parameter
```python
  pytimbr_api.run_query(
    url = "<TIMBR_URL>",
    ontology = "<ONTOLOGY_NAME>",
    token = "<USER_TOKEN>",
    query = "<TIMBR_QUERY>",
    datasource = "<DATASOURCE_NAME>",
    nested = "<true/false>",
    verify_ssl = <True/False>,
    enableIPv6 = <True/False>,
  )

  # url         - Required - String - The IP / Hostname of the Timbr platform.
  # ontology    - Required - String - The ontology / knowledge graph to connect to.
  # token       - Required - String - Timbr token value.
  # query       - Required - String - The query that you want to execute.
  # datasource  - Optional - String - Add the specific datasource name that you want to query from, the default value is the current active datasource of your ontology.
  # nested      - Optional - String - Change to 'true' if nested flag needs to be enabled. make sure this flag contains string value not bool value.
  # verify_ssl  - Optional - Boolean - Verifying the target server's SSL Certificate, use False to disable this process.
  # enableIPv6  - Optional - Boolean - Change to 'true' if you are using IPv6 connection.
```

### HTTP example
```python
  pytimbr_api.run_query(
    url = "http://mytimbrenv.com:11000",
    ontology = "my_ontology",
    token = "tk_mytimbrtoken",
    query = "SELECT * FROM timbr.sys_concepts",
    datasource = "my_datasource",
    nested = "false",
    verify_ssl = False,
    enableIPv6 = False,
  )
```

### HTTPS example
```python
  pytimbr_api.run_query(
    url = "https://mytimbrenv.com:443",
    ontology = "my_ontology",
    token = "tk_mytimbrtoken",
    query = "SELECT * FROM timbr.sys_concepts",
    datasource = "my_datasource",
    nested = "false",
    verify_ssl = True,
    enableIPv6 = False,
  )
```

## Execute query examples
### HTTP connection
```python
  response = pytimbr_api.run_query(
    url = "http://mytimbrenv.com:11000",
    ontology = "my_ontology",
    token = "tk_mytimbrtoken",
    query = "SELECT * FROM timbr.sys_concepts",
    datasource = "my_datasource",
    nested = "false",
    verify_ssl = False,
    enableIPv6 = False,
  )
  print(response)
```

### HTTPS connection
```python
  response = pytimbr_api.run_query(
    url = "https://mytimbrenv.com:443",
    ontology = "my_ontology",
    token = "tk_mytimbrtoken",
    query = "SELECT * FROM timbr.sys_concepts",
    datasource = "my_datasource",
    nested = "false",
    verify_ssl = True,
    enableIPv6 = False,
  )
  print(response)
```
