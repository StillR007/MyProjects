name = str(input('Ведите имя'))
surname = str(input('Ведите фамилию'))
age = int(input('Ведите возраст'))
weight = float(input('Ведите вес'))

if age < 30 and (50 < weight < 120):
    print(name, surname, 'возраст:', age, 'вес:', weight, ' - хорошее состояние')
elif age < 30 and not (50 < weight < 120):
    print(name, surname, 'возраст:', age, 'вес:', weight, ' - следует обратиться к врачу')
elif 30 <= age < 40 and not (50 < weight < 120):
    print(name, surname, 'возраст:', age, 'вес:', weight, ' - следует заняться собой')
elif 30 <= age < 40 and (50 < weight < 120):
    print(name, surname, 'возраст:', age, 'вес:', weight, ' - хорошее состояние')
elif age >= 40 and not (50 < weight < 120):
    print(name, surname, 'возраст:', age, 'вес:', weight, ' - следует обратиться к врачу')
elif age >= 40 and (50 < weight < 120):
    print(name, surname, 'возраст:', age, 'вес:', weight, ' - следует поддерживать себя в форме')
