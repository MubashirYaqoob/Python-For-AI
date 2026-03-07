with open("pr.txt","r") as f :
    data = f.read()

new_data = data.replace("java","python")
print(new_data)

with open("pr.txt","w") as f :
    data = f.write()