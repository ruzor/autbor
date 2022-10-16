print('Please enter space seperated values...')
listItems = input().split()

def lTS(listItems):
    try:
        print(', '.join(listItems[:-1]) + ', and ' + listItems[-1])
    except IndexError:
        print('Please enter comma seperated values', end='\n')

lTS(listItems)