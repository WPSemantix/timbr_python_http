![Timbr logo description](Timbr_logo.png)

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
  - `pip install pytimbr_api`

## Sample usage
- For an example of how to use the REST API connector for Timbr, follow this [Example file](example.py)

## Execute query with http connection
 ```python
  # For http connections
  response = timbr.executeQuery(hostname='<TIMBR_IP/HOST>', port='<TIMBR_PORT>', ontology='<ONTOLOGY_NAME>', token='<USER_TOKEN>', query='<TIMBR_QUERY>', enabled_ssl=False, verify_ssl=<True/False>, nested='<true/false>')

  # hostname - The IP / Hostname of the Timbr platform.
  # port - Timbr default port 443
  # ontology - the ontology / knowledge graph to connect to.
  # token - Timbr token value.
  # query - The query that you want to execute.
  # nested - Change to true if nested flag needs to be enabled.

  print(response)
```

## Execute query with https connection
 ```python
  # For https connections
  response = timbr.executeQuery(hostname='<TIMBR_IP/HOST>', port='<TIMBR_PORT>', ontology='<ONTOLOGY_NAME>', token='<USER_TOKEN>', query='<TIMBR_QUERY>', enabled_ssl=True, verify_ssl=<True/False>, nested='<true/false>')
  
  # hostname - string - The IP / Hostname of the Timbr platform.
  # port - string - Timbr default port 443.
  # ontology - string - The ontology / knowledge graph to connect to.
  # token - string - Timbr token value.
  # query - string - The query that you want to execute.
  # enabled_ssl - boolean - Use True for https connection and False for http connection.
  # verify_ssl - boolean - Verifying the target server’s SSL Certificate, use False to diable this proccess.
  # nested - string - Change to 'true' if nested flag needs to be enabled. make sure this flag contains string value not bool value.

  print(response)
```
