# Домашннее задание №1
#Напишите функцию (имя можете быть любое), которая будет суммировать все целые числа от первого до второго параметра, 
# если первый параметр будет больше второго, то поменяйте их местами.

a = int(input('Введите первый параметр: '))
b = int(input('Введите второй параметр: '))

def sumator(a,b):
    sum=0
    if a<b:
        for i in range(a,b+1):
            sum+=i
        print (sum)
    else:
        for i in range(b,a+1):
            sum+=i
        print (sum)
sumator(a,b)

# Домашннее задание №2
# Напишите функцию, которая будет принимать на себя 2 параметра в виде имени и фамилии студента, 
# а выводить на экран запись вида Привет Имя Фамилия.

fname = str(input('Введите Имя: '))
lname = str(input('Введите Фамилию: '))

def spisok(lname,fname):
    lname=lname
    fname=fname
    print(f"Привет {lname} {fname}")

spisok(fname,lname)

#Домашнее задание №3
#Создайте функцию, которая позволяет посчитать 
# периметр и площадь квадрата (значения сторон вводит пользователь).

x=int(input("Введите дилинну первой стороны квадрата :"))
y=int(input("Ведите длинну второй стороны квадрата :"))
def mat(x,y):
    print("Площадь квадрата равна = ", x*y)
    print("Периметр квадрата равен = ", 2*(x+y))
mat(x,y)

# def message_form(a,b,c,d):   
#     print(f'Имя :{a}')
#     print(f'Работа:{b}')
#     print(f"Возраст:{c}")
#     print(f'Зарплата:{d}')

# a = input('Введите Имя: ')
# b = input('Введите своё место работы:')
# c = int(input('Введите свой возраст:'))
# if c>=99:
#     print("Ваш возраст не может быть больше 99. Либо вы очень редкий долгожитель =)")
# elif c < 18:
#     print("Кажется вам ещё рано заходить на наш сервис х)")
# else:
#     d = int(input('Введите свою зарплату:'))

#     #print(f'Возраст:{c}')
# #d = input(int('Введите свою зарплату:'))

# message_form(a,b,c,d)















# message_form ("1","2",'3','4')    

# def my (a,b):
#     d=a+b
#     return d
# print ( my (10,10)+20) 

# def square(num):
#     return 
#     num * num
# print (square(4))

# args
# kwargs

# def argss (*args):
#     for i in args:
#         print (args)
# argss ('1','2','3')

# def argss (*args):
#     print (args)
# argss ('1','2','3')

# def kwar(**qwe):
#     for i, value in qwe.items ():
#         printf (f` i:{value}` )
# kwar (first = 'Hello', world = " worldf")    

# aquare = lambda num : print (num*num)
# (aquare (8)

