 # todo => category 
 # ! Question
 #  Solution 
 

# todo = ShortCut
# ! Exchange 2 variable 
a = 1
b = 2
a,b = b,a 
# print(f'{a}=a, {b}=b')

# ! reverse or flip a string, list (! can not reverset set or dictionary)
str1 = 'henry'
list1 = ['d','o','g']
dict1 = {'a':1,'b':2,'c':3}
# print(str1[::-1])
# print(list1[::-1])

# ! combine 2 dictionaries
dic1 = {'a':1, 'a':222}
# new key/value pair will mutate the old one 
dic2 = {'b':2, 'c':3}
dic3 = {'x':100}
dicAll={**dic1, **dic2, **dic3}
print(dicAll)


# ! remove dupilicate in string or list
list_remove_dup = [1,2,2,4,5,]
str_remove_dup = 'allisionmandy'
print(list(set(list_remove_dup)))
# still want return list 
print(set(str_remove_dup))



# todo => basic operation 