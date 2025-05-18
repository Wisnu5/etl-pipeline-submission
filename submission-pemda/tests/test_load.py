import pytest
import pandas as pd
import gspread
import psycopg2
from utils.load import save_to_csv, save_to_google_sheets, save_to_postgres

def test_save_to_csv(tmp_path):
    data = pd.DataFrame({
        'Title': ['Shirt'],
        'Price': [160000.0],
        'Rating': [4.5],
        'Colors': [3],
        'Size': ['M'],
        'Gender': ['Male'],
        'timestamp': ['2025-05-17T19:00:00']
    })
    
    file_path = tmp_path / "test.csv"
    save_to_csv(data, file_path)
    
    result = pd.read_csv(file_path)
    assert len(result) == 1
    assert result['Title'].iloc[0] == 'Shirt'

def test_save_to_csv_error_handling(tmp_path, monkeypatch):
    def mock_to_csv(*args, **kwargs):
        raise Exception("Simulated CSV write error")
    
    monkeypatch.setattr(pd.DataFrame, "to_csv", mock_to_csv)
    
    data = pd.DataFrame({
        'Title': ['Shirt'],
        'Price': [160000.0],
        'Rating': [4.5],
        'Colors': [3],
        'Size': ['M'],
        'Gender': ['Male'],
        'timestamp': ['2025-05-17T19:00:00']
    })
    
    file_path = tmp_path / "test.csv"
    save_to_csv(data, file_path)

def test_save_to_google_sheets(monkeypatch):
    data = pd.DataFrame({
        'Title': ['Shirt'],
        'Price': [160000.0],
        'Rating': [4.5],
        'Colors': [3],
        'Size': ['M'],
        'Gender': ['Male'],
        'timestamp': ['2025-05-17T19:00:00']
    })
    
    def mock_authorize(*args, **kwargs):
        class MockClient:
            def open(self, *args):
                class MockSheet:
                    def get_worksheet(self, *args):
                        return None
                    def add_worksheet(self, *args, **kwargs):
                        return MockWorksheet()
                    def share(self, *args, **kwargs):
                        pass
                return MockSheet()
            def create(self, *args):
                class MockSheet:
                    def get_worksheet(self, *args):
                        return None
                    def add_worksheet(self, *args, **kwargs):
                        return MockWorksheet()
                    def share(self, *args, **kwargs):
                        pass
                return MockSheet()
        return MockClient()
    
    class MockWorksheet:
        def update(self, *args, **kwargs):
            pass
    
    monkeypatch.setattr(gspread, "authorize", mock_authorize)
    save_to_google_sheets(data)

def test_save_to_postgres(monkeypatch):
    data = pd.DataFrame({
        'Title': ['Shirt'],
        'Price': [160000.0],
        'Rating': [4.5],
        'Colors': [3],
        'Size': ['M'],
        'Gender': ['Male'],
        'timestamp': ['2025-05-17T19:00:00']
    })
    
    class MockConnection:
        def cursor(self):
            return MockCursor()
        def commit(self):
            pass
        def close(self):
            pass
    
    class MockCursor:
        def execute(self, *args, **kwargs):
            pass
        def close(self):
            pass
    
    monkeypatch.setattr(psycopg2, "connect", lambda **kwargs: MockConnection())
    save_to_postgres(data, {'dbname': 'etl_submission', 'user': 'postgres', 'password': 'wisnu154', 'host': 'localhost', 'port': '5432'})