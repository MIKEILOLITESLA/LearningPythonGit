print ("hello world")
name = input ()
# mike
print (name)
#input() practice
name = input ("please enter your name :")    #good
#print (1024*768=)
print ("1024 * 768 =",1024*768 )    #good
#print without space
result = 1024*768
strResult = str(result)
strWhole = "1024*768="+strResult
print(strWhole)    #good
#\\
print('\\\n\\')    #good
print("I\'m \'OK\'")    #good
print('\\\t\\')
# \n
print('''爸爸 
妈妈
孩子''')    #good
# 布尔数
3>1
90<30    #good
True and True
not True 
not False
False and True
False and False
not False and True
False or True
5 > 3 or 3 < 1 #good
s = input('age:')
AGE = int(s)
if AGE >= 18:
    print('adult')
else:
    print('teenager')    #not good
#chr()_transfer the code to the characters
#ord('')_transfer the character to the code
'\u4e2d\u6587'#'中文'
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
# practice of 'if elif else'

# BMI = weight/(height*2)
80.5/(1.75**2)

t = input ('please enter your hight:')
p = input ('please enter your weight:')
t = float(t)
p = float(p)
BMI = p / (t**2)
if BMI > 32:
    print ('严重肥胖')
elif BMI >= 28:
    print ('肥胖')
elif BMI >= 25:
    print ('过重')
elif BMI >= 18.5:
    print ('正常')
else:
    print ('过轻') #good

#循环
sum = 0
for x in range (101):
    sum = sum + x
print (sum)

sum = 0
n = 999
while n > 0:
    sum = sum + n
    n = n -2
print(sum)
#break
n = 1
while n <= 100:
    if n>= 20:
        break
    print (n)
    n = n + 1

print('end')
#continue 
n = 1
while n <50:
    n = n + 1
    if n % 2 == 0:
        continue
    print (n)    #good
#dictionary
dict = {'mice':100, 'lin':66,'dianna':33}
dict['mice']
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x    #good
#函数
def my_sabs(x):
    if not isinstance(x,(int or float)): #Q: may the x be more than one characte
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x    #good
#function2
def quadratic(a, b, c):
    nx1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
    nx2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
    return nx1, nx2 # too complex?
#function2
import math
def quandratic(a, b, c):
    d = b*b - 4*a*c
    if d < 0:
        print('no reasonabe result')
    elif d == 0:
        x0 = -b/(2*a)
        return x0
    elif d > 0:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        return x1, x2     # good
#函数参数
def power (x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s    # good





