# File of functions for interaction with clients in the CRUD brought from the database.
from Connection import *

class CClients:

    #Function to display the clients that have the database.
    def showClients():
        try:
            connect = CConnection.ConnectionDataBase()
            cursor = connect.cursor()
            cursor.execute("select * from users;")
            result = cursor.fetchall()
            connect.commit()
            connect.close()
            return result

        except mysql.connector.Error as error:
            print("Error to show data, error: {}".format(error))

    # Function to add new customers to the database from the CRUD.
    def enterClients(firstname,lastname,gender): # In the props you pass the attributes you want to add to the database.
        try:

            connect = CConnection.ConnectionDataBase()
            cursor = connect.cursor()
            sql = "insert into users values(null, %s, %s, %s);"
            values = (firstname,lastname,gender)
            cursor.execute(sql,values)
            connect.commit()
            print(cursor.rowcount,"Registered")
            connect.close()

        except mysql.connector.Error as error:
            print("Error to enter data, error: {}".format(error))

    # Function to update database clients from the CRUD.
    def updateClients(idUser,firstname,lastname,gender):  # In the props, the attributes to be updated from the database are passed to it
        try:

            connect = CConnection.ConnectionDataBase()
            cursor = connect.cursor()
            sql = "UPDATE users SET users.firtsname = %s,users.lastname =  %s,users.gender =  %s Where users.id =  %s;"
            values = (firstname,lastname,gender,idUser)
            cursor.execute(sql,values)
            connect.commit()
            print(cursor.rowcount,"Update")
            connect.close()

        except mysql.connector.Error as error:
            print("Error to update user, error: {}".format(error))

    # Function to remove customers from the database from the CRUD.
    def deleteClients(idUser): #In this prop you pass the ID of the customer you want to remove from the database.
        try:

            connect = CConnection.ConnectionDataBase()
            cursor = connect.cursor()
            sql = "DELETE from users WHERE users.id=%s;"
            values = (idUser,)
            cursor.execute(sql,values)
            connect.commit()
            print(cursor.rowcount,"Deleted")
            connect.close()

        except mysql.connector.Error as error:
            print("Error to delete user, error: {}".format(error))