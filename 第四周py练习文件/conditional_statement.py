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
        free_apps_ratings.append(rating)
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

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]

free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    if price == 0.0 and genre == 'Games':
        free_games_ratings.append(rating)
     avg_rating_free_games = sum(free_games_ratings) / len(free_games_ratings)

#
ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    
    if price > 9:
        ratings.append(rating)
        
avg_rating = sum(ratings) / len(ratings)
n_apps_more_9 = len(ratings)
n_apps_less_9 = len(apps_data[1:]) - len(ratings)

#
for app in apps_data[1:]:
    price = float(app[4])

for app in apps_data[1:]:
    price = float(app[4])   
    if price == 0.0:
        app.append('free')
    else:
        app.append('non-free')

apps_data[0].append('free_or_not')
print(apps_data[:6])

#
for app in apps_data[1:]:
    price = float(app[4])
    if price == 0:
        app.append('free')
    elif price > 0 and price < 20:
        app.append('affordable')
    elif price >= 20 and price < 50:
        app.append('expensive')
    elif price >=50 :
        app.append('very expensive')
apps_data[0].append('price_label')
print(apps_data[6:])