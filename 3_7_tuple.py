data = (('Виталий', 243), ('Виктор', 404), ('Василий', 812), ('Павел', 907))
for item in data:
    print('{0} пройдите пожалуйста в кабинет номер {1}'.format(*item))