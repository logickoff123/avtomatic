#def my_personal_sun(x: int |float , y:int) -> int|float: # последня херь со стрелочкой это то что функция вернет
    #pass

#print('hello')
    
#def my_personal_sum (*args, **kwargs) -> int|float
   # print (f'Args: {args}')
   
   
#практика 3 (пишем функцию)

n = int(input())

def guess(n):
    if n/2<1:
        p = (n)
    elif n>0:
        for i in range(n+1):
            if i*i == n:
                p = i
                i= i+1
                if p is not None:
                    return p
            elif i == n:
                    p = "Я не могу такое вычетать"
                    
    return p

g = guess(n)
print (g)


    
 