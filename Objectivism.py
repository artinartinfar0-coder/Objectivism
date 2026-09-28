class User:
    def __init__(self,user_name,pass_word,full_name):
        self.user_name = user_name
        self.pass_word = pass_word
        self.full_name = full_name
    def p(self):
        print(self.user_name, self.pass_word,self.full_name)

u1 = User("Mark_2008",'848fs8',"Mark Grayson")
u2 = User("Jimmy_88","ffs4545","Jimmy wilsone")
# Finished.Now We Can Call Them
#For Example We Can Call u1
u1.p()