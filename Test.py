from Graph import createSubpath, createCircuit

#========== Main ============
eulerGraph = ['1 9',
         '9 6',
         '6 1',
         '2 4',
         '3 2',
         '3 4',
         '5 8',
         '8 7',
         '7 5',
         '1 2',
         '2 8',
         '8 1']

nonEulerGraph = ['7 5','1 9',
         '9 6',
         '6 1',
         '2 4',
         '3 2',
         '5 8',
         '8 7',
         '3 4']

edgesNumber = ['0 1', '3 4', '2 1', '0 4', '2 3','4 1', '0 2', '1 4', '0 3', '3 2']


print(createSubpath(nonEulerGraph))