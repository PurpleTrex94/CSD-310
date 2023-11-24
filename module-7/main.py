import mysql.connector
from mysql.connector import Error, errorcode

# Specify MySQL connection details
config = {
    "user": "root",
    "password": "Friezavegeta9@",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    # Establish MySQL connection
    db = mysql.connector.connect(**config)
    print(f"\nDatabase user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}")

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Query 1: Displaying Studio Records
    query1 = "SELECT DISTINCT studio_id AS 'Studio ID:', studio_name AS 'Studio Name:' FROM studio;"
    cursor.execute(query1)
    result1 = cursor.fetchall()
    print("\n--DISPLAYING Studio Records--")
    for row in result1:
        print(f"Studio ID: {row[0]}\nStudio Name: {row[1]}")

    # Query 2: Displaying Genre Records
    query2 = "SELECT DISTINCT genre_id AS 'Genre ID:', genre_name AS 'Genre Name:' FROM genre;"
    cursor.execute(query2)
    result2 = cursor.fetchall()
    print("\n--DISPLAYING Genre Records--")
    for row in result2:
        print(f"Genre ID: {row[0]}\nGenre Name: {row[1]}")

    # Query 3: Displaying Short Film Records
    query3 = "SELECT DISTINCT film_name AS 'Film Name:', film_runtime AS 'Runtime:' FROM film WHERE film_runtime < 120;"
    cursor.execute(query3)
    result3 = cursor.fetchall()
    print("\n--DISPLAYING Short Film Records--")
    for row in result3:
        print(f"Film Name: {row[0]}\nRuntime: {row[1]}")

    # Query 4: Displaying Director Records in Order
    query4 = "SELECT DISTINCT film_name AS 'Film Name:', film_director AS 'Director:' FROM film ORDER BY film_director;"
    cursor.execute(query4)
    result4 = cursor.fetchall()
    print("\n--DISPLAYING Director Records in Order--")
    for row in result4:
        print(f"Film Name: {row[0]}\nDirector: {row[1]}")






except mysql.connector.Error as err:
    # Handle MySQL connection errors
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("* The supplied username or password is invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("* The specified database does not exist.")
    else:
        print(err)

finally:
    # Close the cursor and database connection if open
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'db' in locals() and db.is_connected():
        db.close()
        print("\nDatabase connection closed.")
