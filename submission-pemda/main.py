import logging
from utils.extract import scrape_main
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_google_sheets, save_to_postgres

logging.basicConfig(level=logging.INFO)

def main():
    logging.info("Starting ETL pipeline...")
    
    # Ekstraksi
    logging.info("Extracting data...")
    raw_data = scrape_main()
    if raw_data.empty:
        logging.error("No data extracted. Aborting pipeline.")
        return
    
    # Transformasi
    logging.info("Transforming data...")
    cleaned_data = transform_data(raw_data)
    if cleaned_data.empty:
        logging.error("No data after transformation. Aborting pipeline.")
        return
    
    # Menyimpan
    logging.info("Saving data...")
    save_to_csv(cleaned_data, filename='products.csv')
    save_to_google_sheets(cleaned_data)
    
    db_params = {
        'dbname': 'etl_submission',
        'user': 'postgres',
        'password': 'pass',  # ganti dengan pass anda
        'host': 'localhost',
        'port': '5432'
    }
    save_to_postgres(cleaned_data, db_params)
    
    logging.info("ETL pipeline completed.")

if __name__ == "__main__":
    main()
