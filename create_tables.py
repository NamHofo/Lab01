from config import load_config
import psycopg2

def create_table():
    command="""
    CREATE TABLE products (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        url_key TEXT NOT NULL UNIQUE,
        price INT NOT NULL,
        description TEXT NOT NULL,
        images_url TEXT NOT NULL
    );"""

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as e:
        print(f"Error: {e}")


        
if __name__ == '__main__':
    create_table()