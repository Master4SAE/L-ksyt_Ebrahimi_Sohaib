#8.1

import mysql.connector

# Connect to database
connection = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="flight_game",
)


# function gets town from database
def get_countries_from_database(country_code):
    sql = "select municipality, name from airport where ident='" + country_code + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    return results[0]


country_code = input("Hey enter ICAO code of an airport.\n>")
the_data = get_countries_from_database(country_code)
town, airport = the_data

print(f"The airport name is {airport} and your location is {town}")

#8.2

