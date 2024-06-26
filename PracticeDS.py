# Работа со словарями: Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
# Например: Имя(str)-Год рождения(int).

my_dict={'Oleg': 1990, 'Tania': 1992, 'Dania': 2000, 'Nikita': 2004}
print('Dict:', my_dict) # Выведите на экран словарь my_dict

print('Existing value:',my_dict['Tania']) # Выведите на экран одно значение по существующему ключу
print('Existing value:',my_dict.get('Tania')) # или так
print('Not existing value:',my_dict.get('Kristina','Нет в словаре')) # одно по отсутствующему из словаря my_dict без ошибки
print('Not existing value:',my_dict.get('Kristina')) # одно по отсутствующему из словаря my_dict без ошибки

my_dict.update({'Vlad': 2014, 'Nik': 2022}) # Добавьте ещё две произвольные пары того же формата в словарь my_dict
my_dict['Rik']=2024 # # Добавил ещё одного но немного иначе
print(my_dict)

removed=my_dict.pop('Oleg') # Удалите одну из пар в словаре по существующему ключу из словаря my_dict
print(my_dict)
print('Deleted value:',removed) # и выведите значение из этой пары на экран

print(my_dict) # Выведите на экран словарь my_dict
print(my_dict.items()) # или так

# Работа с множествами: Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями
my_set={1,1.1,1,'str',True,(1,2,3),1.1}
print(my_set)

my_set.add('Oleg') # Добавьте 2 произвольных элемента в множество my_set, которых ещё нет
my_set.add(3.14)
my_set.remove('str') # Удалите один любой элемент из множества my_set.
print(my_set) # Выведите на экран измененное множество my_set