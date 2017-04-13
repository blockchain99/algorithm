def Question1(s, t):
    s_length = len(s)
    print "*s_length:",s_length
    t_length = len(t)
    print "*t_length:",t_length
    
    print "*range :",s_length - t_length + 1
    for i in range(s_length - t_length + 1): #7-2+1=6
        print "*i:",i
        print (s[i: i+t_length], t)
        if sorted(s[i: i+t_length])==sorted(t): #ex. t='ad'(2), s[0:2]==t, x[1,3]==t, x[2,4]==t,x[3,5]==t,x[4,6]==t,x[5,7]==t
            return True
    return False


print 'Test result : udacity, ad \n',Question1("udacity", "ad")
print 'Test result : udacity, tyciuda \n',Question1("udacity", "tyciuda")