# from http://stackoverflow.com/questions/5369723/multi-level-defaultdict-with-variable-depth-in-python

from collections import defaultdict

l=lambda:defaultdict(l)
table=l()

table[0][1][2][3][4][5]=6


