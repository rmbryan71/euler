import psycopg2


try:
    connection = psycopg2.connect(user="myuser",
                                            password="mypass",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="postgres_db")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")
    # Print PostgreSQL version
    #cursor.execute("SELECT version();")
    #record = cursor.fetchone()
    #print("You are connected to - ", record, "\n")

    postgres_insert_query = """ INSERT INTO p668 (id) VALUES (%s);"""
    cursor.executemany(postgres_insert_query, [x for x in range(915539, 1000000000)])
    connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")