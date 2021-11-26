f = open('README.md')
try:
    for line in f:
        print(line, end='')
finally:
    f.close()

with open('README.md') as f:
    for line in f:
        print(line, end='')