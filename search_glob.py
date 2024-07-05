import glob

#Searches for all that end in .txt
files = glob.glob('*.txt')
for file in files:
    print(file)
