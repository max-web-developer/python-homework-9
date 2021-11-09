
# my_dictionary = {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}
# summ=sum(my_dictionary[elem] for elem in my_dictionary)
# print(summ)

my_dictionary = {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}
output= 1 #чтоб индекс не был нулевым
for index in my_dictionary:    
    output = output * my_dictionary[index]
print(output)