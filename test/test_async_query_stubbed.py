import time
import pytest
from unittest.mock import patch, MagicMock
import pytimbr_api as timbr

MOCK_URL = 'http://mock-timbr.example.com:11000'
MOCK_ONTOLOGY = 'test_ontology'
MOCK_TOKEN = 'tk_test_api_key_12345'
MOCK_QUERY = 'SELECT * FROM timbr.sys_concepts'
MOCK_RESPONSE_ID = 'abc12345-0000-0000-0000-000000000001'


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _mock_200(data=None):
    mock = MagicMock()
    mock.status_code = 200
    mock.json.return_value = data or [{'concept': 'customer'}]
    return mock


def _mock_202(response_id=MOCK_RESPONSE_ID):
    mock = MagicMock()
    mock.status_code = 202
    mock.json.return_value = {
        'async': True,
        'response_id': response_id,
        'poll_url': f'/timbr/openapi/get-async-results/{response_id}',
        'message': 'Request accepted for async processing',
    }
    return mock


def _mock_get_running(response_id=MOCK_RESPONSE_ID):
    mock = MagicMock()
    mock.status_code = 200
    mock.json.return_value = {'status': 'running', 'response_id': response_id, 'message': 'Still processing'}
    return mock


def _mock_get_completed(data=None):
    mock = MagicMock()
    mock.status_code = 200
    mock.json.return_value = {
        'status': 'completed',
        'response': data or [{'concept': 'customer'}],
        'original_status_code': 200,
    }
    return mock


def _mock_get_error():
    mock = MagicMock()
    mock.status_code = 200
    mock.json.return_value = {'status': 'error', 'error': 'Query timed out', 'error_type': 'ExecutionError'}
    return mock


def _mock_get_404():
    mock = MagicMock()
    mock.status_code = 404
    mock.json.return_value = {'error': 'Response not found'}
    return mock


# ---------------------------------------------------------------------------
# run_query (sync mode) — unchanged behavior
# ---------------------------------------------------------------------------

@patch('pytimbr_api.timbr_http_connector.requests.post')
def test_run_query_sync_returns_data(mock_post):
    mock_post.return_value = _mock_200([{'id': 1}])
    result = timbr.run_query(MOCK_URL, MOCK_ONTOLOGY, MOCK_TOKEN, MOCK_QUERY)
    assert result == [{'id': 1}]


@patch('pytimbr_api.timbr_http_connector.requests.post')
def test_run_query_sync_does_not_send_x_async_header(mock_post):
    mock_post.return_value = _mock_200()
    timbr.run_query(MOCK_URL, MOCK_ONTOLOGY, MOCK_TOKEN, MOCK_QUERY)
    _, kwargs = mock_post.call_args
    assert 'x-async' not in kwargs['headers']


# ---------------------------------------------------------------------------
# run_query(is_async=True) — submit + poll
# ---------------------------------------------------------------------------

@patch('pytimbr_api.timbr_http_connector.requests.post')
def test_is_async_sends_x_async_header(mock_post):
    mock_post.return_value = _mock_202()
    timbr.run_query(MOCK_URL, MOCK_ONTOLOGY, MOCK_TOKEN, MOCK_QUERY, is_async=True)
    _, kwargs = mock_post.call_args
    assert kwargs['headers']['x-async'] == 'true'


@patch('pytimbr_api.timbr_http_connector.requests.post')
def test_is_async_returns_submission_body(mock_post):
    mock_post.return_value = _mock_202()
    result = timbr.run_query(MOCK_URL, MOCK_ONTOLOGY, MOCK_TOKEN, MOCK_QUERY, is_async=True)
    assert result['response_id'] == MOCK_RESPONSE_ID
    assert result['async'] is True
    assert 'poll_url' in result


@patch('pytimbr_api.timbr_http_connector.requests.post')
def test_is_async_sends_api_key_header(mock_post):
    mock_post.return_value = _mock_202()
    timbr.run_query(MOCK_URL, MOCK_ONTOLOGY, MOCK_TOKEN, MOCK_QUERY, is_async=True)
    _, kwargs = mock_post.call_args
    assert kwargs['headers']['x-api-key'] == MOCK_TOKEN


@patch('pytimbr_api.timbr_http_connector.requests.post')
def test_is_async_jwt_headers(mock_post):
    mock_post.return_value = _mock_202()
    timbr.run_query(MOCK_URL, MOCK_ONTOLOGY, 'jwt_token', MOCK_QUERY,
                    is_jwt=True, jwt_tenant_id='tenant1', is_async=True)
    _, kwargs = mock_post.call_args
    assert kwargs['headers']['x-jwt-token'] == 'jwt_token'
    assert kwargs['headers']['x-jwt-tenant-id'] == 'tenant1'


