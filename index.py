prompt = input("Enter the file name you wish to open: ")

data = ""

try:
    with open(prompt, "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found. Please check the file Name.")
else:
    modifyData = data.upper()
    modify_txt= "modified_" + prompt 

with open("modify.txt", "w") as file:
    file.write(modifyData)
    print(data)

