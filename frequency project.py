string_data = input("enter any word: ")

d={}
for alphabet in string_data:
    d[alphabet]=d.get(alphabet,0)+1
    

for key,value in d.items():
    print(key,"=",value)
