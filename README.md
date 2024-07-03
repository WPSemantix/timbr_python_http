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
- For an example of how to use the REST API connector for Timbr, follow this [Example file](examples/example.py)

## Connection parameters - general example
 ```python
  # General example for query execution
  response = pytimbr_api.executeQuery(
    hostname='<TIMBR_IP/HOST>',
    port='<TIMBR_PORT>',
    ontology='<ONTOLOGY_NAME>',
    token='<USER_TOKEN>',
    query='<TIMBR_QUERY>',
    enabled_ssl=<True/False>,
    verify_ssl=<True/False>,
    nested='<true/false>'
  )

  # hostname - String - The IP / Hostname of the Timbr platform.
  # port - String - Timbr's default port with enabled_ssl is 443 without SSL is 11000.
  # ontology - String - The ontology / knowledge graph to connect to.
  # token - String - Timbr token value.
  # query - String - The query that you want to execute.
  # enabled_ssl - Boolean - Use True for HTTPS connection and False for HTTP connection.
  # verify_ssl - Boolean - Verifying the target server's SSL Certificate, use False to disable this process.
  # nested - String - Change to 'true' if nested flag needs to be enabled. make sure this flag contains string value not bool value.
 ```

## Execute query with HTTP connection
 ```python
  # Example with dummy data for HTTP connections
  response = pytimbr_api.executeQuery(
    hostname='mytimbrenv.com',
    port='11000',
    ontology='my_ontology',
    token='tk_mytimbrtoken',
    query='SELECT * FROM timbr.sys_concepts',
    enabled_ssl=False,
    verify_ssl=False,
    nested='false'
  )
  print(response)
```

## Execute query with HTTPS connection
 ```python
  # Real Example with dummy data for HTTPS connections
  response = pytimbr_api.executeQuery(
    hostname='mytimbrenv.com',
    port='443',
    ontology='my_ontology',
    token='tk_mytimbrtoken',
    query='SELECT * FROM timbr.sys_concepts',
    enabled_ssl=True,
    verify_ssl=True,
    nested='false'
  )
  print(response)
```
