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
  - `pip install PyTimbrRestAPI`

## Sample usage
- For an example of how to use the REST API connector for Timbr, follow this [Example file](example.py)

## Execute query with http connection
 ```python
  # For http connections
  response = PyTimbrRestAPI.executeQuery(hostname='<TIMBR_IP/HOST>', port='<TIMBR_PORT>', ontology='<ONTOLOGY_NAME>', token='<USER_TOKEN>', query='<TIMBR_QUERY>', nested='<true/false>')

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
  # For http connections
  response = PyTimbrRestAPI.securedExecuteQuery(hostname='<TIMBR_IP/HOST>', port='<TIMBR_PORT>', ontology='<ONTOLOGY_NAME>', token='<USER_TOKEN>', query='<TIMBR_QUERY>', nested='<true/false>')

  # hostname - The IP / Hostname of the Timbr platform.
  # port - Timbr default port 443
  # ontology - the ontology / knowledge graph to connect to.
  # token - Timbr token value.
  # query - The query that you want to execute.
  # nested - Change to true if nested flag needs to be enabled.

  print(response)
```
