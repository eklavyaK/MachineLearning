import os

path = os.getcwd()  # gets the current working directory
print(path)

print(os.listdir(path)) # lists the files and folders present in the location

f = open('testfile.txt', 'w')
f.write("at the stroke of the midnight when the world sleeps, India will awake for life and freedom\n")
f.write("this was a famous speech given by Pt. Jawaharlal Nehru on the independence of india\n")
f.write("it is very iconic speech, which many indians remember to this date, and that's why I'm talking about it now\n")

f.seek(0) # moves the cursor to the begining of the file
f.write("Let me tell you about a iconic speech\n")
f.close()
f = open('testfile.txt', 'r')
contents = f.read()  # whole file is contained inside a string
print(contents)

f.seek(0) # f.read() has placed the cursor to the end of the the file
contents = f.readline()
print(contents)

f.seek(0)
contents = f.readlines() # it makes a list of the lines in the file
for i in contents: 
	print(i)