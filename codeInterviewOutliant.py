import random


class Database:
    def __init__(self):
        self.customers = {}


class CustomerObject:
    def __init__(self, customer_dict):
        self.id = customer_dict['id']
        self.name = customer_dict['name']
        self.account_balance = customer_dict['account_balance']

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "account_balance": self.account_balance,
        }


def generate_fake_database():
    database = Database()
    for i in range(10):
        customer_dict = {
            "id": i,
            "name": "Example Name",
            "account_balance": random.randint(1, 100),
        }
        database.customers[i] = CustomerObject(customer_dict)
    return database


class Application:
    def __init__(self):
        self.database = generate_fake_database()

    def get_customer_by_id(self, customer_id):
        # TODO: return the matching customer object
        if customer_id in self.database.customers:
            return self.database.customers[customer_id]

    def get_top_n_customers_by_account_balance(self, n):
        # Return n customers sorted from highest to lowest based on their account_balance

        return sorted(self.database.customers.values(
        ), key=lambda balance: balance.account_balance, reverse=True)[:n]


app = Application()

# 1. Customer to dict
print("Customer to dict:", app.database.customers[0].to_dict())

# 2. Customer By Id
print("Customer by id:", app.get_customer_by_id(4).to_dict())

#print([i.to_dict() for i in app.get_top_n_customers_by_account_balance(5)])
print("Top 5 Customer balance:",
      app.get_top_n_customers_by_account_balance(5))
