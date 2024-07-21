f = open('example11.txt', 'w')
f.write("Hello, World!\n")
f.write("This is example file.\n")
f.write("Python file handling is easy!")

f = open('example11.txt', 'r')
content = f.read()
print("File Content:")
print(content)