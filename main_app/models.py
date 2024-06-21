
# from . import Client

# class Portfolio:
#     id = db.Column(int, primary_key=True)
    
#     def __init__(self, client: Client):
#         self.db = client.get_db()
#         self.collection = self.db["Portfolio"]

#     def add_portfolio(self, user_id):
#         self.collection.insert_one({"user_id": user_id,
#                                     "assets": []})

# class User:
#     id = db.Column(int, primary_key=True)
#     username = db.Column(str, unique=True, nullable=False)
#     wallet = db.Column(str, unique=True, nullable=False)
#     balance_RCoin = db.Column(int, default=0, nullable=False)
#     user_id_telegram = db.Column(int, unique=True, nullable=False)

#     def add_user(self):
#         self.user = self.collection.insert_one({"username": self.username, 
#                                     "balance_RCoin": self.balance_RCoin,
#                                     "wallet": self.wallet, 
#                                     "user_id_telegram": self.user_id_telegram})
        
#         self.portfolio = Portfolio(self.db).add_portfolio(self.user.inserted_id)