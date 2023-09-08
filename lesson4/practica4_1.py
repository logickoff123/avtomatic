from practica4 import RACE_DATA # перенесла файлик сюды

vals = list(RACE_DATA.values()) # преобразую в список 

sorted_values = sorted(vals, key=lambda d: d['FinishedPlace']) # сортировка 

s = f'Выйграл - ' + sorted_values[0]['RacerName'] + "!!! Поздравляем!!" # присваиваем строку чтобы в дальнейшем посчитать черточки 
print(s)
print (len(s) * "-") # выводим столько черточек сколько и букв в строке (по длине )

print("Первые три места:\n") # вывод

for  v in (sorted_values[:3]): # делаем срез трех гонщиков и выводим данные 
    print (f"Гонщик на {v['FinishedPlace']} месте: ")
    print (f"\tИмя: {v['RacerName']}")
    print (f"\tКоманда: {v['RacerTeam']}")
    print (f"\tВремя: {v['FinishedTimeSeconds']//3600}:{(v['FinishedTimeSeconds'] // 60) % 60} {v['FinishedTimeSeconds'] % 60} (H:M:S)")


#Зона испытаний работала по документации со словарями и списками -_-

# my_dict = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

# print(my_dict['jack']) 

# vals = list(my_dict.values())
# sorted_values = sorted(vals)

# print (sorted_values)