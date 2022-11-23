# Importing Sqlite3 Module
import sqlite3
import pandas as pd

con = sqlite3.connect('Task.db')

df = pd.read_sql_query("SELECT * from Items", con)

for index, row in df.iterrows():
    if "table" in row['items_name']:
        row['items_name'] = row['items_name'].replace("table", "desk")

df.to_sql('Task.db', con, schema=None, if_exists='replace', index=True,
          index_label=None, chunksize=None, dtype=None, method=None)

con.close()
