#
a_list = [1, 8, 10, 9, 7]
print(max(a_list))
def max(list1):
    return 'No max value returned'
max_val_test_0 = max(a_list)
print(max_val_test_0)
del max

#
def open_dataset(file_name = 'AppleStore.csv'):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    return data

apps_data = open_dataset()

#
one_decimal = round(3.43, ndigits=1)
two_decimals = round(0.23321, 2)
five_decimals = round(921.2225227, 5)

#
def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:]
    else:
        return data
    
apps_data = open_dataset()

#
def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:], data[0]
    else:
        return data
    
all_data = open_dataset()

#
def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:], data[0]
    else:
        return data
apps_data, header = open_dataset()

#
def print_constant():
    x = 3.14
    #return x
    print(x)
    
j = print_constant()
print(j)
type (j)

#
e = 'mathematical constant'
a_sum = 1000
length = 50
def exponential(x):
    e = 2.72
    print(e)
    return e**x

result = exponential(5)
print(e)

def divide():
    print(a_sum)
    print(length)
    return a_sum / length

result_2 = divide()
