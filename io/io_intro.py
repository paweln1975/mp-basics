def sep():
    print()
    print("*" * 80)

# reading text file
try:
    jabber = open("/home/centos/IdeaProjects/mp-basics/io/sample.txt", mode='r')

    for line in jabber:
        print(line, end="")

except FileNotFoundError:
    print("File not found")
else:
    sep()
    print("File closed")
    jabber.close()

# no need to close file when using "with"
with open("/home/centos/IdeaProjects/mp-basics/io/sample.txt", mode='r') as jabber:
    for line in jabber:
        if "Jabberwock" in line:
            print("Found Jabberwock")

sep()

# using readline()
with open("/home/centos/IdeaProjects/mp-basics/io/sample.txt", mode='r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end="")
        line = jabber.readline()

sep()

# using readlines()
with open("/home/centos/IdeaProjects/mp-basics/io/sample.txt", mode='r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines:
    print(line, end="")

sep()

# using read and displaying backwards
with open("/home/centos/IdeaProjects/mp-basics/io/sample.txt", mode='r') as jabber:
    lines=jabber.read()

for line in lines[::-1]:
    print(line, end="")

