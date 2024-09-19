def all_variants(text):
    for size in range(1,len(text) +1):#Цикл по size перебирает возможные длины подпоследовательностей.
        for start in range(len(text)-size +1):#Внутри этого цикла start перемещает срез по строке, начиная с каждого возможного индекса.
            yield text[start:start + size]#Каждая итерация генератора возвращает срез строки нужной длины.

a = all_variants("abc")
for i in a:
    print(i)