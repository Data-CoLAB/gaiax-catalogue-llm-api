import os
import psycopg2
from dotenv import load_dotenv

class PostGresDB:
    def __init__(self):
        load_dotenv(override=True)
        self.db_params = {
            'dbname': os.getenv('DB_NAME'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'host': os.getenv('DB_HOST'),
            'port': os.getenv('DB_PORT')
        }
        self.conn = None
        self.cur = None
        
    def connect(self):
        try:
            self.conn = psycopg2.connect(**self.db_params)
            print("Connected to the database")
        except Exception as e:
            print(f"An error occurred during connection: {e}")
    
    def get_resource_data(self):
        query = "SELECT * from public.data_category_metadata"
        try:
            self.cur = self.conn.cursor()
            self.cur.execute(query)
            data = self.cur.fetchall()
            return data
        except Exception as e:
            print(f"An error occurred while fetching data: {e}")
            return None
        
    def close(self):
        if self.cur:
            try:
                self.cur.close()
                print("Cursor closed")
            except Exception as e:
                print(f"An error occurred while closing the cursor: {e}")
        if self.conn:
            try:
                self.conn.close()
                print("Connection closed")
            except Exception as e:
                print(f"An error occurred while closing the connection: {e}")