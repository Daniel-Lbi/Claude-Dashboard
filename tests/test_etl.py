import pytest
import pandas as pd
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import get_data

def test_extract_data():
    """Test data extraction from API"""
    # Using a reliable test API
    api_url = "https://httpbin.org/json"
    data = extract_data(api_url)
    assert data is not None
    assert isinstance(data, dict)

def test_transform_data():
    """Test data transformation"""
    sample_data = [
        {"id": 1, "title": "Test Post", "body": "Test body"},
        {"id": 2, "title": "Another Post", "body": "Another body"}
    ]
    df = transform_data(sample_data)
    assert df is not None
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert 'processed_at' in df.columns

def test_load_and_get_data():
    """Test data loading and retrieval"""
    sample_df = pd.DataFrame({
        'id': [1, 2],
        'title': ['Test', 'Data'],
        'processed_at': pd.Timestamp.now()
    })
    
    from etl.load import load_data
    load_data(sample_df, db_path='test_data.db', table_name='test_table')
    
    retrieved_df = get_data(db_path='test_data.db', table_name='test_table')
    assert retrieved_df is not None
    assert len(retrieved_df) == 2
    
    # Clean up
    import os
    if os.path.exists('test_data.db'):
        os.remove('test_data.db')