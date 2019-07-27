import getpass
username = input('请输入用户名：')
password = getpass.getpass('请输入密码：')
if username == 'admin' and password == 'password':
    print('身份验证成功')
else:
    print('身份验证失败')
x = float(input('x ='))
#good
if x > 1:
    y = 3*x - 5
elif -1 <= x <= 1:
    y = x + 2
else:
    y = 5*x + 3
print('f(%.2f)=%.2f' % (x,y))
#good
x = float(input('x ='))
if x > 1:
    y = 3*x - 5
else:
    if -1 <= x <= 1:
         y = x + 2
    else:
         y = 5*x + 3
print('f(%.2f)=%.2f' % (x,y))
#good
#unit change
value = float(input('请输入长度'))
unit = str(input('请输入单位'))
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value,value*2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米 = %f英寸' % (value,value/2.54))
else:
    print('请输入有效单位')
#good
#百分制成绩转等级制成绩
#90分以上    --> A
#80分~89分    --> B
#70分~79分	   --> C
#60分~69分    --> D
#60分以下    --> E
score = int(input('成绩：'))
if score >= 90:
    grade = 'A'
elif 80 <= score <=89:
    grade = 'B'
elif 70 <= score <=79:
    grade = 'C'
elif 60 <= score <=69:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是',grade) 
#roll the dice
from random import randint
value = randint(1,9)
if value == 1:
    print('攻击+8')
elif value == 2:
    print('获得+1长剑一把')
elif value == 3:
    print('攻击无效')
elif value == 4:
    print('原地爆炸')
elif value == 5:
    print('砍到队友')
elif value == 6:
    print('暴击*2')
elif value == 7:
    print('被反伤一次')
else:
    print('击中')
#calculate the area of triangle
import math
a = float(input('a ='))
b = float(input('b ='))
c = float(input('c ='))
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c )/2
    area = math.sqrt(p*(p - a)*(p - b)*(p - c))
    print('周长 = %f' % (a+b+c))
    print(area)
else:
    print('此三边无法构成三角形')
salary = float(input('月收入：'))
insurance = float(input('五险一金：'))
diff = salary - insurance
if diff <= 0:
    rate = 0
    deduction = 0
elif diff <= 1500:
    rate = 0.03
    deduction =0
elif diff < 4500:
    rate = 0.1
    deduction = 105
elif diff < 9000:
    rate = 0.2
    deduction = 555
elif diff < 35000:
    rate = 0.25
    deduction = 1005
elif diff < 55000:
    rate = 0.3
    deduction = 2755
elif diff < 80000:
    rate = 0.35
    deduction = 5505
else:
    rate = 0.45
    deduction = 13505
tax = abs(diff * rate - deduction)
print('个人所得税: ￥%.2f元' % tax)
print('实际到手收入: ￥%.2f元' % (diff + 3500 - tax))
#haven't check
#循环迭代
#for...in recycle:
sum = 0
for x in range (101):
    sum += x
   #print (sum)#print位置的变化造成结果的不同
print(sum)
#分割线
sum = 0 
for x in range (2,101,2):
    sum += x
print(sum)
sum = 0
for x in range (1,101):
    if x % 2 == 0:
        sum +=x
print(sum)
#猜数字
import random
answer = random.randint(1,100)
count = 0
while True:
    count += 1
    number = int(input('请输入'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('猜对了')
        break
print('你总共猜了%d次' % count)
if count >= 7:
    print('你的智商明显不足')#good 好玩
#九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()#did not totally understand
#素数
from math import sqrt
num = int(input('请输入一个正整数'))
end = int(sqrt(num))
is_prime = True
for x in range (2,end + 1):
    if num % x == 0:#这里一开始打错了x打成2
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数'% num)#need to be understood
x = int(input('x ='))
y = int (input('y ='))
if x > y:
    x,y = y,x
for factor in range (x,0,-1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数为%d' % (x,y,factor))
        print('%d和%d的最小公倍数为%d' % (x,y,x*y/factor))
        break#不是很理解，如果不加break就会跳出1和54...所以问题到底出在哪？
#打印三角形

#水仙花数
for x,y,z in range(0,10):
    if x*100 + y*10 + z == x**3 + y**3 + z**3:
        print('%d' % x*100 + y*10 + z)
    else:
        pass

for x in range (1,10):
    for y in range (0,10):
        for z in range(0,10):
            Nnumber = x*100 + y*10 +z
        if Nnumber == x**3 + y**3 + z**3:
            print(Nnumber)
        else:
            pass




    


