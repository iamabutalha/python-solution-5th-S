
file = open("data.txt", "w")
file.write("Hello python")
file.close()

file = open("data.txt", "r")
print(file.read())
file.close()