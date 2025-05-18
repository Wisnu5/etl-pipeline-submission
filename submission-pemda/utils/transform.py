import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def transform_data(df):
    """Transformasi data hasil scraping."""
    try:
        if df.empty:
            logging.warning("Input DataFrame is empty.")
            return pd.DataFrame()

        # Menghapus entri yang tidak valid (Title = 'Unknown Product')
        df = df[df['Title'] != 'Unknown Product'].copy()
        
        # Membersihkan Price: Hapus '$' dan konversi ke Rupiah (1 USD = Rp16,000)
        df['Price'] = df['Price'].replace(r'[\$,]', '', regex=True).astype('float64') * 16000
        
        # Menghapus baris dengan Price == 0
        df = df[df['Price'] > 0].copy()
        
        # Membersihkan Rating: Ekstrak angka desimal, tangani 'Invalid Rating'
        df['Rating'] = df['Rating'].replace('Invalid Rating', '0').str.extract(r'(\d+\.\d)').astype('float64')
        df['Rating'] = df['Rating'].fillna(0.0)
        
        # Membersihkan Colors: Ekstrak angka, konversi ke Int64
        df['Colors'] = df['Colors'].str.replace(' Colors', '', regex=False).astype('Int64')
        
        # Membersihkan Size: Hapus 'Size: '
        df['Size'] = df['Size'].str.replace('Size: ', '', regex=False)
        
        # Membersihkan Gender: Hapus 'Gender: '
        df['Gender'] = df['Gender'].str.replace('Gender: ', '', regex=False)
        
        # Hapus duplikat dan nilai null
        df = df.drop_duplicates().dropna()
        
        # Memastikan tipe data yang benar
        df = df.astype({
            'Title': 'object',
            'Price': 'float64',
            'Rating': 'float64',
            'Colors': 'Int64',
            'Size': 'object',
            'Gender': 'object',
            'timestamp': 'object'
        })
        
        logging.info(f"Transformed data: {len(df)} rows.")
        return df
    
    except Exception as e:
        logging.error(f"Error in transformation: {e}")
        return pd.DataFrame()