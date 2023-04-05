class User:
    def __init__(self):
        self.first_name = "ada"
        self.last_name = "Lovelace"
        self.email = "hzdkv@example.com"
        self.age = 30
print('Hello World!')

# class User:
#     def init(self, name, email, member_status=False, gold_card_points=0):
#         self.name = name
#         self.email = email
#         self.member_status = member_status
#         self.gold_card_points = gold_card_points

#     def display_info(self):
#         print("Name:", self.name)
#         print("Email:", self.email)
#         print("Member Status:", self.member_status)
#         print("Gold Card Points:", self.gold_card_points)

#     def enroll(self):
#         self.member_status = True
#         self.gold_card_points = 200

#     def spend_points(self, amount):
#         self.gold_card_points -= amount