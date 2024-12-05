List = ["Apple" , "Mango" , "Banana" , "Kiwi" , "Guava"]

print("The length of List is :", len(List))
print("The first Term of the List is", List[0])
print("The last term of the list is" ,List[-1])

List.append("Papaya")
print("The updated list is" , List)

List.remove("Guava")
print("The updated list is" , List)

List.sort()
print("The sorted list is" , List)

List.pop(1)
print(List)

List.reverse()
print("The reversed list is ", List)

print("Multiplication on list", List*2)

List = List[:4]
print("Sliced list is", List)

List.clear()
print("The cleared list is ", List)




my_dict = {}
my_dict = {1: 'Apple' , 2: 'Banana'}

my_dict = {'name': 'Ranveer' , 'Age': 13 , }

print(my_dict['name'])
print(my_dict.get('Age'))

my_dict['Age'] = 14
print(my_dict)

my_dict['address'] =  'Croydon'
print(my_dict)

my_dict.pop('Age')
print(my_dict)

print(my_dict.get('address'))
