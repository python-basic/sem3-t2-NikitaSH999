#Реализуйте работу функции zip() через map()

list1=[9,8,7,6,5]
list2=[1,2,3,4,5]

print(list(zip(list1,list2)))
print(list(map(lambda x,y: (x,y), list1,list2)))