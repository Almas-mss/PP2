with open("file2.txt","r") as file:
    content = file.read()
    print(content)
with open("file_to_copy","w") as file:
    file.write(content)