#Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
#Подсчитайте количество слов в тексте
#Замените точки в тексте на восклицательные знаки
#Сохраните результат в файл referat2.txt

with open('referat.txt','r',encoding='utf-8') as ref:
    ref = ref.read()
    ref = ref.replace('.','!')
    word_count = 0
    for word in ref:
        word_count = word_count+1
print(word_count)
with open('referat2.txt','w',encoding='utf8') as ref2:
    ref2.write(ref)
