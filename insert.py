from config import load_config
import psycopg2
import pandas as pd
import os
import json


def insert_data(data):
    sql = "INSERT INTO products(id,name,url_key,price,description,images_url) VALUES(%s,%s,%s,%s,%s,%s) RETURNING *"
    try:
        config = load_config()
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.executemany(sql, [(row["id"], row["name"], row["url_key"], row["price"], row["description"], row["images_url"]) for row in data])
                print(f"Inserted {len(data)} rows successfully!")
    except (psycopg2.DatabaseError, Exception) as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    data_dir = "/home/hofonam/Documents/UniGap/Project02/data"
    for i in range(1, 201):
        file_path = os.path.join(data_dir, f"products_{i}.json")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            insert_data(data)
        else:
            print(f"File {file_path} does not exist.")
