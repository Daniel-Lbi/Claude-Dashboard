import schedule
import time
from etl.etl_pipeline import run_etl

def job():
    """Scheduled job to run ETL pipeline"""
    api_url = "https://jsonplaceholder.typicode.com/posts"  # Replace with your API
    run_etl(api_url)

# Schedule the job to run every hour
schedule.every(1).hours.do(job)

if __name__ == "__main__":
    print("Scheduler started. ETL will run every hour.")
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute