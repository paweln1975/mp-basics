with open("/home/centos/IdeaProjects/mp-basics.py/io/output.txt", "a") as output_file:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{0:>2} times {1:>2} is {2}".format(i, j,  i * j), file=output_file)
        print("-" * 20, file=output_file)
