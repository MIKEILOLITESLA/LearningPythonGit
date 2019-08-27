#引入 csv 库的 reader() 函数
from csv import reader

#引入 explore_data() function
def explore_data(dataset, start, end, rows_and_columns = False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice: #打印列表全部内容
        print(row)
        print('\n') # 行间空
        
    if rows_and_columns:
        print('Number of rows:',len(dataset)) # 行数
        print('Number of columns',len(dataset[0])) # 列数

# _*_ coding:utf-8 _*_
#Apple dataset
open_fileA = open('AppleStore.csv',encoding='UTF-8')
read_fileA = reader(open_fileA)
ios = list(read_fileA)
ios_T_head = ios[0]
ios = ios[1:] #去掉首行的每列名称

#Google dataset
open_fileG = open('googleplaystore.csv',encoding='UTF-8')
read_fileG = reader(open_fileG)
android = list(read_fileG)
android_T_head = android[0]
android = android[1:] #去掉各自表格首行的每列名称

#有一行数据报错，确认错误
print(android[10472])
print('\n')
print(android[10473])
print('\n')
print(android_T_head)

#在删除掉错误数据前后确认一下表格行数变化
print(len(android))
del android[10472]  #删掉这组有问题的数据
print(len(android))

#除去重复的数据组
#除去 Android 的重复数据组
duplicate_apps = []
unique_apps = []

for app in android:
    name = app[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)
        

dup_num = len(duplicate_apps)

print('\n')        
print('number of duplicated apps:',dup_num )
print('\n')
print('Expected length:', (len(android) - dup_num))
print('\n')

#用新建 dictionary 除去重复数据组

reviews_max = {}

for app in android:
    name = app[0]
    n_reviews = float(app[3])
    
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
        
    elif name not in reviews_max:
        reviews_max[name] = n_reviews

        
#检查一下 reviews_max 中元素数量是不是对
print('Expected length:', len(android) - 1181)
print('\n')
print('Actual number:',len(reviews_max))

#开始清除重复应用数据
android_clean = []
already_added = []

for app in android:
    name = app[0]
    n_reviews = float(app[3])#这里利用了数据组的第四列 id 的独一无二来区分相同 name 的重复数据组
    
    if (reviews_max[name] == n_reviews) and (name not in already_added):
        android_clean.append(app)
        already_added.append(name)

explore_data(android_clean, 0, 2, True) #检验元素数量是否正确

#除去非英语 app 的数据
def is_english(string):
    non_ascii = 0
    
    for character in string:
        if ord(character) > 127: #利用英语字母的 ASCII 编码小于127
            non_ascii += 1
    
    if non_ascii > 3:
        return False
    else:
        return True

#选出英语应用
android_english = []
ios_english = []

for app in android_clean:
    name = app[0]
    if is_english(name):
        android_english.append(app)
        
for app in ios:
    name = app[2]#出过一个乌龙，注意序列号
    if is_english(name):
        ios_english.append(app)

print('android English Apps samples and total number:')
print('\n')
explore_data(android_english, 0, 2, True)
print('\n')
print('ios English Apps samples and total number:')
print('\n')
explore_data(ios_english, 0, 2, True)

#选出免费应用
android_final = []
ios_final = []

for app in android_english:
    price = app[7]
    if price == '0':
        android_final.append(app)
        
for app in ios_english:
    price = app[5]
    if price == '0':
        ios_final.append(app)
        
print('Number of android free English Apps:',len(android_final))
print('Number of ios free English Apps:',len(ios_final)) 
print('\n')

#clean data end______________

# data analysis of genre 
def freq_table(dataset, index):
    table = {}
    total = 0
    
    for row in dataset:
        total += 1
        value = row[index]
        if value in table:
            table[value] += 1
        else:
            table[value] = 1
    
    table_percentages = {}

    for genre in table:
        percentage = (table[genre] / total) * 100
        table_percentages[genre] = percentage 
    
    return table_percentages


def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)
        
    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])

#Content Rating
print('Content Rating:')
display_table(ios_final, -5)
print('\n')

#category
print('Category:')
display_table(android_final, 1)
print('\n')

#Genres
print('Genres:')
display_table(android_final, -4)
print('\n')

#average number of installs for each ios app genre 
genres_ios = freq_table(ios_final, -5)

for genre in genres_ios:
    total = 0
    len_genre = 0
    for app in ios_final:
        genre_app = app[-5]
        if genre_app == genre:            
            n_ratings = float(app[6])
            total += n_ratings
            len_genre += 1
    avg_n_ratings = total / len_genre
    print(genre, ':', avg_n_ratings)
print('\n')

#user rating
for app in ios_final:
    if app[-5] == 'Navigation':
        print(app[2], ':', app[6]) # print name and number of ratings
print('\n')

#Reference
for app in ios_final:
    if app[-5] == 'Reference':
        print(app[2], ':', app[6])
print('\n')

#Most Popular Apps by Genre on Google Play
display_table(android_final, 5) # the Installs columns
print('\n')

# name + procentage
categories_android = freq_table(android_final, 1)

for category in categories_android:
    total = 0
    len_category = 0
    for app in android_final:
        category_app = app[1]
        if category_app == category:            
            n_installs = app[5]
            n_installs = n_installs.replace(',', '')
            n_installs = n_installs.replace('+', '')
            total += float(n_installs)
            len_category += 1
    avg_n_installs = total / len_category
    print(category, ':', avg_n_installs)
print('\n')

# 
for app in android_final:
    if app[1] == 'COMMUNICATION' and (app[5] == '1,000,000,000+'
                                      or app[5] == '500,000,000+'
                                      or app[5] == '100,000,000+'):
        print(app[0], ':', app[5])
print('\n')

# If we removed all the communication apps 
# that have over 100 million installs, 
# the average would be reduced roughly ten times:

under_100_m = []

for app in android_final:
    n_installs = app[5]
    n_installs = n_installs.replace(',', '')
    n_installs = n_installs.replace('+', '')
    if (app[1] == 'COMMUNICATION') and (float(n_installs) < 100000000):
        under_100_m.append(float(n_installs))
        
print(sum(under_100_m) / len(under_100_m))
print('\n')

#
for app in android_final:
    if app[1] == 'BOOKS_AND_REFERENCE':
        print(app[0], ':', app[5])
print('\n')

#
for app in android_final:
    if app[1] == 'BOOKS_AND_REFERENCE' and (app[5] == '1,000,000,000+'
                                            or app[5] == '500,000,000+'
                                            or app[5] == '100,000,000+'):
        print(app[0], ':', app[5])
print('\n')

#
for app in android_final:
    if app[1] == 'BOOKS_AND_REFERENCE' and (app[5] == '1,000,000+'
                                            or app[5] == '5,000,000+'
                                            or app[5] == '10,000,000+'
                                            or app[5] == '50,000,000+'):
        print(app[0], ':', app[5])

if __name__ == '__main__':
  fire.Fire()