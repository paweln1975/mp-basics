with open("/home/centos/IdeaProjects/mp-basics.py/binary", "bw") as bin_file:
    bin_file.write(bytes(range(1, 17)))

with open("/home/centos/IdeaProjects/mp-basics.py/binary", "br") as bin_file:
    for b in bin_file:
        print(b)

a = 65534
b = 2993839

with open("/home/centos/IdeaProjects/mp-basics.py/binary", "bw") as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(4, 'big'))
    bin_file.write(b.to_bytes(4, 'little'))

with open("/home/centos/IdeaProjects/mp-basics.py/binary", "br") as bin_file:
    c = int.from_bytes(bin_file.read(2), 'big')
    print(c)
    d = int.from_bytes(bin_file.read(4), 'big')
    print(d)
    e = int.from_bytes(bin_file.read(4), 'little')
    print(e)



