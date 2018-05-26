mport sys
class Solution:
    def __init__(self):
        self.t = []
        self.q = []
        self.x = []
        self.i = 1
    def pushCharacter(self, ch):
        self.t.append(ch)
       
    def enqueueCharacter(self, ch):
        self.q.append(ch)
      
    def popCharacter(self):
        return self.t.pop()
    
    def dequeueCharacter(self):
        if self.i == 1:
            self.x = self.q
            self.x.reverse()
            self.i+=1
            return self.x.pop()
        else:
            return self.x.pop()
            
            
            
 if __init__ = '__main__':
    # read the string s
    s=input()
    #Create the Solution class object
    obj=Solution()   

    l=len(s)
    # push/enqueue all the characters of string s to stack
    for i in range(l):
        obj.pushCharacter(s[i])
        obj.enqueueCharacter(s[i])
    
    isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
    for i in range(l // 2):
         if obj.popCharacter()!=obj.dequeueCharacter():
            isPalindrome=False
            break
#finally print whether string s is palindrome or not.
    if isPalindrome:
        print("The word, "+s+", is a palindrome.")
    else:
        print("The word, "+s+", is not a palindrome.")    
