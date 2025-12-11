import pytest
from pytimbr_api.timbr_http_connector import run_query


def test_run_query_with_unicode_characters(test_config):
    """Test that queries with unicode characters are properly encoded to UTF-8."""
    url = test_config['url']
    ontology = test_config['ontology']
    token = test_config['token']
    
    # Query with unicode characters - using simple SELECT with unicode strings
    # This tests that UTF-8 encoding works without requiring specific tables
    query_with_unicode = "SELECT '测试' as chinese, 'café' as french, '😀' as emoji"
    
    results = run_query(url, ontology, token, query_with_unicode)
    
    assert results is not None, "Results should not be None for unicode query"
    assert len(results) > 0, "Results should contain data"
    # Verify unicode characters are correctly processed in results
    first_row = results[0]
    assert first_row['chinese'] == '测试', "Chinese characters should be preserved"
    assert first_row['french'] == 'café', "French accented characters should be preserved"
    assert first_row['emoji'] == '😀', "Emoji should be preserved"


def test_run_query_with_already_encoded_bytes(test_config):
    """Test that queries already encoded as bytes are handled correctly."""
    url = test_config['url']
    ontology = test_config['ontology']
    token = test_config['token']
    
    # Query already encoded as bytes
    query_as_bytes = b"SELECT 1"
    
    results = run_query(url, ontology, token, query_as_bytes)
    
    assert results is not None, "Results should not be None for bytes query"
    assert len(results) > 0, "Results should contain data"


def test_run_query_with_special_sql_characters(test_config):
    """Test that queries with special SQL characters are properly encoded."""
    url = test_config['url']
    ontology = test_config['ontology']
    token = test_config['token']
    
    # Query with special characters that need proper encoding
    query_with_special_chars = "SELECT 'O''Brien' as name, '©' as copyright"
    
    results = run_query(url, ontology, token, query_with_special_chars)
    
    assert results is not None, "Results should not be None for query with special characters"
    assert len(results) > 0, "Results should contain data"
    # Verify special characters are correctly processed in results
    first_row = results[0]
    assert first_row['name'] == "O'Brien", "Apostrophe in name should be preserved"
    assert first_row['copyright'] == '©', "Copyright symbol should be preserved"


def test_run_query_with_multilingual_text(test_config):
    """Test that queries with multiple languages are properly encoded."""
    url = test_config['url']
    ontology = test_config['ontology']
    token = test_config['token']
    
    # Query with multiple languages (Latin, Cyrillic, Arabic, Japanese)
    query_multilingual = "SELECT 'Hello' as english, 'Привет' as russian, 'مرحبا' as arabic, 'こんにちは' as japanese"
    
    results = run_query(url, ontology, token, query_multilingual)
    
    assert results is not None, "Results should not be None for multilingual query"
    assert len(results) > 0, "Results should contain data"
    # Verify multilingual characters are correctly processed in results
    first_row = results[0]
    assert first_row['english'] == 'Hello', "English text should be preserved"
    assert first_row['russian'] == 'Привет', "Russian Cyrillic text should be preserved"
    assert first_row['arabic'] == 'مرحبا', "Arabic text should be preserved"
    assert first_row['japanese'] == 'こんにちは', "Japanese text should be preserved"
