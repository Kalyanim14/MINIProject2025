import mysql.connector

def initialize_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sharvan8"
        )
        cursor = conn.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS image_encryption")
        cursor.execute("USE image_encryption")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS image_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                image_id VARCHAR(255) NOT NULL,
                image_name VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Database and table initialized successfully.")
    except Exception as e:
        print(f"❌ Failed to initialize database: {e}")
