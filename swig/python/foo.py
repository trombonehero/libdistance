import cluster, string
from _distance import *

def ld(str1, str2):
    # d = levenshtein_d(str1, len(str1), str2, len(str2))
    d = damerau_d(str1, len(str1), str2, len(str2))
    return d

n = []
f = open("allfiles", "r")
for file in f.readlines():
    input = ""
    tmp = open(string.strip(file), "r")
    for line in tmp.readlines():
        input += line
    n.append(input)
    tmp.close()
f.close()

print cluster.make_groups(n, 2, ld, 1.8)
