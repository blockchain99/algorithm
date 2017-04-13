def Question1(s, t):
    s_length = len(s)
#     print "*s_length:",s_length
    t_length = len(t)
#     print "*t_length:",t_length
    
#     print "*range :",s_length - t_length + 1
    for i in range(s_length - t_length + 1): #7-2+1=6
#         print "*i:",i
#         print (s[i: i+t_length], t)
        if sorted(s[i: i+t_length])==sorted(t): #ex. t='ad'(2), s[0:2]==t, x[1,3]==t, x[2,4]==t,x[3,5]==t,x[4,6]==t,x[5,7]==t
            return True
    return False


print 'Test 1 : udacity, ad \n',Question1("udacity", "ad")
#Test 1 : udacity, ad 
# True
print 'Test 2 : udacity, tyciuda \n',Question1("udacity", "tyciuda")
# Test 2 : udacity, tyciuda 
# True
print 'Test 3 : timeline, k s \n',Question1("timelne", "k s")
# Test 3 : timeline, k s 
# False
print 'Test 4 : butterfly, a rl \n',Question1("butterfly", "a r")
# Test 4 : butterfly, a rl 
# False


