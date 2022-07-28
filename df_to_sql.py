import pandas as pd
import sqlite3

con = sqlite3.connect('nodes.db')
df = pd.read_sql("SELECT * FROM nodesdf", con)
df.to_csv("notre_brazil.csv", index=False, encoding="utf-8")
