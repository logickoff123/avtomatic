n = input ('Ввод:  ').split(' ')
comba = ['камень', 'ножницы', 'бумага'] # список слов 
array = ['ничья','первый', 'второй'] 

first = comba.index(n[0]) # индекс перовго слова игорока
second = comba.index(n[1]) # индекс второго слова игорока
diff = second - first # разница индексов 

#print(diff, first, second)
print(f"победил {array[diff]}")
   