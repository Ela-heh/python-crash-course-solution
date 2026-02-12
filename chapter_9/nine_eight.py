class Privileges :
    def __init__ (self,privileges):

        self.privileges = privileges
    def show(self):
        print ("Admin privileges : ")
        for i in self.privileges:
            print(f"- {i}")

class User:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

class Admin(User):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

        self.privileges = Privileges([
            "can add post",
            "can delete post",
            "can ban user"
        ])

admin = Admin("Elaheh", "Farajzadeh")
admin.privileges.show()