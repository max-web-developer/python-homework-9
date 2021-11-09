# Coздайте словарь из строки 'pythonist' следующим образом: в качестве ключей возьмите буквы строки,
# а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.



# =) непонял как это сделать)





str1='pythonist'
my_dictionary=[]
for i in str1:
    str1.count(i)
    my_dictionary.append(i)
print(my_dictionary)







# str1 = 'pythonist'
# my_dict = {i: str1.count(i) for i in str1}
# print(my_dict)
