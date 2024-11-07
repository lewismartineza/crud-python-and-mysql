# MySQL database connection file and function.

import mysql.connector

class CConnection:

    def ConnectionDataBase():

        try:
            connection = mysql.connector.connect(
                                                # Here is the user of the database.
                                                user='**********',

                                                # Here is the password to the database.
                                                password="**********",

                                                # Here goes the database host.
                                                host="**********",

                                                # Here is the database name.
                                                database="**********",

                                                # Here is the port of the database.
                                                port="**********"
                                                )
            # Console printout that the database connection was successful.
            print('Connected to DATABASENAME')

            return connection
        # Console printout of database connection failure.
        except mysql.connector.Error as error:
            print("Error to connected, error: {}".format(error))


            return connection
    ConnectionDataBase()
