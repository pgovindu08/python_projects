class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def unfollow(self, user):
        user.followers -= 1
        self.following -= 1

user_1 = User("001", "Pranav")
user_2 = User("002", "John")

user_1.follow(user_2)
user_2.follow(user_1)

print(f"User 1 followers: {user_1.followers}")
print(f"User 2 followers: {user_2.followers}")
print(f"User 1 following: {user_1.following}")
print(f"User 2 following: {user_2.following}")

