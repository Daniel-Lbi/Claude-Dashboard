from extract import extract_data
from transform import transform_data
from load import load_data

def run_etl(api_url, params=None):
    """
    Run the complete ETL pipeline.
    
    Args:
        api_url (str): The API endpoint URL
        params (dict): Optional query parameters
    """
    print("Starting ETL pipeline...")
    
    # Extract
    print("Extracting data...")
    raw_data = extract_data(api_url, params)
    if raw_data is None:
        print("ETL failed at extraction stage")
        return
    
    # Transform
    print("Transforming data...")
    transformed_df = transform_data(raw_data)
    if transformed_df is None:
        print("ETL failed at transformation stage")
        return
    
    # Load
    print("Loading data...")
    load_data(transformed_df)
    
    print("ETL pipeline completed successfully!")

if __name__ == "__main__":
    # Example ETL run
    api_url = "https://jsonplaceholder.typicode.com/posts"
    run_etl(api_url)