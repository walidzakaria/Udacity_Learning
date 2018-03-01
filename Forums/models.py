class Member:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return  'name: {}\t\tAge: {}'.format(self.name, self.age)


class Post(Member):

    def __init__(self, subject, content, member):
        self.subject = subject
        self.content = content
        self.member = member
    def __str__(self):
        return 'member: {}\tage: {}\nsubject: {}\ncontent: {}' .format(self.member.name, self.member.age, self.subject, self.content)
