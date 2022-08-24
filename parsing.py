file = open('file_for_parsing.txt', 'r')


def read_and_sorted_one_line(file):
    english_words = []
    russian_words = []
    while True:
        line = file.readline()  # считываем строку
        one_str = line.split('\t', 1)  # разбиваем строку по символу табуляции
        if len(one_str) == 2:
            english_words.append(one_str[0] + '\n')
            russian_words.append(one_str[1])

        if not line:  # в случае окончания файла завершаем цикл
            break

    return russian_words, english_words


def create_file_txt(name, words):
    file_txt = open(f"{name}.txt", "w+")
    for item in words:
        file_txt.write("%s" % item)
    file_txt.close()


russian_words, english_words = read_and_sorted_one_line(file)
create_file_txt("Russian", russian_words)
create_file_txt("English", english_words)
file.close()
