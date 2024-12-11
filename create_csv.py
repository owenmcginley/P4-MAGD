import pandas as pd
import numpy as np
import datetime as dt

# Preparamos los dataframes

cities = ['malaga', 'mallorca', 'menorca']
dir_data = "../airbnb/"
calendar = pd.DataFrame()
reviews_gz = pd.DataFrame()
listings_gz = pd.DataFrame()

# Vamos encadenando los csv de las distintas ciudades, añadiendo la columna city y su numero correspondiente
# (barcelona = 1, madrid = 2, malaga = 3, mallorca = 4, menorca = 5, sevilla = 6, valencia = 7)

for city in cities:
    temp_calendar = pd.read_csv(f'{dir_data}{city}/calendar.csv', parse_dates=['date'], low_memory=False)
    temp_calendar['city'] = cities.index(city) + 3
    calendar = pd.concat([temp_calendar, calendar])

    temp_reviews_gz = pd.read_csv(f'{dir_data}{city}/reviews_gz.csv')
    temp_reviews_gz['city'] = cities.index(city) + 3
    reviews_gz = pd.concat([temp_reviews_gz, reviews_gz])

    temp_listings_gz = pd.read_csv(f'{dir_data}{city}/listings_gz.csv')
    temp_listings_gz['city'] = cities.index(city) + 3
    listings_gz = pd.concat([temp_listings_gz, listings_gz])


# Guardamos los dataframes creados en archivos csv

calendar.to_csv('./csv/calendar.csv', index=False)
reviews_gz.to_csv('./csv/reviews_gz.csv', index=False)
listings_gz.to_csv('./csv/listings_gz.csv', index=False)

print("Program completed")