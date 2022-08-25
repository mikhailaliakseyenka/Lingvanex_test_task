file = open('file_for_parsing.txt', 'r')


def read_sorted_one_line(file):
    english_words = []
    russian_words = []

    while True:
        line = file.readline()  # считываем строку
        one_str = line.split('\t', 1)  # разбиваем строку по символу табуляции
        if len(one_str) == 2:
            english_line = one_str[0].split(';')  # разбиваем англ и рус строку на отдельные слова
            russian_line = one_str[1].split(';')

            print(english_line)
            print(russian_line)




            for i in range(len(english_line)):
                english_words.append(english_line[i].strip() + '\n')
                russian_words.append(one_str[1].strip() + '\n')

        if not line:  # в случае окончания файла завершаем цикл
            break

    return russian_words, english_words


def removing_duplicate_words(russian_words, english_words):  # убираем повторяющиеся слова с двух сторон
    english_words_individual = []
    russian_words_individual = []

    for i in range(len(english_words)):  # не добавляю в список повторяющиеся слова
        if english_words[i] not in english_words_individual:
            english_words_individual.append(english_words[i])

            russian_line = russian_words[i].split(';')
            if len(russian_line) != 1:
                individual_rus = []
                for x in range(len(russian_line)):
                    individual_rus.append(russian_line[x].strip())
                one_str_rus = list(set(individual_rus))
                russian_words_individual.append(one_str_rus)
            else:
                russian_words_individual.append(russian_line)


    return english_words_individual, russian_words_individual


def create_file_txt(name, words):  # создаём файл txt
    file_txt = open(f"{name}.txt", "w+")
    for item in words:
        file_txt.write("%s" % item)
    file_txt.close()


russian_words, english_words = read_sorted_one_line(file)
english_words_individual, russian_words_individual = removing_duplicate_words(russian_words, english_words)

create_file_txt("Russian", russian_words_individual)
create_file_txt("English", english_words_individual)

file.close()
