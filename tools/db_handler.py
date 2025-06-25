import sqlite3
import pandas as pd

def get_data_from_db(db_path, table_name):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(f'SELECT * FROM `{table_name}`;', conn)
    conn.close()
    return df
