from math import sqrt#sqrt求平方根函数
for num in range (1,10):#n 是
    end  = int(sqrt(num))
    for x in range (2,end + 1):
        if num % x != 0 and num != 1:
            p = num 
            for x in range (2,end + 1):
                if (2**(p - 1)) % x != 0 :
                    break
                elif (2**(p - 1)) != 1 :
                    D = (((2**p) - 1) *(2**(p - 1)))
                    print('%d 是完美数' % D)

                  