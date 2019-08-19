opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    # Complete the code from here
    price = float(row[4])
      
    if price == 0.0:
        free_apps_ratings.append (rating)
        avg_rating_free = sum(free_apps_ratings) / len(free_apps_ratings)

a_price = 0
if a_price == 0:
    print('This is free')
elif a_price == 1:
    print('This is not free')

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

non_free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])   
    if price != 0.0:
        non_free_apps_ratings.append(rating)
    
avg_rating_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)

#
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
non_games_ratings = []
for app_data in apps_data[1:]:
    rating = app_data[7]
    genre = app_data[11]
    if genre != 'Games':
        non_games_ratings.append(rating)
avg_rating_non_games = sum(non_games_ratings) / len(non_games_ratings)

#
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
non_games_ratings = []
for app_data in apps_data[1:]:
    rating = float(app_data[7])
    genre = app_data[11]
    if genre != 'Games':
        non_games_ratings.append(rating)
avg_rating_non_games = sum(non_games_ratings) / len(non_games_ratings)