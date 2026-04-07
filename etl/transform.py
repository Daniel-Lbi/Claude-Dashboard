import pandas as pd
import json

def transform_data(raw_data):
    """
    Transform raw API data into a clean pandas DataFrame.
    
    Args:
        raw_data (dict or list): Raw data from the API
    
    Returns:
        pd.DataFrame: Cleaned and transformed data
    """
    try:
        # Convert to DataFrame
        df = pd.DataFrame(raw_data)
        
        # Basic cleaning
        df = df.dropna()  # Remove rows with missing values
        df = df.drop_duplicates()  # Remove duplicate rows
        
        # Add timestamp for when data was processed
        df['processed_at'] = pd.Timestamp.now()
        
        # Example transformations (customize based on your data)
        # df['column_name'] = df['column_name'].str.lower()  # Convert to lowercase
        # df['date_column'] = pd.to_datetime(df['date_column'])  # Convert to datetime
        
        return df
    except Exception as e:
        print(f"Error transforming data: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Load raw data
    with open('../data/raw_data.json', 'r') as f:
        raw_data = json.load(f)
    
    transformed_df = transform_data(raw_data)
    if transformed_df is not None:
        print(f"Transformed data shape: {transformed_df.shape}")
        print(transformed_df.head())
        
        # Save transformed data
        transformed_df.to_csv('../data/transformed_data.csv', index=False)