@patch('pytimbr_api.timbr_http_connector.requests.post')
def test_is_async_raises_on_non_202(mock_post):
    mock = MagicMock()
    mock.status_code = 500
    mock.text = 'Internal Server Error'
    mock_post.return_value = mock
    with pytest.raises(Exception, match='Error submitting async query'):
        timbr.run_query(MOCK_URL, MOCK_ONTOLOGY, MOCK_TOKEN, MOCK_QUERY, is_async=True)


@patch('pytimbr_api.timbr_http_connector.requests.post')
def test_is_async_with_datasource(mock_post):
    mock_post.return_value = _mock_202()
    timbr.run_query(MOCK_URL, MOCK_ONTOLOGY, MOCK_TOKEN, MOCK_QUERY, datasource='my_ds', is_async=True)
    call_url = mock_post.call_args[0][0]
    assert 'datasource=my_ds' in call_url


@patch('pytimbr_api.timbr_http_connector.requests.post')
def test_is_async_raises_when_no_response_id(mock_post):
    mock = MagicMock()
    mock.status_code = 202
    mock.json.return_value = {'async': True}  # missing response_id
    mock_post.return_value = mock
    with pytest.raises(Exception, match='did not return a response_id'):
        timbr.run_query(MOCK_URL, MOCK_ONTOLOGY, MOCK_TOKEN, MOCK_QUERY, is_async=True)


# ---------------------------------------------------------------------------
# get_async_result — single poll
# ---------------------------------------------------------------------------

@patch('pytimbr_api.timbr_http_connector.requests.get')
def test_get_async_result_returns_completed(mock_get):
    mock_get.return_value = _mock_get_completed([{'id': 42}])
    result = timbr.get_async_result(MOCK_URL, MOCK_RESPONSE_ID, MOCK_TOKEN)
    assert result['status'] == 'completed'
    assert result['response'] == [{'id': 42}]


@patch('pytimbr_api.timbr_http_connector.requests.get')
def test_get_async_result_returns_running(mock_get):
    mock_get.return_value = _mock_get_running()
    result = timbr.get_async_result(MOCK_URL, MOCK_RESPONSE_ID, MOCK_TOKEN)
    assert result['status'] == 'running'


@patch('pytimbr_api.timbr_http_connector.requests.get')
def test_get_async_result_raises_on_404(mock_get):
    mock_get.return_value = _mock_get_404()
    with pytest.raises(Exception, match='Async result not found'):
        timbr.get_async_result(MOCK_URL, MOCK_RESPONSE_ID, MOCK_TOKEN)


@patch('pytimbr_api.timbr_http_connector.requests.get')
def test_get_async_result_returns_error_status(mock_get):
    mock_get.return_value = _mock_get_error()
    result = timbr.get_async_result(MOCK_URL, MOCK_RESPONSE_ID, MOCK_TOKEN)
    assert result['status'] == 'error'


@patch('pytimbr_api.timbr_http_connector.requests.get')
def test_get_async_result_sends_api_key_header(mock_get):
    mock_get.return_value = _mock_get_completed()
    timbr.get_async_result(MOCK_URL, MOCK_RESPONSE_ID, MOCK_TOKEN)
    _, kwargs = mock_get.call_args
    assert kwargs['headers']['x-api-key'] == MOCK_TOKEN


@patch('pytimbr_api.timbr_http_connector.requests.get')
def test_get_async_result_jwt_headers(mock_get):
    mock_get.return_value = _mock_get_completed()
    timbr.get_async_result(MOCK_URL, MOCK_RESPONSE_ID, 'jwt_token',
                            is_jwt=True, jwt_tenant_id='tenant1')
    _, kwargs = mock_get.call_args
    assert kwargs['headers']['x-jwt-token'] == 'jwt_token'
    assert kwargs['headers']['x-jwt-tenant-id'] == 'tenant1'


@patch('pytimbr_api.timbr_http_connector.requests.get')
def test_get_async_result_uses_correct_url(mock_get):
    mock_get.return_value = _mock_get_completed()
    timbr.get_async_result(MOCK_URL, MOCK_RESPONSE_ID, MOCK_TOKEN)
    call_url = mock_get.call_args[0][0]
    assert MOCK_RESPONSE_ID in call_url
    assert 'get-async-results' in call_url


@patch('pytimbr_api.timbr_http_connector.requests.get')
def test_get_async_result_raises_on_non_200(mock_get):
    mock = MagicMock()
    mock.status_code = 500
    mock.text = 'Internal Server Error'
    mock_get.return_value = mock
    with pytest.raises(Exception, match='Error fetching async result'):
        timbr.get_async_result(MOCK_URL, MOCK_RESPONSE_ID, MOCK_TOKEN)
