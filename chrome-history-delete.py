#!/usr/bin/env python3
import sqlite3
import re

def delete_history(db_location, website):
    result = True
    id = 0
    while result:
        result = False
        connection = sqlite3.connect(db_location, timeout=1)
        cursor = connection.cursor()
        try:
            ids = []
            for row in cursor.execute("""SELECT id, url FROM urls WHERE url LIKE '%{}%'""".format(website)):
                print (row)
                id = row[0]
                ids.append((id,))
            cursor.executemany('DELETE FROM urls WHERE id=?', ids)
            connection.commit()
        except sqlite3.OperationalError:
            print("Database locked, please close Google Chrome")
    connection.close()
    return 1
