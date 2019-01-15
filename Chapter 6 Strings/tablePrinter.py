#! python3
# tablePrinter.py
# Mackenzie Weaver 12/11/2018 macknz7@gmail.com
# Display a list of lists of strings in a well-organized way
def printTable(listOfLists):
    # list variable stores longest string in each list
    colWidths = [0] * len(listOfLists)
    # finds longest string in each list
    for i in range(len(listOfLists)):
        for j in range(len(listOfLists[i])):
            if len(listOfLists[i][j]) > colWidths[i]:
                colWidths[i] = len(listOfLists[i][j])
    # finds longest string of the lists
    justify = 0
    for k in range(len(colWidths)):
        if colWidths[k] > justify:
            justify = colWidths[k]
    # prints table
    for r in range(len(listOfLists[0])): # assume all lists are of the same length
        for t in range(len(listOfLists)):
            print(listOfLists[t][r].rjust(justify), end = '')
        print()
# example list of lists
tableData = [   ['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']]
# function call
printTable(tableData)
