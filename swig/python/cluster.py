from _distance import *

# http://en.wikipedia.org/wiki/Binary_search_tree

def hier_cluster(nodes, dist_fn):
    """takes lists of lists of nodes to run hierarchical clustering on evaluating 
       them all pairwise using the distance function dist_fn. 

       prototype of dfn: dfn(node1, node2)
       dfn should return a distance value (int, float)

       returns a list of clusters as a list of lists."""

    if len(nodes) == 0:
        return None
    elif len(nodes) == 1:
        return nodes[0][0]

    tmp = []
    for n in nodes:
        for t in n:
            tmp.append(t)
    nodes = tmp

    """build a 0 half matrix ..."""
    d = [[0]]
    for i in xrange(1, len(nodes)):
        l = [0, 0]
        for j in xrange(1, i):
            l.append(0)
        d.append(l)

    """calculate the internode distances"""
    for i in xrange(0, len(nodes)):
        for j in xrange(0, i):
            if i == j:
                dist = 0
            else:
                dist = apply(dist_fn, (nodes[i], nodes[j]))
            d[i][j] = dist

    nodes_remaining = len(nodes)
    while nodes_remaining > 1:
        dist_min = 99999
        min_i = -1
        min_j = -1

        for i in xrange(0, len(nodes)):
            for j in xrange(0, i):
                try:
                    tmp = d[i][j]
                except IndexError:
                    continue
                dist = d[i][j]
                if dist < dist_min:
                    dist_min = dist
                    min_i = i
                    min_j = j

        """debug"""
        print "nodes_remaining: %d, dist_min: %d, min_i: %d, min_j: %d" % (nodes_remaining, dist_min, min_i, min_j)
        nodes_remaining -= 1

    # XXX
    results = []
    for n in nodes:
        t = []
        t.append(n)
        results.append(t)
    return results

def hier_get_sliceheight(results, zval):
    pass

def make_groups(nodes, npasses, dist_fn, zval):
    """takes a list of nodes to run hierarchical clustering on evaluating 
       them all pairwise for npasses using the distance function dist_fn.

       results is a list of lists of strings.

       zval is the slice height, ie num of std deviations from root.

       prototype of the distance function: dist_fn(str1, str2), should return 
       a distance (int or float) between the two strings.

    returns a list of lists of clusters."""

    results = []
    for n in nodes:
        tmp = []
        tmp.append(n)
        results.append(tmp)

    for i in xrange(0, npasses):
        results = hier_cluster(results, dist_fn)
        print "results:", results

        if npasses:
            height = hier_get_sliceheight(results, 0.0)
        else:
            height = hier_get_sliceheight(results, zval)

    return results
