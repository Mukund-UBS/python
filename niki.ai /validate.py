"""
Python3

validate.py - When put inside a directory containing only text files, the script recursively traverses
through the entire directory and prints all the mobile numbers (base 10-digit format
Indian mobile numbers and its variations).

"""

import re, glob
def check(cfn):
    f=open(cfn)
    l=f.readlines()
    cond=re.compile(r'\+?(91|91\s)?([7-9][0-9]{9}$)')
    for i in l:
        m=cond.match(i)
        if m: print(m.group(2))

print("Valid Indian Numbers are:")
for filename in glob.iglob('./*.txt'):
    corrected_filename=filename[2:]
    check(corrected_filename)
