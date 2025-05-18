import pytest
import requests
import pandas as pd
from datetime import datetime
from utils.extract import scrape_page, scrape_main

def test_scrape_page():
    result = scrape_page(1)
    assert isinstance(result, list)
    assert len(result) >= 0
    if result:
        assert all(key in result[0] for key in ['Title', 'Price', 'Rating', 'Colors', 'Size', 'Gender', 'timestamp'])
        timestamp = result[0]['timestamp']
        try:
            datetime.fromisoformat(timestamp)
            assert True
        except ValueError:
            assert False, "Timestamp not in valid ISO format"

def test_scrape_page_error_handling(monkeypatch):
    def mock_get(*args, **kwargs):
        raise requests.RequestException("Simulated HTTP error")
    
    monkeypatch.setattr(requests, "get", mock_get)
    result = scrape_page(1)
    assert result == []

def test_scrape_main():
    result = scrape_main()
    assert isinstance(result, pd.DataFrame)
    assert all(col in result.columns for col in ['Title', 'Price', 'Rating', 'Colors', 'Size', 'Gender', 'timestamp'])

def test_scrape_main_error_handling(monkeypatch):
    def mock_scrape_page(*args, **kwargs):
        raise Exception("Simulated scrape error")
    
    monkeypatch.setattr("utils.extract.scrape_page", mock_scrape_page)
    result = scrape_main()
    assert result.empty