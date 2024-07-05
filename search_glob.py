import glob

files = glob.glob('*.txt')
for file in files:
    print(file)