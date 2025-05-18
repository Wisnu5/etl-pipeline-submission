# ETL Pipeline Submission
This project is an ETL (Extract, Transform, Load) pipeline developed for the Dicoding submission. It extracts product data from `fashion-studio.dicoding.dev`, transforms the data to meet specific requirements, and loads it into a CSV file, Google Sheets, and a PostgreSQL database.

## Project Structure
submission-pemda
├── tests
│   ├── init.py
│   ├── test_extract.py
│   ├── test_load.py
│   ├── test_transform.py
├── utils
│   ├── init.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
├── main.py
├── requirements.txt
├── submission.txt
├── products.csv
├── google-sheets-api.json

- **`main.py`**: Main script to run the ETL pipeline.
- **`utils/`**: Contains modules for extraction (`extract.py`), transformation (`transform.py`), and loading (`load.py`).
- **`tests/`**: Contains unit tests for each module.
- **`requirements.txt`**: Lists Python dependencies.
- **`submission.txt`**: Instructions for running the pipeline and tests.
- **`products.csv`**: Output CSV file containing transformed data.
- **`google-sheets-api.json`**: Google Cloud credentials (excluded from GitHub via `.gitignore`).
- **`.gitignore`**: Excludes sensitive and temporary files.

## Prerequisites

1. **Python 3.11**: Ensure Python 3.11 is installed.
2. **Git**: Installed for version control.
3. **PostgreSQL**: Set up a database named `etl_submission` with user `postgres`.
4. **Google Cloud Credentials**: Obtain `google-sheets-api.json` from Google Cloud Console with Google Sheets and Drive API enabled.

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/etl-pipeline-submission.git
   cd submission-pemda
2. **Create and Activate Virtual Environment**:
   ```bash
   python -m venv venv
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Configure PostgreSQL*:
   ```bash
   psql -U postgres
   ```sql
   CREATE DATABASE your_database;

## Running the ETL Pipeline
1. **Run the Pipeline**:
    ```bash
    python main.py
2. **Running Unit Tests**:
   ```bash
    python -m pytest tests
3. **Run Test Coverage:**:
   ```bash
    coverage run -m pytest tests



   
