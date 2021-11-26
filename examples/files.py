import glob
import os


readme_path = os.path.join('..', 'README.md')
f = open(readme_path)
try:
    for line in f:
        print(line, end='')
finally:
    f.close()

with open(readme_path) as f:
    for line in f:
        print(line, end='')


for path in glob.iglob(os.path.join('**', '*.py'), recursive=True):
    f = open(path)
    matched = False
    for line in f:
        if "import" in line:
            print(line, path)
            matched = True
            break
    if matched:
        break
