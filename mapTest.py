def fun(str):
    i= 0
    s=''
    while i < len(str):
        if i == 0:
            s+=str[i].upper()
        else:
            s+=str[i].lower()
        i+=1
    print s
fun('dssds')
map(fun,['adam', 'LISA', 'barT'])