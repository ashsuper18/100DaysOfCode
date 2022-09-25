#
# * we usually give Class name is PascalCase
# class User:
#     def __init__(self):
#         print("hello")
# # object

# user_1 = User()
# # adding attribute
# user_1.username = "Ashish"
# user_1.id = "561"
# print(user_1.username)

# * one method to create different user but if there is more than one user then it will be difficult to write attribute for different user again and agin so below method is for attributes
# ***********************************************************
# creating attributes
# class User:
#     def __init__(self,username,id) :
#         self.username = username
#         self.id = id

# user1 = User("Ashish","561")
# print(user1.username)

# *************************************************************
# creating methods
class User:
    def __init__(self, username, id):
        self.username = username
        self.id = id
        self.followers = 0
        self.following = 0

    # Creating method ,method always need self parameter
    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("Ashish", "561")
user2 = User("okaif", "619")

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
