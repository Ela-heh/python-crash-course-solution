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


user = User('ela','farajzadeh')
user.increment()
user.reset()
user.increment()
user.increment()
user.reset()