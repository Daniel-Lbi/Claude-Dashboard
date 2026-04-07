import sqlite3
import pandas as pd

def load_data(df, db_path='../data/dashboard_data.db', table_name='api_data'):
    """
    Load transformed data into SQLite database.
    
    Args:
        df (pd.DataFrame): Transformed data
        db_path (str): Path to SQLite database
        table_name (str): Name of the table to create/update
    """
    try:
        # Connect to SQLite database
        conn = sqlite3.connect(db_path)
        
        # Load data into database (replace table if it exists)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        
        print(f"Data loaded successfully into {table_name} table")
        
        # Close connection
        conn.close()
    except Exception as e:
        print(f"Error loading data: {e}")

def get_data(db_path='../data/dashboard_data.db', table_name='api_data'):
    """
    Retrieve data from SQLite database.
    
    Args:
        db_path (str): Path to SQLite database
        table_name (str): Name of the table to query
    
    Returns:
        pd.DataFrame: Data from the database
    """
    try:
        conn = sqlite3.connect(db_path)
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        conn.close()
        return df
    except Exception as e:
        print(f"Error retrieving data: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Load transformed data
    df = pd.read_csv('../data/transformed_data.csv')
    load_data(df)
    
    # Test retrieval
    retrieved_df = get_data()
    if retrieved_df is not None:
        print(f"Retrieved data shape: {retrieved_df.shape}")