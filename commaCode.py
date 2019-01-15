#Function
def commaCode (unaLista):
    listLength = len(unaLista)
    for i in range (0, listLength):
        if ((i + 1) == listLength):
            print('and ', end = '')
        print(str(unaLista[i]), end = '')
        if ((i + 1) != listLength):
            print(', ', end = '')
    print()
#Variables
list = []
item = 'more'
#Main
print('Welcome to the list generator!') 
print('List an item then press enter: ')
print('Type "done" to submit your list.')
while(item != 'done'):    
    item = input()
    list.append(item)
list.remove('done')
commaCode(list)
