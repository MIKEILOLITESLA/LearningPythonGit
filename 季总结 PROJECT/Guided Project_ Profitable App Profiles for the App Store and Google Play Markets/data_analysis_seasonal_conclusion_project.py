#
file_handle = open('result.txt',mode='w')

#
from csv import reader


#
def explore_data(dataset, start, end, rows_and_columns = False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice: #打印列表全部内容
        print(row)
        print('\n') # 行间空
        DS = str(row)
        file_handle.write(DS)
        file_handle.write('\n')
        
    if rows_and_columns:
        print('Number of rows:',len(dataset)) # 行数
        Row = ['Number of rows:',str(len(dataset))] 
        file_handle.writelines(Row)
        print('Number of columns:',len(dataset[0])) # 列数       
        Col = ['Number of columns:',str(len(dataset[0]))]
        file_handle.writelines(Col)
        

#UTF-8 编码以防万一
#_*_ coding:utf-8 _*_
 
# 读取 Applestore dataset
open_fileA = open('AppleStore.csv',encoding='UTF-8')
read_fileA = reader(open_fileA)
ios = list(read_fileA)
ios_T_head = ios[0]
ios = ios[1:] #去掉首行的每列名称

#读取 Googleplay dataset
open_fileG = open('googleplaystore.csv',encoding='UTF-8')
read_fileG = reader(open_fileG)
android = list(read_fileG)
android_T_head = android[0]
android = android[1:] #去掉各自表格首行的每列名称

print('##导入数据完成##')
print('\n')

print('##开始对数据的清理##')
file_handle.write('##开始对数据的清理##')
file_handle.write('\n')
file_handle.write('\n')

#得知 Googleplay dataset 中有一行数据是错误的，确认错误位置
print('【确认 android 中的错误数据行位置】')
file_handle.write('【确认 android 中的错误数据行位置】')
file_handle.write('\n')
print(android[10472])
print('\n')
A2 = [str(android[10472])]
file_handle.writelines(A2)
file_handle.write('\n')
file_handle.write('\n')
print(android[10473])
print('\n')
A3 = [str(android[10473])]
file_handle.writelines(A3)
file_handle.write('\n')
file_handle.write('\n')
print(android_T_head)
ATH = [str(android_T_head)]
file_handle.writelines(ATH)
file_handle.write('\n')
file_handle.write('\n')

#在删除掉错误数据前后确认一下表格行数变化
print('【在删除掉错误数据前后确认一下表格行数变化】')
file_handle.write('【在删除掉错误数据前后确认一下表格行数变化】')
file_handle.write('\n')
print(len(android))
LA = str(len(android))
file_handle.write(LA)
file_handle.write('\n')
file_handle.write('\n')
del android[10472]  #删掉这组有问题的数据
print(len(android))
print('\n')
LA = str(len(android))
file_handle.write(LA)
file_handle.write('\n')
file_handle.write('\n')

#除去 android 的重复数据组
print('【检查并清除 android 的重复数据组】')
file_handle.write('【检查并清除 android 的重复数据组】')
file_handle.write('\n')
file_handle.write('\n')
duplicate_apps = []
unique_apps = []

for app in android:
    name = app[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)
        

dup_num = len(duplicate_apps)

print('number of duplicated apps:',dup_num )
print('\n')
NAD = ['number of duplicated apps:',str(dup_num)]
file_handle.writelines(NAD)
file_handle.write('\n')
print('Expected length:', (len(android) - dup_num))
print('\n')
EALD = ['Expected length:',str((len(android) - dup_num))]
file_handle.writelines(EALD)
file_handle.write('\n')
file_handle.write('\n')

#用新建 dictionary 除去重复数据组

reviews_max = {}

for app in android:
    name = app[0]
    n_reviews = float(app[3])
    
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
        
    elif name not in reviews_max:
        reviews_max[name] = n_reviews

        
#检查一下 reviews_max 中元素数量是不是正确
print('Expected length:', len(android) - 1181)
print('\n')
EAL = ['Expected length:',str((len(android) - 1181))]
file_handle.writelines(EAL)
file_handle.write('\n')
file_handle.write('\n')
print('Actual number:',len(reviews_max))
ANL= ['Actual number:',str(len(reviews_max))]
file_handle.writelines(ANL)
file_handle.write('\n')
file_handle.write('\n')

#开始清除重复应用数据
android_clean = []
already_added = []

for app in android:
    name = app[0]
    n_reviews = float(app[3])#这里利用了数据组的第四列 id 的独一无二来区分相同 name 的重复数据组
    
    if (reviews_max[name] == n_reviews) and (name not in already_added):
        android_clean.append(app)
        already_added.append(name)

explore_data(android_clean, 0, 2, True) #检验元素样本和数量是否正确
file_handle.write('\n')
file_handle.write('\n')

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
print('【选出英语应用】')
file_handle.write('【选出英语应用】')
file_handle.write('\n')

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
file_handle.write('android English Apps samples and total number:')
file_handle.write('\n')
explore_data(android_english, 0, 2, True)
print('\n')
file_handle.write('\n')
print('ios English Apps samples and total number:')
print('\n')
file_handle.write('ios English Apps samples and total number:')
file_handle.write('\n')
file_handle.write('\n')
explore_data(ios_english, 0, 2, True)

#选出英语应用里的免费应用
print('【选出免费的英语应用】')
file_handle.write('【选出免费的英语应用】')
file_handle.write('\n')

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
NFEA = ['Number of android free English Apps:',str(len(android_final))]
file_handle.writelines(NFEA)
file_handle.write('\n')
print('Number of ios free English Apps:',len(ios_final)) 
print('\n')
NFEI = ['Number of ios free English Apps:',str(len(ios_final))]
file_handle.writelines(NFEI)
file_handle.write('\n')
file_handle.write('\n')

print('##结束对数据的清理##')
print('\n')
file_handle.write('##结束对数据的清理##')
file_handle.write('\n')
file_handle.write('\n')

#
print('##开始分析数据##')
print('\n')
file_handle.write('##开始分析数据##')
file_handle.write('\n')
file_handle.write('\n')
# data analysis of genre  app 热门种类百分比
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
        G = [str(entry[1]),':', str(entry[0])]
        file_handle.writelines(G)
        file_handle.write('\n')
    

#Content Rating 苹果应用内容分级占比
print('【Applestore 应用不同分类占比(%)】')
file_handle.write('【Applestore 应用不同分类占比(%)】')
file_handle.write('\n')
display_table(ios_final, -5)
print('\n')
file_handle.write('\n')

#category 安卓应用分级占比
print('【Googleplay 应用分级占比(%)】')
file_handle.write('【Googleplay 应用分级占比(%)】')
file_handle.write('\n')
display_table(android_final, 1)
print('\n')
file_handle.write('\n')

#Genres 安卓应用内容占比
print('【Googleplay 应用内容各自占比(%)】')
file_handle.write('【Googleplay 应用内容各自占比(%)】')
file_handle.write('\n')
display_table(android_final, -4)
print('\n')
file_handle.write('\n')

#average number of installs for each ios app genre 苹果各个应用内容的应用的平均下载量
print('【Applestore 不同应用分类应用的平均下载量】')
file_handle.write('【Applestore 不同应用分类应用的平均下载量】')
file_handle.write('\n')

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
    GIOS = [genre, ':',str(avg_n_ratings)]
    file_handle.writelines(GIOS)
    file_handle.write('\n')
print('\n')
file_handle.write('\n')

#user rating
print('【Applestore 导航类各应用的评价人数】')
file_handle.write('【Applestore 导航类各应用的评价人数】')
file_handle.write('\n')
for app in ios_final:
    if app[-5] == 'Navigation':
        print(app[2],':', app[6]) # print name and number of ratings
        AAA = [str(app[2]),':', str(app[6])]
        file_handle.writelines(AAA)
        file_handle.write('\n')
print('\n')
file_handle.write('\n')

#Reference
print('【Applestore 参考类各应用的评价人数】')
file_handle.write('【Applestore 参考类各应用的评价人数】')
file_handle.write('\n')
for app in ios_final:
    if app[-5] == 'Reference':
        print(app[2], ':', app[6])
        AAA = [str(app[2]),':', str(app[6])]
        file_handle.writelines(AAA)
        file_handle.write('\n')
print('\n')
file_handle.write('\n')

#Most Popular Apps by Genre on Google Play
print('【Googleplay 应用下载数量级占比（%）】')
file_handle.write('【Googleplay 应用下载数量级占比（%）】')
file_handle.write('\n')
display_table(android_final, 5) # the Installs columns
print('\n')
file_handle.write('\n')

# name + procentage
categories_android = freq_table(android_final, 1)
print('【Googleplay 不同分类应用平均下载量（%）】')
print('\n')
file_handle.write('【Googleplay 不同应用分类应用平均下载量（%）】')
file_handle.write('\n')
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
    CA = [category, ':', str(avg_n_installs)]
    file_handle.writelines(CA)
    file_handle.write('\n')
print('\n')
file_handle.write('\n')

# 
print('【Googleplay 通信类应用高下载量软件及其下载数量级】')
print('\n')
file_handle.write('【Googleplay 通信类应用高下载量软件及其下载数量级】')
file_handle.write('\n')
for app in android_final:
    if app[1] == 'COMMUNICATION' and (app[5] == '1,000,000,000+'
                                      or app[5] == '500,000,000+'
                                      or app[5] == '100,000,000+'):
        print(app[0], ':', app[5])
        AA = [app[0], ':', str(app[5])]
        file_handle.writelines(AA)
        file_handle.write('\n')
print('\n')
file_handle.write('\n')

#这个程序是为了看一下如果去掉那些超过一亿下载量的应用之后样本中Googleplay应用的平均下载量，

under_100_m = []

for app in android_final:
    n_installs = app[5]
    n_installs = n_installs.replace(',', '')
    n_installs = n_installs.replace('+', '')
    if (app[1] == 'COMMUNICATION') and (float(n_installs) < 100000000):
        under_100_m.append(float(n_installs))

print(sum(under_100_m) / len(under_100_m))
print('\n')
SL = str(sum(under_100_m) / len(under_100_m))
file_handle.write('【如果去掉那些超过一亿下载量的应用之后通信类应用样本中Googleplay应用的平均下载量】：')
file_handle.write('\n')
file_handle.write(SL)
file_handle.write('\n')
file_handle.write('\n')

#

print('【Googleplay 参考类软件及其下载数量级】')
print('\n')
file_handle.write('【Googleplay 参考类软件及其下载数量级】')
file_handle.write('\n')
for app in android_final:
    if app[1] == 'BOOKS_AND_REFERENCE':
        print(app[0], ':', app[5])
        AA = [app[0],':', app[5]]
        file_handle.writelines(AA)
        file_handle.write('\n')
print('\n')
file_handle.write('\n')

#

print('【Googleplay 参考类高下载量应用及其下载数量级】')
print('\n')
file_handle.write('【Googleplay 参考类高下载量应用及其下载数量级】')
file_handle.write('\n')
for app in android_final:
    if app[1] == 'BOOKS_AND_REFERENCE' and (app[5] == '1,000,000,000+'
                                            or app[5] == '500,000,000+'
                                            or app[5] == '100,000,000+'):
        print(app[0], ':', app[5])
        AA = [app[0],':', app[5]]
        file_handle.writelines(AA)
        file_handle.write('\n')
print('\n')
file_handle.write('\n')

#

print('【Googleplay 通信类软件中高下载量软件及其下载数量级】')
print('\n')
file_handle.write('【Googleplay 通信类软件中高下载量软件及其下载数量级】')
file_handle.write('\n')
for app in android_final:
    if app[1] == 'BOOKS_AND_REFERENCE' and (app[5] == '1,000,000+'
                                            or app[5] == '5,000,000+'
                                            or app[5] == '10,000,000+'
                                            or app[5] == '50,000,000+'):
        print(app[0], ':', app[5])
        AA = [app[0],':', app[5]]
        file_handle.writelines(AA)
        file_handle.write('\n')
print('\n')
file_handle.write('\n')

print('##结束数据分析##')
file_handle.write('##结束数据分析##')
print('\n')

file_handle.close()

print('请在当前文件夹内查看 result.txt 获取分析结果')