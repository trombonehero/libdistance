#!/usr/local/bin/python 

import string

from _distance import *

f = open("/home/jose/work/allsubjects", "r")
subjects = f.readlines()
f.close()

l = open("LD-subjects.out", "w")
d = open("DD-subjects.out", "w")

for i in xrange(0,len(subjects)):
    for j in xrange(0,len(subjects)):
        str1 = subjects[i]
        str2 = subjects[j]
        l.write("%d:%d:%d\n" % (i, j, (levenshtein_d(str1, len(str1), str2, len(str2)))))
        d.write("%d:%d:%d\n" % (i, j, (damerau_d(str1, len(str1), str2, len(str2)))))

l.close()
d.close()
