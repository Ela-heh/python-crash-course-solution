class User:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.login_attempt = 0

    def increment(self):
        self.login_attempt += 1
        print (f"{self.fname.title()} {self.lname.title()} has tried {self.login_attempt} time !")


    def reset(self):
        self.login_attempt = 0
        print(f"attempts has been reset to {self.login_attempt}")

class Admin(User):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
 
    def privileges (self):
        show = ['can add post' , 'can add user','can ban user','cn delete post']
        return show

admin=Admin("ela" , "fj")
print (f"admin is {admin.fname.title()} and she has {admin.privileges()} privileges")