time_in_seconds = int(input('Введите время в секундах'))
time_in_minutes = int(0)
time_in_hours = int(0)

while time_in_seconds >= 60:
    time_in_minutes += 1
    time_in_seconds -= 60

while time_in_minutes >= 60:
    time_in_hours += 1
    time_in_minutes -= 60

if time_in_seconds <= 9:
    time_in_seconds = "0" + str(time_in_seconds)

if time_in_minutes <= 9:
    time_in_minutes = "0" + str(time_in_minutes)

if time_in_hours <= 9:
    time_in_hours = "0" + str(time_in_hours)

print("Это: ", time_in_hours, ':', time_in_minutes, ':', time_in_seconds)
