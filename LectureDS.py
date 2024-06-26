print('Date: 26.06.2024')
print('Topic: Dictionaries and Sets')
# Catching up: %
a=7/3
b=7//3
c=7%3
d=8%3 # первое значение остатка
print(a,b,c,d)
# Catching up: sep=''
print(a,b,c,d,sep='') # убирает авто пробелы в функции print
# Let us get started the Topic
phone_book = {'Oleg':+71111111111,'Tania':+72222222222} # скобки фигурные, ключ идет первым, вторым значение с двоеточием между
print(phone_book) # пара ключ, значение - это один объект
print(phone_book['Oleg']) # 71111111111
phone_book['Oleg']=+72222222223 # можем менять значение пары и даже на одинаковый
print(phone_book)
phone_book['Nikita']=+77777777774 # если нет, то просто добавляет пару
print(phone_book)
del (phone_book['Oleg']) # удаление
print(phone_book)
phone_book.update({'Oleg':+71111111111,'Dania':+73333333333,
                   'Kristina':+74444444444}) # добавляем несколько пар и можно на одной или несколько строк
print(phone_book) # {'Tania': 72222222222, 'Nikita': 77777777777, 'Oleg': 71111111111, 'Dania': 73333333333, # 'Kristina': 74444444444}
print(phone_book.get('Oleg')) # 71111111111 - получить значение по ключу
print(phone_book.get('Kamila','Нет такого ключа')) # None или Нет такого ключа
# если ключа нет, то выпадает None, но мы можем сказать, что должно выпасть 'Нет такого ключа'
phone_book.pop('Oleg') # удалили ключ
print(phone_book) # {'Tania': 72222222222, 'Nikita': 77777777777, 'Dania': 73333333333, 'Kristina': 74444444444}
a=phone_book.pop('Tania')
print(phone_book) # нет уже Тани - {'Nikita': 77777777777, 'Dania': 73333333333, 'Kristina': 74444444444}
print(a) # есть ее номер
# тоже самое можно делать со списком
list_=[1,2,3,4,5,6] # список
print(list_) # [1, 2, 3, 4, 5, 6]
print(list_[0]) # 1 - вывести первый индексом
print(list_.pop(0)) # 1 - удалить и вывести первый используя pop
print(list_.pop(0)) # 2 - удалить и вывести первый из того что осталось
print(list_) # вывести остаток
# обратно к словарям
print(phone_book.keys()) # список ключей словаря - dict_keys(['Nikita', 'Dania', 'Kristina'])
print(phone_book.values()) # значения ключей словаря - dict_values([77777777777, 73333333333, 74444444444])
print(phone_book.items()) # значения пар словаря - dict_items([('Nikita', 77777777777), ('Dania', 73333333333), ('Kristina', 74444444444)])
print(phone_book) # {'Nikita': 77777777777, 'Dania': 73333333333, 'Kristina': 74444444444}
# ключ не изменяем, значения же можно изменять как мы видели и добавлять списком
phone_book={'Nikita': [77777777777, 490000000000], 'Dania': 73333333333, 'Kristina': 74444444444}
print(phone_book) # {'Nikita': [77777777777, 490000000000], 'Dania': 73333333333, 'Kristina': 74444444444}
# так можно детализовать и пары логин и пароль
set_={1,1.1,1,'str',True,(1,2,3),1.1}
print(set_) # {1, (1, 2, 3), 'str', 1.1} - все типы данных, но без повторений, в иной последовательности и не показывает boolian
print(list_) # [3, 4, 5, 6]
print(set(list_)) # {3, 4, 5, 6} - перевели список в множество и вывели
list_=set(list_) # функцией преобразовали в множество
print(list_) # {3, 4, 5, 6} вывели
list_.discard(3)
print(list_) # {4, 5, 6} вывели остаток
print(list_.remove(4)) # None - удалили 4, зачем print - показать, что ее нет?
print(list_) # {5, 6} - что осталось
# discard не будет выдавать ощибку - если не найден во множестве, remove будет
list_.add(7)
print(list_)
print(list_.add(8)) # None
print(list_) # {5, 6, 7, 8}
print(list_.pop()) # 5