import itertools as it
from itertools import combinations
import sys
import argparse

def powerset(iterable):
    s = list(iterable)
    return it.chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def sumcut(cuts, setel):
    ""
    l=0
    if len( setel[0] )> 0 :
        for k in setel[0]:
            if( len(k)>0 ):
                l = l + cuts[k]

    return l
     
def buildAndFilterSets(cutsList, barList):
     
    ""
    S = list( powerset(cutsList) )
    
    ret = []
    
    for b in barList :
        el  = []
        for c in S :
            tmp = (c,b)

            l = sumcut(cutsList, tmp)

            if l<=barList[ b ] :
                el.append( tmp )       
    
        ret.append(el)

    U=list( it.product(*ret) )

    ret=[]
    
    for c in U :
        
        t = list( it.chain.from_iterable( [x[0] for x in c] ) )
        
        if len(t) == len( set(t) ) :
            if len(t) == len(cutsList) :
                e = 0
                for k in c :
                    l = sumcut(cutsList, k)
                    if l>0:
                        e = e + barList[ k[1] ] - l
                    
                ret.append([c,e])

    return ret




def main(file_):
    
    parser = argparse.ArgumentParser(description='Compute best bars cuts')

    parser.add_argument('-Cuts',
                        metavar='N',
                        type=float,
                        nargs='+',
                        help='Cut List')

    parser.add_argument('-Bars',
                        metavar='M',
                        type=float,
                        nargs='+',
                        help='Bar List')


    args = parser.parse_args()

    #start dict
    barre = {}
    k=0
    for i in args.Bars:
        
        barre['B' + str(k)] = i
        k=k+1
        
    
    tagli = {}
    k=0
    for i in args.Cuts: 
        tagli['T' + str(k)] = i
        k=k+1


    print ""
    print "Input Bars(ID: length):", barre
    print "Input Cuts(ID: length):", tagli
    print ""
    print "Cuts on bars:"

    
    TB = buildAndFilterSets(tagli, barre )

    if len(TB) > 0:
        out = min(TB, key=lambda x: x[1])
        
        #subset best cuts
        ls = [t for t in TB if t[1]<=out[1]]

        #heuristic: select the best
        u = [ [barre[l[1]]-sumcut(tagli,l) for l in k[0] ] for k in ls]
        h = [max(k)-min(k) for k in u]

        bestID = h.index(max(h))
        
        #print 'Best cut: ', ls[bestID][0], ' Tot. leftovers: ', ls[bestID][1]
        for x in ls[bestID][0]:
            print 'Bar:', x[1], '(',barre[x[1]], ')', ' Cuts', x[0]

        print 'Total waste: ', ls[bestID][1]
        out = ls[bestID]

    else:
	print 'No cuts found'


if __name__ == '__main__':
    main( sys.argv[1] )
