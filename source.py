import json

# read a file

file = open('example.json', 'r')
Data = file.read()


#Parse
obj = json.loads(Data)

#print(str(obj['name']))
#print(str(obj['Hobbies']))



print("Name:", str(obj['name']))
print("Is a Programmer:", str(obj['isProgrammer']))
#print(str(obj['friends']))

list = obj['friends']

for i in range(len(list)):
    print("Is a Programmer:", i, "is.....")
    print("Hobbies:", list[i].get('Hobbies'))
    print("name:", list[i].get('name'))
    print("favourite Numebr:", list[i].get('favouriteNumber'))
