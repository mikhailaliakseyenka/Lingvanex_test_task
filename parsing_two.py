'''
Были вопросы по заданию написал на почту никто не ответил поэтому сделал и второй вариант
уже без дублирования английских слов
все фалы из это парсинга с подпиской _two
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
            for i in range(len(english_line)):
                english_words.append(english_line[i].strip() + '\n')
                russian_words.append(one_str[1])

        if not line:  # в случае окончания файла завершаем цикл
            break

    return russian_words, english_words


def removing_duplicate_words(russian_words, english_words):  # убираем повторяющиеся слова с двух сторон
    english_words_individual = []
    russian_words_individual = []

    for i in range(len(english_words)):  # не добавляю в список повторяющиеся слова
        if english_words[i] not in english_words_individual:
            english_words_individual.append(english_words[i])
            russian_words_individual.append(russian_words[i])

    return english_words_individual, russian_words_individual


def create_file_txt(name, words):  # создаём файл txt
    file_txt = open(f"{name}.txt", "w+")
    for item in words:
        file_txt.write("%s" % item)
    file_txt.close()


russian_words, english_words = read_sorted_one_line(file)
english_words_individual, russian_words_individual = removing_duplicate_words(russian_words, english_words)

create_file_txt("Russian_two", russian_words_individual)
create_file_txt("English_two", english_words_individual)

file.close()
