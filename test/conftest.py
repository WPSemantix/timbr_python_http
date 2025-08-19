import os
import pytest
from dotenv import load_dotenv

# Load .env file if it exists
load_dotenv(override=True)

def convert_env_to_bool(value):
  """Convert environment variable string to boolean."""
  if value is None:
    return None
  if value.lower() in ['true', '1', 'yes']:
    return True
  elif value.lower() in ['false', '0', 'no']:
    return False
  else:
    raise ValueError(f"Invalid boolean value: {value}")

# Global fixture to load config values
@pytest.fixture(scope="session")
def test_config():
  return {
    "url": os.getenv("URL"),
    "ontology": os.getenv("ONTOLOGY"),
    "token": os.getenv("TOKEN"),
    "query": os.getenv("QUERY"),
    "datasource": os.getenv("DATASORCE"),
    "hostname": os.getenv("HOSTNAME"),
    "port": os.getenv("PORT"),
    "enabled_ssl": convert_env_to_bool(os.getenv("ENABLED_SSL")),
    "verify_ssl": convert_env_to_bool(os.getenv("VERIFY_SSL")),
    "nested": os.getenv("NESTED"),
    "enableIPv6": convert_env_to_bool(os.getenv("ENABLE_IPV6")),
    "jwt_timbr_url": os.getenv("JWT_TIMBR_URL"),
    "jwt_timbr_ontology": os.getenv("JWT_TIMBR_ONTOLOGY"),
    "jwt_tenant_id": os.getenv("JWT_TENANT_ID"),
    "jwt_client_id": os.getenv("JWT_CLIENT_ID"),
    "jwt_username": os.getenv("JWT_USERNAME"),
    "jwt_password": os.getenv("JWT_PASSWORD"),
    "jwt_scope": os.getenv("JWT_SCOPE"),
    "jwt_secret": os.getenv("JWT_SECRET"),
  }
