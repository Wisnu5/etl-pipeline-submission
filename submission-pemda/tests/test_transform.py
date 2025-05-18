import pytest
import pandas as pd
import logging
from utils.transform import transform_data

logging.basicConfig(level=logging.INFO)

def test_transform_data():
    data = pd.DataFrame({
        'Title': ['Shirt', 'Unknown Product', 'Pants'],
        'Price': ['$10.00', '$20.00', '$30.00'],
        'Rating': ['4.5', 'Invalid Rating', '4.8'],
        'Colors': ['3 Colors', '2 Colors', '1 Colors'],
        'Size': ['Size: M', 'Size: L', 'Size: S'],
        'Gender': ['Gender: Male', 'Gender: Female', 'Gender: Male'],
        'timestamp': ['2025-05-17T19:00:00', '2025-05-17T19:00:00', '2025-05-17T19:00:00']
    })
    
    result = transform_data(data)
    assert len(result) == 2  
    assert result['Price'].iloc[0] == 160000.0  
    assert result['Rating'].dtype == 'float64'  
    assert result['Colors'].dtype == 'Int64'  
    assert 'Size: ' not in result['Size'].values  
    assert 'Gender: ' not in result['Gender'].values  
    assert result['Title'].dtype == 'object'  
    assert result['Size'].dtype == 'object'  
    assert result['Gender'].dtype == 'object'  

def test_transform_data_empty_input():
    data = pd.DataFrame(columns=['Title', 'Price', 'Rating', 'Colors', 'Size', 'Gender', 'timestamp'])
    result = transform_data(data)
    assert result.empty  