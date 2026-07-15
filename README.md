![Timbr logo](https://timbr.ai/wp-content/uploads/2025/01/logotimbrai230125.png)

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FWPSemantix%2Ftimbr_python_http.svg?type=shield&issueType=license)](https://app.fossa.com/projects/git%2Bgithub.com%2FWPSemantix%2Ftimbr_python_http?ref=badge_shield&issueType=license)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FWPSemantix%2Ftimbr_python_http.svg?type=shield&issueType=security)](https://app.fossa.com/projects/git%2Bgithub.com%2FWPSemantix%2Ftimbr_python_http?ref=badge_shield&issueType=security)

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-31017/)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-31112/)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3129/)

[![PypiVersion](https://img.shields.io/pypi/v/pytimbr-api.svg)](https://badge.fury.io/py/pytimbr-api)

# timbr REST API connector using Python
This project is a pure python connector to timbr (no dependencies required).

## Dependencies
- Access to a timbr-server
- Python from 3.10 or newer

## Installation
- Install as clone repository:
  - Install Python: https://www.python.org/downloads/release/python-3913/

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
    enable_IPv6 = <True/False>,
    is_jwt = <True/False>,
    jwt_tenant_id = "<JWT_TENANT_ID>",
    additional_headers = <{ "x-api-impersonate-user": "<user to impersonate>" }>,
    is_async = <True/False>,
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
  # jwt_tenant_id       - Optional - String - The tenant ID for JWT authentication.
  # additional_headers  - Optional - Dict - Extra Timbr connection parameters sent with every request (e.g., 'x-api-impersonate-user').
  # is_async            - Optional - Boolean - Set to True to submit the query asynchronously. Returns the submission response (including response_id) immediately instead of waiting for the result. Use get_async_result() to poll for completion. Default: False.
```

## Async query execution

For long-running queries that may time out on a synchronous HTTP connection, use the two-step async flow:

1. **Submit** — call `run_query` with `is_async=True`. It returns immediately with a submission response containing a `response_id`.
2. **Poll** — call `get_async_result` with the `response_id` to check the status. Repeat until `status` is `'completed'` or `'error'`.

```python
import time
import pytimbr_api

URL = "https://mytimbrenv.com:443"
ONTOLOGY = "my_ontology"
TOKEN = "tk_mytimbrtoken"

# Step 1: submit the query asynchronously
submission = pytimbr_api.run_query(
  url = URL,
  ontology = ONTOLOGY,
  token = TOKEN,
  query = "SELECT * FROM timbr.large_table",
  is_async = True,
)
response_id = submission["response_id"]
print(f"Query submitted — response_id: {response_id}")

# Step 2: poll until the result is ready
while True:
  result = pytimbr_api.get_async_result(
    url = URL,
    response_id = response_id,
    token = TOKEN,
  )
  status = result["status"]
  if status == "completed":
    print(result["response"])
    break
  elif status == "error":
    raise Exception(f"Query failed: {result.get('error')}")
  else:
    print(f"Status: {status} — waiting...")
    time.sleep(3)
```

`get_async_result` makes a **single** request each call and returns the raw server response — polling cadence and timeout logic are left to the caller.

### Using Timbr token

#### HTTP example
```python
  pytimbr_api.run_query(
    url = "http://mytimbrenv.com:11000",
    ontology = "my_ontology",
    token = "tk_mytimbrtoken",
    query = "SELECT * FROM timbr.sys_concepts",
    datasource = "my_datasource",
    nested = "false",
    verify_ssl = False,
    enable_IPv6 = False,
  )
```

#### HTTPS example
```python
  pytimbr_api.run_query(
    url = "https://mytimbrenv.com:443",
    ontology = "my_ontology",
    token = "tk_mytimbrtoken",
    query = "SELECT * FROM timbr.sys_concepts",
    datasource = "my_datasource",
    nested = "false",
    verify_ssl = True,
    enable_IPv6 = False,
  )
```

### Using JWT token

#### HTTP example
```python
  pytimbr_api.run_query(
    url = "http://mytimbrenv.com:11000",
    ontology = "my_ontology",
    token = "tk_mytimbrtoken",
    query = "SELECT * FROM timbr.sys_concepts",
    datasource = "my_datasource",
    nested = "false",
    verify_ssl = False,
    enable_IPv6 = False,
    is_jwt = True,
    jwt_tenant_id = "my_tenant_id",
  )
```

#### HTTPS example
```python
  pytimbr_api.run_query(
    url = "https://mytimbrenv.com:11000",
    ontology = "my_ontology",
    token = "tk_mytimbrtoken",
    query = "SELECT * FROM timbr.sys_concepts",
    datasource = "my_datasource",
    nested = "false",
    verify_ssl = True,
    enable_IPv6 = False,
    is_jwt = True,
    jwt_tenant_id = "my_tenant_id",
  )
```

## Execute query examples

### Using Timbr token

#### HTTP connection
```python
  response = pytimbr_api.run_query(
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
```

#### HTTPS connection
```python
  response = pytimbr_api.run_query(
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
```

### Using JWT token

#### HTTP example
```python
  response = pytimbr_api.run_query(
    url = "http://mytimbrenv.com:11000",
    ontology = "my_ontology",
    token = "tk_mytimbrtoken",
    query = "SELECT * FROM timbr.sys_concepts",
    datasource = "my_datasource",
    nested = "false",
    verify_ssl = False,
    enable_IPv6 = False,
    is_jwt = True,
    jwt_tenant_id = "my_tenant_id",
  )
  print(response)
```

#### HTTPS example
```python
  response = pytimbr_api.run_query(
    url = "https://mytimbrenv.com:11000",
    ontology = "my_ontology",
    token = "tk_mytimbrtoken",
    query = "SELECT * FROM timbr.sys_concepts",
    datasource = "my_datasource",
    nested = "false",
    verify_ssl = True,
    enable_IPv6 = False,
    is_jwt = True,
    jwt_tenant_id = "my_tenant_id",
  )
  print(response)
```
