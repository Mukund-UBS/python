import glob
for filename in glob.iglob('./*.txt'):
    corrected_filename=filename[2:]
    print(corrected_filename)
