import pytest
import pytimbr_api.timbr_http_connector as timbr

def test_simple_connection(test_config):
  url = test_config['url']
  ontology = test_config['ontology']
  token = test_config['token']
  query = test_config['query']

  results = timbr.simpleQueryExecution(url, ontology, token, query)
  
  print("Results:", results)

  assert results is not None, "Results should not be None"

def test_advanced_connection(test_config):
  hostname = test_config['hostname']
  port = test_config['port']
  ontology = test_config['ontology']
  token = test_config['token']
  query = test_config['query']
  enabled_ssl = test_config['enabled_ssl']
  verify_ssl = test_config['verify_ssl']
  nested = test_config['nested']
  enableIPv6 = test_config['enableIPv6']
  datasource = test_config['datasource']

  results = timbr.advancedQueryExecute(
    hostname,
    port,
    ontology,
    token,
    query,
    enabled_ssl,
    verify_ssl,
    nested,
    enableIPv6,
    datasource,
  )
  
  print("Results:", results)

  assert results is not None, "Results should not be None"

def test_legacy_connection(test_config):
  hostname = test_config['hostname']
  port = test_config['port']
  ontology = test_config['ontology']
  token = test_config['token']
  query = test_config['query']
  enabled_ssl = test_config['enabled_ssl']
  verify_ssl = test_config['verify_ssl']
  nested = test_config['nested']

  results = timbr.executeQuery(
    hostname,
    port,
    ontology,
    token,
    query,
    enabled_ssl,
    verify_ssl,
    nested,
  )
  
  print("Results:", results)

  assert results is not None, "Results should not be None"