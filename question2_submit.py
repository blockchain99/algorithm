"""
Question 2 :
Given a string a, find the longest palindromic substring contained in a. 
Your function definition should look like "question2(a)", and return a string.
"""

def question2(a):
    a = a.lower()
    def is_palindrome(a):   #returns T/F
        return str(a) == str(a)[::-1]
    
    longest_palindrome = ""

    i = 0
    j = 1

    #new value can't be longest palindrome if len(string[i:j]) <= len(longest palindrome)
    while i < (len(a) - len(longest_palindrome)):
        #don't look beyond the possible indexes
        if j <= len(a):
            temp_string = a[i:j]
            #only worth checking if it is eligible to be the longest 
            if len(temp_string) > len(longest_palindrome):
                if is_palindrome(temp_string) == True:
                    longest_palindrome = temp_string
            j += 1
        #move forward one place, start over
        else:
            i += 1
            j = i+1

    return longest_palindrome



print "test 1: ", question2("racecar")
# test 1:  racecar
print "test 2: ", question2("cumquat") 
# test 2:  c
print "test 3: ",question2("forgeeksskeegfor and the the results")
# test 3:  geeksskeeg
print "test 4: ",question2("I love banana and racec r and cumquat and all the other thing in all I geekskeegfor")
#test 4:  geekskeeg 