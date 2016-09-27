# Cutting-stock-problem
Simple brute force optimal solution for 1D problem

Heurystics at lower level only to select a solution in min waste optimal solution set
that preserve bars and apply maximal number of cuts on a single element.

Needs: python standard library

Limits: since combinatorial explosion of the brute force approach 
it works on a limited set of bars / cuts of the order of a dozen.

usage:
$ python linearCut.py -Bars 8 5 3 -Cuts 6 3 2

Input Bars(ID: length): {'B0': 8.0, 'B1': 5.0, 'B2': 3.0}
Input Cuts(ID: length): {'T2': 2.0, 'T0': 6.0, 'T1': 3.0}

Cuts on bars:
Bar: B0 ( 8.0 )  Cuts ('T2', 'T0')
Bar: B1 ( 5.0 )  Cuts ()
Bar: B2 ( 3.0 )  Cuts ('T1',
Total waste:  0.0

where Cuts () stay for no cut on bar B1 in this case.

