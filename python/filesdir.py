import os


def list_directories(s):

    def dir_list(d):
        nonlocal tab_stop
        try:
            files = os.listdir(d)
        except PermissionError:
            print("Permission denied to " + d)
            files = []

        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)

    tab_stop = 0
    if os.path.exists(s):
        print("Directory listing of " + s)
        dir_list(s)
    else:
        print(s + " does not exist")


list_directories('/home')
