name = { 'baby' : 'vedant', 'babu' :'shivam' , 'bachi' : 'akshara' }

def addDic () :
    print ('do you want to add more items')
    var1 = input()
    if var1.lower() == 'y' :
        print ('insert key')
        var_k = input()
        print ('insert value')
        var_v = input()
        name[var_k] = var_v
        print ('itmes added')
        return name
    else :
        print ('do nothing')

def prntitem (name) :
    for k,v in name.items() :
        print (k + ' ' + v)
        continue
for r in range (100) :
    name = addDic ()
    prntitem(name)
    break
