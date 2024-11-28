from datetime import datetime
# put your python code here
h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())


def time_diff(h2, m2, s2, h1, m1, s1):
    start = str(h1) + ":" + str(m1) + ":" + str(s1)
    end = str(h2) + ":" + str(m2) + ":" + str(s2)

    time1 = datetime.strptime(start, "%H:%M:%S")
    time2 = datetime.strptime(end, "%H:%M:%S")

    return int((time2 - time1).total_seconds())


print(time_diff(h2, m2, s2, h1, m1, s1))