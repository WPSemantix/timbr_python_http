import requests
import pytest
import time
from pytimbr_api.timbr_http_connector import run_query

create_granting_user_stmt = "CREATE USER {username} OPTIONS(email='{username}@timbr-test.ai', password='{password}', first_name='{first_name}', last_name='{last_name}');" \
                   "GRANT QUERY ON ALL DATASOURCE TO USER {username};" \
                   "GRANT ACCESS ON ALL ONTOLOGY TO USER {username};" \
                   "GRANT EDIT ON ALL USER TO USER {username};"

create_impersonating_user_stmt = "CREATE USER {username} OPTIONS(email='{username}@timbr-test.ai', password='{password}', first_name='{first_name}', last_name='{last_name}');" \
                   "GRANT ACCESS ON ALL ONTOLOGY TO USER {username};" \
                   "GRANT QUERY ON ALL USER TO USER {username};"

grant_auth_stmt = "GRANT AUTH ON user.{granting} TO USER `{impersonating}`"

revoke_auth_stmt = "REVOKE AUTH ON user.{granting} FROM USER `{impersonating}`"

drop_user_stmt = "REVOKE EDIT ON ALL USER FROM USER {username};" \
"REVOKE ACCESS ON ALL ONTOLOGY FROM USER {username};" \
"REVOKE QUERY ON ALL DATASOURCE FROM USER {username};" \
"DROP USER {username};"

granting_user = "timbr_python_http_granting_user"
impersonating_user = "timbr_python_http_impersonating_user"

def create_users(test_config):
    print("Creating users...")
    granting_user_stmt = create_granting_user_stmt.format(username=granting_user, password="SecurePassword123", first_name="Granting", last_name="User")
    impersonating_user_stmt = create_impersonating_user_stmt.format(username=impersonating_user, password="SecurePassword123", first_name="Impersonating", last_name="User")

    run_query(
        url=test_config['url'],
        ontology=test_config['ontology'],
        token=test_config['token'],
        query=granting_user_stmt,
        datasource=test_config['datasource'],
        nested='false',
        verify_ssl=test_config['verify_ssl'],
        enable_IPv6=test_config['enableIPv6'],
    )
    run_query(
        url=test_config['url'],
        ontology=test_config['ontology'],
        token=test_config['token'],
        query=impersonating_user_stmt,
        datasource=test_config['datasource'],
        nested='false',
        verify_ssl=test_config['verify_ssl'],
        enable_IPv6=test_config['enableIPv6'],
    )

    grant_auth = grant_auth_stmt.format(granting=granting_user, impersonating=impersonating_user)
    run_query(
        url=test_config['url'],
        ontology=test_config['ontology'],
        token=test_config['token'],
        query=grant_auth,
        datasource=test_config['datasource'],
        nested='false',
        verify_ssl=test_config['verify_ssl'],
        enable_IPv6=test_config['enableIPv6'],
    )

    # Waiting for user creation to propagate
    run_query(
        url=test_config['url'],
        ontology=test_config['ontology'],
        token=test_config['token'],
        query="refresh permissions",
        datasource=test_config['datasource'],
        nested='false',
        verify_ssl=test_config['verify_ssl'],
        enable_IPv6=test_config['enableIPv6'],
    )


def drop_users(test_config):
    print("\nDropping users...")
    revoke_cmd = revoke_auth_stmt.format(granting=granting_user, impersonating=impersonating_user)
    run_query(
        url=test_config['url'],
        ontology=test_config['ontology'],
        token=test_config['token'],
        query=revoke_cmd,
        datasource=test_config['datasource'],
        nested='false',
        verify_ssl=test_config['verify_ssl'],
        enable_IPv6=test_config['enableIPv6'],
    )

    drop_impersonating_user_stmt = drop_user_stmt.format(username=impersonating_user)
    run_query(
        url=test_config['url'],
        ontology=test_config['ontology'],
        token=test_config['token'],
        query=drop_impersonating_user_stmt,
        datasource=test_config['datasource'],
        nested='false',
        verify_ssl=test_config['verify_ssl'],
        enable_IPv6=test_config['enableIPv6'],
    )

    drop_granting_user_stmt = drop_user_stmt.format(username=granting_user)
    run_query(
        url=test_config['url'],
        ontology=test_config['ontology'],
        token=test_config['token'],
        query=drop_granting_user_stmt,
        datasource=test_config['datasource'],
        nested='false',
        verify_ssl=test_config['verify_ssl'],
        enable_IPv6=test_config['enableIPv6'],
    )

@pytest.fixture(scope="class")
def setup_test_users(test_config):
    """Fixture to create users at the start and drop them at the end"""
    # Setup: Create users
    create_users(test_config)
    
    yield test_config  # This provides the test_config to the test
    
    # Teardown: Drop users (runs even if tests fail)
    try:
        drop_users(test_config)
    except Exception as e:
        print(f"Warning: Failed to drop users during teardown: {e}")

class TestUserImpersonation:
    def test_user_impersonation(self, setup_test_users):
        test_config = setup_test_users
        
        impersonating_user_token_res = run_query(
            url=test_config['url'],
            ontology=test_config['ontology'],
            token=test_config['token'],
            query=f"show token for `{impersonating_user}`",
            datasource=test_config['datasource'],
            nested='false',
            verify_ssl=test_config['verify_ssl'],
            enable_IPv6=test_config['enableIPv6'],
        )

        impersonating_user_token = impersonating_user_token_res[0]['token']

        # Act
        res = run_query(
            url=test_config['url'],
            ontology=test_config['ontology'],
            token=impersonating_user_token,
            query='select timbr_username()',
            datasource=test_config['datasource'],
            nested='false',
            verify_ssl=test_config['verify_ssl'],
            enable_IPv6=test_config['enableIPv6'],
            additional_headers={
                "x-api-impersonate-user": granting_user
            }
        )
        assert res[0].keys() == {'timbr_python_http_granting_user'}
        assert res[0]['timbr_python_http_granting_user'] == 'timbr_python_http_granting_user'
