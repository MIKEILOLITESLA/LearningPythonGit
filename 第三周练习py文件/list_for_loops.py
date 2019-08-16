#list for loop

#list
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

#list
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
ratings_1 = (row_1[3])
ratings_2 = (row_2[3])
ratings_3 = (row_3[3])
total = ratings_1 + ratings_2 + ratings_3
average = total / 3

#list
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
rating_1 = row_1[-1]
rating_2 = row_2[-1]
rating_3 = row_3[-1]
total_rating = rating_1 + rating_2 + rating_3 
average_rating = total_rating / 3

#list
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
fb_rating_data = [row_1[0],row_1[3],row_1[4]]
insta_rating_data = [ row_2[0],row_2[3],row_2[4]]
pandora_rating_data = [ row_5[0],row_5[3],row_5[4]]
avg_rating = (fb_rating_data[2] + insta_rating_data[2] + pandora_rating_data[2])/3

#list
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
first_4_fb = row_1 [0:4]
last_3_fb = row_1 [-3:]
pandora_3_4 = row_5 [2:4]#后面的那个数是不读的

#list
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
app_data_set = [row_1 , row_2 , row_3 , row_4 , row_5]
avg_rating = (app_data_set [0][4] + app_data_set[1][4] + app_data_set[2][4] + app_data_set[3][4] + app_data_set[4][4])/5

#len
from csv import reader
opened_file = open('AppleStore.csv')
opened_file
read_file = reader(opened_file)
apps_data = list(read_file)
len(apps_data)
#loops
app_data_set = [row_1, row_2, row_3, row_4, row_5]
for each_list in app_data_set:
    print (each_list)

#loops
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]
app_data_set = [row_1, row_2, row_3, row_4, row_5]
rating_sum = 0
for each_row in app_data_set:#这个each_row为什么能代表每行
    rating_sum = rating_sum + each_row[4]
avg_rating = rating_sum / 5
print(avg_rating)

#loops
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
rating_sum = 0
for each_row in apps_data[1:]:
    rating = float (each_row[7])
    rating_sum = rating_sum + rating
avg_rating = rating_sum /(len(apps_data))
print (avg_rating)#这个和标准答案有一点小误差，不知道怎么搞的，等过去了回来看看

#上式修改版：
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
rating_sum = 0
for each_row in apps_data[1:]:
    rating = float (each_row[7])
    rating_sum = rating_sum + rating
avg_rating = rating_sum /(len(apps_data)-1）
#这里是从第二个开始取，所以个数减一
print (avg_rating)

#loops
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
all_ratings = []
for each_row in apps_data[1:]:
    rating = float(each_row[7])
    all_ratings.append(rating)
avg_rating = sum(all_ratings) / (len(all_ratings))

#这里对我来说最不好过的大概是那个for A in range（）中的 A，写这段的时候试了好几次，最后照着提示又做了一遍才知道可以随意命名，
# 这个A代表的是range（）里的任意元素吧。做py100days 的时候这块就有点迷。