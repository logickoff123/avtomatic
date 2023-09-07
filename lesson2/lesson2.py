#_list: list = [1, 2, 23, None, 'sad',]
#print (_list [1:7])
#print (_list[0:-1:2])
#print (_list [::-1])

#_set: set = ([i,f s ,n ,b ,g])
#_set2: set = {'m', 'i', 's', 'p', }
#print (_list)

#_list1 = [1, 2, 3, 4]

#_list1.append([5,6])

#print(_list1[-1])


#_matrix = [
    #[1, 2, 3],
    #[2, 3, 4],
    #[5, 6, 7]
#]

#print (_matrix[2][2])

numbers: list  = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in numbers:
    if n %3 == 0:
        print(f'Число {n}')
    elif n%5 ==0:
        print(f'Число {n}')
    else:
        print(f'Число не кратное {n}')