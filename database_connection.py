# Importing MySQL connector and error
import mysql.connector
from mysql.connector import Error

# Function to create a connection to the database
def connect_database():
    # Database Connection Parameters:
    db_name = "library_management_db"  
    user = "root"              
    password = "33Rafi77!"     
    host = "localhost"         

    try: # Establishing the database connection
        conn = mysql.connector.connect(
	        database=db_name,
	        user=user,
	        password=password,
	        host=host
        )

        # Verifying the connection 
        print("Connected to MySQL database successfully.")
        return conn

    except Error as e: # Error handling
        print(f"Database Connection Error: {e}")