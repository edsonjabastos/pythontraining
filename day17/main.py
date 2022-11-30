class User:
    def __init__(self, user_id, username):
        print("New use being created... ")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


def nothing():
    pass


user_1 = User('001', 'daq_naipão')
# user_1.id = '001'
# user_1.username = 'daq_naipão'

# user_2 = User()
user_2 = User('002', 'daq_naipasso')
# user_2.id = '002'
# user_2.username = 'daq_naipasso'
user_1.follow(user_2)
print(user_2.id, user_2.username, user_2.followers, user_2.following)
print(user_1.id, user_1.username, user_1.followers, user_1.following)
