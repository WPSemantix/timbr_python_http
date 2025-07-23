import requests
from pytimbr_api.timbr_http_connector import run_query

def test_query_using_jwt(test_config):
    # Azure AD token endpoint URL
    token_url = f'https://login.microsoftonline.com/{test_config["jwt_tenant_id"]}/oauth2/v2.0/token'

    # Request payload for token exchange
    payload = {
        'client_id': test_config["jwt_client_id"],
        'client_secret': test_config["jwt_secret"],
        'scope': test_config["jwt_scope"],
        'username': test_config["jwt_username"],
        'password': test_config["jwt_password"],
        'grant_type': 'password'
    }

    # Request headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Make the request to get the access token
    response = requests.post(token_url, data=payload, headers=headers)
    tokens = response.json()

    access_token = None
    if response.status_code == 200:
        access_token = tokens.get('access_token')
        print(f"Access Token: {access_token}")
    else:
        print(f"Error fetching access token: {tokens}")
        assert False, f"Error fetching access token: {tokens}"
    
    results = run_query(
        url=test_config['url'],
        ontology=test_config['ontology'],
        token=access_token,
        query='SELECT 1',
        datasource=test_config['datasource'],
        nested='false',
        verify_ssl=test_config['verify_ssl'],
        enable_IPv6=test_config['enableIPv6'],
        is_jwt=True,
    )
    
    assert results is not None, "Results should not be None"
