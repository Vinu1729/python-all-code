import operator

list1=[10,20,30,40,50]
list2=[60,70,80,90]
#checking of properties
print("list1 conatains 10",operator.contains(list1,10))
print("list1 conatains 10",operator.contains(list1,100))
#addition
print("\naddition os 10 and 20",operator.add(10,20))
#concat
list3=operator.concat(list1,list2)
print("\nafter concatting the lists",list3)