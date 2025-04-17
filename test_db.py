# test_db.py
import mysql.connector
from config import DB_CONFIG

try:
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM returns_table.returns_table LIMIT 1")
    row = cursor.fetchone()

    if row:
        print("✅ Success! Sample row:")
        print(row)
    else:
        print("⚠️ Connected, but no data found in 'returns' table.")

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")
