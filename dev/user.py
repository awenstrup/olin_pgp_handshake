class User:
    def __init__(self, uid, email, type, first, last, class_name):
        self.uid = uid
        self.email = email
        self.type = type
        self.first = first
        self.last = last
        self.class_name = class_name
    def __str__(self):
        line1 = 'Username: ' + self.uid + '\n'
        line2 = 'Name: ' + self.last + ', ' + self.first + '\n'
        line3 = 'Class: ' + self.class_name + '\n'
        return line1 + line2 + line3
