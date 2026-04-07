# ETL Pipeline for API Data Extraction, Transformation, and Loading

## Overview
This repository implements an ETL pipeline that extracts data from a free API, transforms it using Python and pandas, and loads it into a SQLite database. The data is then visualized using a Dash (Plotly) web application.

## Architecture

### ETL Module (`etl/`)
- `extract.py`: Handles data extraction from the API using the `requests` library.
- `transform.py`: Processes and cleans the raw data using pandas.
- `load.py`: Loads the transformed data into a SQLite database.
- `etl_pipeline.py`: Orchestrates the entire ETL process.

### Data Storage (`data/`)
- SQLite database (`dashboard_data.db`) for storing processed data.

### Visualization (`viz/`)
- `app.py`: Dash application that reads data from the database and creates interactive visualizations using Plotly.

### Scheduling
- `scheduler.py`: (Optional) Runs the ETL pipeline at scheduled intervals using the `schedule` library.

## Getting Started

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the ETL pipeline:
   ```
   python etl/etl_pipeline.py
   ```

3. Start the dashboard:
   ```
   python viz/app.py
   ```

4. Open your browser to `http://127.0.0.1:8050/` to view the dashboard.

## Choosing a Free API
Select a free API that provides interesting data for visualization. Examples:
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/): Fake data for testing
- [OpenWeatherMap](https://openweathermap.org/api): Weather data (requires free API key)
- [REST Countries](https://restcountries.com/): Country information
- [CoinGecko](https://www.coingecko.com/en/api): Cryptocurrency data

Update the API endpoint and parameters in `etl/extract.py` accordingly.

## Best Practices
- Use environment variables for API keys
- Implement error handling and logging
- Add data validation in the transform step
- Consider using a more robust database (e.g., PostgreSQL) for production
- Implement caching to avoid unnecessary API calls