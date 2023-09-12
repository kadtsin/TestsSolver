import json

dataset = dict()
flag_ans = False
flag_question = False
question = ''

with open('example.txt', 'r', encoding='utf8') as file:
    for line in file:
        if line != '\n':
            if "Задание" in line:
                flag_question = True
            elif flag_question:
                question = line.replace('\n', '')
                flag_question = False
            if '+' in line:
                flag_ans = True
            elif flag_ans:
                if question in dataset:
                    dataset[question] += [line.replace('\n', '')]
                else:
                    dataset[question] = [line.replace('\n', '')]
                flag_ans = False

with open('database.json', 'w', encoding='utf8') as file:
    json.dump(dataset, file, ensure_ascii=False)
