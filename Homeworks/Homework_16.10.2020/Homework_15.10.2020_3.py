low_salary = []
need_salary = 20000
all_salaries = []
with open("My_file_3.txt") as my_file:
    for line in my_file:
        # print(line.split())
        name, salary = line.split()
        salary = int(salary)
        all_salaries.append(salary)
        if salary < need_salary:
            low_salary.append(name)
    print(f'оклад менее {need_salary} у {low_salary}')
    print(f'средний оклад сотрудников {sum(all_salaries)/len(all_salaries)}')
