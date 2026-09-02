from pymongo import MongoClient

# connection string
MONGODB_CONNECTION_URL = "mongodb://localhost:27017/"

client = MongoClient(MONGODB_CONNECTION_URL)

db = client["expense_tracker"]
collection_name = db["expense"]


# add expense
def add_expense(amount, category, type, description):
    expense = {
        "amount": amount,
        "category": category,
        "type": type,
        "description": description,
    }
    data = collection_name.insert_one(expense)
    # print(data)
    if data.acknowledged:
        print("Expense added successfully")


# main function
def main():
    while True:
        print("\n Expense tracker")
        print(
            "1. Add expense\n2. List expense\n3. Delete expense\n4. Update expense\n5. Exit"
        )
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                amount = int(input("Enter the ammount: "))
                category = input("Enter the category: ")
                type = input("Enter the type like incomming or outgoing: ")
                description = input("Enter the description: ")
                add_expense(amount, category, type, description)


if __name__ == "__main__":
    main()
