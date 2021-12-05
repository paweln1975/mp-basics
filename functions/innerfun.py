def spam1():

    def spam2():

        def spam3():
            z = " even"
            z += y
            print("spam3() locals {}".format(locals()))
            return z

        y = " more"
        y += x
        y += spam3()
        print("spam2() locals {}".format(locals()))
        return y

    x = " spam"    # x must exists before spam2() is called
    x += spam2()
    print("spam1() locals {}".format(locals()))
    return x


print(spam1())
print(locals())
print(globals())



