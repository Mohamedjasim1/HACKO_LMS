

class Authentication:
    def __init__(self):
        pass

    def authenticate(self, stu_email):
        if(stu_email in database): #assuming database is in list format
            return True
        else:
            return False


if __name__ == "__main__":
    obj = Authentication()
    print(obj.authenticate("jo123@gmail.com"))
