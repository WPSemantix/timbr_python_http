import pytest
import pytimbr_api.timbr_http_connector as timbr

def test_run_query(test_config):
  url = test_config['url']
  ontology = test_config['ontology']
  token = test_config['token']
  query = test_config['query']

  results = timbr.run_query(url, ontology, token, query)

  print("Results:", results)

  assert results is not None, "Results should not be None"