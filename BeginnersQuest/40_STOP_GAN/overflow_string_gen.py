from sys import stdout

for i in range(10):
    for j in range(10):
        for k in range(10):
            stdout.write("{}".format(k))
            stdout.flush()
print()
