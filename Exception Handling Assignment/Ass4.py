class KeyNotInListException(Exception):
    pass

def add_to_list_in_dict(d,listname, elements):
    try:
        key = d.keys()
        if listname not in key:
            raise KeyNotInListException()
    except KeyNotInListException as e:
        d.update({listname:elements})
    else:
        print(listname, d[listname])
    finally:
        print(d)





d = { 'names' : ['Harshal, Vedant, Akshay'], 'roll_nos' : [10, 5, 12]}
listname = input('Enter listname: ')
elements = ['Amrutkar', 'Bhosale', 'Funde']
add_to_list_in_dict(d,listname, elements)