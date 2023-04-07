class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points 
    
    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards member: {self.is_rewards_member}")
        print(f"Gold card points: {self.gold_card_points}")
    
    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True
    
    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("Insufficient gold card points.")
        else:
            self.gold_card_points -= amount


# Users
tiger_woods = User("Tiger", "Woods", "tigerwoods@example.com", 45)
jack_nicklaus = User("Jack", "Nicklaus", "jacknicklaus@example.com", 82)
arnold_palmer = User("Arnold", "Palmer", "arnoldpalmer@example.com", 87)

# Display info for each user
tiger_woods.display_info()
jack_nicklaus.display_info()
arnold_palmer.display_info()

# enroll and spend 50 points
tiger_woods.enroll()
tiger_woods.spend_points(50)

# enroll and spend 80 points
jack_nicklaus.enroll()
jack_nicklaus.spend_points(80)

# Try to spend 40 points (should result in an error)
arnold_palmer.spend_points(40)

# Display info for each user again
tiger_woods.display_info()
jack_nicklaus.display_info()
arnold_palmer.display_info()