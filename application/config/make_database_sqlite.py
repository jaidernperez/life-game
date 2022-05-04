import sqlite3
import os

DB_PATH = '../../stat.sqlite'

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.execute('CREATE TABLE transitions (dead_to_life INTEGER, dead_to_dead INTEGER, life_to_dead INTEGER, life_to_life INTEGER)')
c.execute("INSERT INTO transitions (dead_to_life, dead_to_dead, life_to_dead, life_to_life) VALUES (0, 0, 0, 0)")

conn.commit()
conn.close()
