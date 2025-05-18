import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import psycopg2
from psycopg2 import sql
import logging

logging.basicConfig(level=logging.INFO)

def save_to_csv(df, filename='products.csv'):
    """Menyimpan DataFrame ke CSV."""
    try:
        df.to_csv(filename, index=False)
        logging.info(f"Successfully saved to CSV: {filename}")
    except Exception as e:
        logging.error(f"Error saving to CSV: {e}")

def save_to_google_sheets(df, credentials_file='google-sheets-api.json', sheet_name='Hasil Scraping'):
    """Menyimpan DataFrame ke Google Sheets."""
    try:
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
        client = gspread.authorize(creds)
        
        try:
            sheet = client.open(sheet_name)
        except gspread.SpreadsheetNotFound:
            sheet = client.create(sheet_name)
        
        worksheet = sheet.get_worksheet(0) or sheet.add_worksheet('Sheet1', rows=1000, cols=10)
        
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
        sheet.share('', perm_type='anyone', role='writer')
        logging.info(f"Successfully saved to Google Sheets: {sheet.url}")
    except Exception as e:
        logging.error(f"Error saving to Google Sheets: {e}")

def save_to_postgres(df, db_params):
    """Menyimpan DataFrame ke PostgreSQL."""
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS products (
            Title VARCHAR,
            Price FLOAT,
            Rating FLOAT,
            Colors INTEGER,
            Size VARCHAR,
            Gender VARCHAR,
            timestamp VARCHAR
        );
        """
        cursor.execute(create_table_query)
        
        for _, row in df.iterrows():
            insert_query = sql.SQL("""
            INSERT INTO products (Title, Price, Rating, Colors, Size, Gender, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """)
            cursor.execute(insert_query, tuple(row))
        
        conn.commit()
        logging.info("Successfully saved to PostgreSQL")
    except Exception as e:
        logging.error(f"Error saving to PostgreSQL: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()