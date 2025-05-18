import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)

def scrape_page(page_num):
    """Scrape data from a single page."""
    try:
        url = f"https://fashion-studio.dicoding.dev/?page={page_num}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        products = []
        timestamp = datetime.now().isoformat()
        product_items = soup.find_all('div', class_='product-details')
        
        if not product_items:
            logging.warning(f"No product items found on page {page_num}. HTML may have changed.")
            return []

        for item in product_items:
            # Ambil Title
            title = item.find('h3', class_='product-title')
            
            # Ambil Price
            price_container = item.find('div', class_='price-container')
            price = price_container.find('span', class_='price') if price_container else None
            
            # Ambil Rating, Colors, Size, Gender dari elemen <p> dengan gaya tertentu
            p_elements = item.find_all('p', style='font-size: 14px; color: #777;')
            rating = None
            colors = None
            size = None
            gender = None
            
            for p in p_elements:
                text = p.text.strip()
                if text.startswith('Rating:'):
                    rating = text.replace('Rating: ⭐ ', '').replace(' / 5', '')
                elif 'Colors' in text:
                    colors = text
                elif text.startswith('Size:'):
                    size = text
                elif text.startswith('Gender:'):
                    gender = text

            product = {
                'Title': title.text.strip() if title else 'Unknown Product',
                'Price': price.text.strip() if price else '$0',
                'Rating': rating if rating else 'Invalid Rating',
                'Colors': colors if colors else '0 Colors',
                'Size': size if size else 'Size: Unknown',
                'Gender': gender if gender else 'Gender: Unknown',
                'timestamp': timestamp
            }
            products.append(product)
        
        logging.info(f"Scraped {len(products)} products from page {page_num}")
        return products

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from page {page_num}: {e}")
        return []

def scrape_main():
    """Scrape data from multiple pages."""
    try:
        all_products = []
        for page in range(1, 51):
            products = scrape_page(page)
            all_products.extend(products)
        df = pd.DataFrame(all_products)
        logging.info(f"Total products scraped: {len(df)}")
        return df
    except Exception as e:
        logging.error(f"Error in scrape_main: {e}")
        return pd.DataFrame()