class Student:
    def __init__(self, sname, susn, squali, saddr):
        self.name = sname
        self.usn = susn
        self.quali = squali
        self.address = saddr

s1 = Student("rama", "1VTUCS10", "CSE" , "Bang")
s2 = Student("sita", "1VTUCS15", "CSE" , "Mys")
s3 = Student("rama", "1VTUCS30", "CSE" , "Delhi")

print(s1.address)
print(s2.quali)
print(s3.usn)

