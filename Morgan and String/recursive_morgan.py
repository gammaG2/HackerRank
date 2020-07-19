def morganAndString_v2(a, b,result=''):
    if len(a)==0:
        return result+b
    if len(b) == 0:
        return result+a
    
    if(a[:1]==b[:1]):
        result = result + min(morganAndString(a[1:], b,a[:1]),morganAndString(a, b[1:],b[:1]))
        return result
        
    if (a[:1]<b[:1]):
        return morganAndString(a[1:], b,result+a[:1])
    else:
        return morganAndString(a, b[1:],result+b[:1])