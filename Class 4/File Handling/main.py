# WRITING TO A FILE
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()

# READING FROM A FILE
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# APPENDING TO A FILE
file = open("example.txt", "a")
file.write("Hello, World!")
file.close()



