![Timbr logo description](https://timbr.ai/wp-content/uploads/2023/06/timbr-ai-l-5-226x60-1.png)

[![license](https://img.shields.io/github/license/WPSemantix/timbr_http)](https://github.com/WPSemantix/timbr_http/blob/main/LICENSE)
[![PypiVersion](https://img.shields.io/pypi/v/pytimbr-api.svg)](https://badge.fury.io/py/pytimbr-api)
[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B50508%2Fgithub.com%2FWPSemantix%2Ftimbr_python_http.svg?type=shield&issueType=license)](https://app.fossa.com/projects/custom%2B50508%2Fgithub.com%2FWPSemantix%2Ftimbr_python_http?ref=badge_shield&issueType=license)
[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B50508%2Fgithub.com%2FWPSemantix%2Ftimbr_python_http.svg?type=shield&issueType=security)](https://app.fossa.com/projects/custom%2B50508%2Fgithub.com%2FWPSemantix%2Ftimbr_python_http?ref=badge_shield&issueType=security)

[![Python 3.7.13](https://img.shields.io/badge/python-3.7.13+-blue.svg)](https://www.python.org/downloads/release/python-3713/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-3820/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-3921/)

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
```

### HTTP example
```python
  pytimbr_api.run_query(
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
```

### HTTPS example
```python
  pytimbr_api.run_query(
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
```

## Execute query examples
### HTTP connection
```python
  response = pytimbr_api.run_query(
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
```

### HTTPS connection
```python
  response = pytimbr_api.run_query(
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
```
