number = str(input('Введите целое положительное число'))
max_number = int(number[0])
seq_number = int(0)

while seq_number <= int(len(number) - 1):
    if max_number < int(number[seq_number]):
        max_number = int(number[seq_number])
    seq_number += 1

print(max_number)
