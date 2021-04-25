import os

# List all files in a directory using os.listdir
print(os.getcwd())
basepath = '/'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)

with os.scandir('/') as entries:
    for entry in entries:
        print(entry.name)