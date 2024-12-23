
# # Примеры
#     "Python Community",
#     "i like python community!",
#     "Should, I. subscribe? Yes!"



user_input = "Python Community"

# Удаляем знаки препинания и пробелы
user_input = user_input.replace(",", "").replace(".", "").replace("!", "").replace("?","")
user_input = user_input.replace(";", "").replace(":", "").replace("-", "").replace("_", "")

# Разбиваем строку на слова
words = user_input.split()

# Делаем каждое слово с большой буквы, соединяем их и добовляем #
hashtag = "#"
for word in words:
    hashtag += word.capitalize()

# Проверяем длину хэштега, если больше 140 символов, обрезаем
if len(hashtag) > 140:
    hashtag = hashtag[:140]

# Результат
print(hashtag)
