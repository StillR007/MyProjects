import json
import datetime

path = 'todos.json'

date_file_name = datetime.datetime.today().strftime("%Y-%m-%d")
date_text = datetime.datetime.today().strftime("%d.%m.%Y %H:%M")


def string_to_row(iterab):
    new_string = '\n'.join(iterab)
    return new_string


def write_a_file(user_id, completed_tasks, incompleted_tasks):
    file = open(f"{user_id}_{date_file_name}.txt", "w+")
    file.write(f"# Сотрудник №{user_id}\n{date_text}\n\n## Завершенные задачи:\n"
               f"{str(string_to_row(completed_tasks))}\n\n"
               f"## Оставшиеся задачи:\n{str(string_to_row(incompleted_tasks))}")


def get_user_id(data):
    user_ids = []
    for row in data:
        _one_id = row.get('userId')
        if _one_id:
            user_ids.append(_one_id)
    user_ids = set(user_ids)
    return user_ids


def get_status(row, completed_tasks, incompleted_tasks):
    row['title'] = make_it_shorter(row['title'])
    if row['completed'] is True:
        completed_tasks.append(row['title'])
    else:
        incompleted_tasks.append(row['title'])
    return completed_tasks, incompleted_tasks


def make_it_shorter(title):
    if len(title) > 50:
        title = title[:50]
        title = str(title) + '...'
    return title


def main():
    with open(path, 'r') as file:
        data = json.loads(file.read())

        completed_tasks = []
        incompleted_tasks = []
        user_ids = get_user_id(data)

        for row in data:
            if len(row) == 4:
                print(row)
                for user_id in user_ids:
                    if row['userId'] == user_id:
                        completed_tasks, incompleted_tasks = get_status(row, completed_tasks, incompleted_tasks)
                        write_a_file(user_id, completed_tasks, incompleted_tasks)


if __name__ == '__main__':
    main()
