'''
как я понял задание из примера к каждому английскому слову приставляю русское
и к каждому русскому переставляю каждое английское
'''

file = open('file_for_parsing.txt', 'r')


def read_sorted_one_line(file):
    english_words = []
    russian_words = []

    while True:
        line = file.readline()  # считываем строку
        one_str = line.split('\t', 1)  # разбиваем строку по символу табуляции
        if len(one_str) == 2:
            english_line = one_str[0].split(';')
            russian_line = one_str[1].split(';')

            for i in range(len(english_line)):
                english_words.append(english_line[i].strip() + '\n')  # добавляю каждое анлийское слово на новую строку
                russian_words.append(russian_line[0].strip() + '\n')  # добовляю первое русское слово к каждому англий
            if len(russian_line) != 1:  # если русских слов больше чем одно к каждому слову добавляем все английские
                for x in range(len(russian_line)-1):
                    for it in range(len(english_line)):
                        russian_words.append(russian_line[x].strip() + '\n')  # добавляю второе руское слово
                        english_words.append(english_line[it].strip() + '\n')  # добавляю каждое ангийское

        if not line:  # в случае окончания файла завершаем цикл
            break

    return russian_words, english_words


def create_file_txt(name, words):  # создаём файл txt
    file_txt = open(f"{name}.txt", "w+")
    for item in words:
        file_txt.write("%s" % item)
    file_txt.close()


russian_words, english_words = read_sorted_one_line(file)
create_file_txt("Russian", russian_words)
create_file_txt("English", english_words)

file.close()