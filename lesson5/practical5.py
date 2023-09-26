def convert_ab_to_int (a: str, b:str) -> tuple [int, int]:
    return a, b

def devided (a: int )

while True:
    a, b =input ("Введите два числа для их суммы").split()
    try:
        a,b  =  convert_ab_to_int(a, b)
        devided  = devided(a, b)
    except:
        print("абобус")
        print()
        continue
    #a,b = int(a), int(b)
    
    a_b = a+b
    print (f"Суммы {a} + {b} = {a_b}")
    print()