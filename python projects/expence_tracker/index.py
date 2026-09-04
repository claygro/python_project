from pymongo import MongoClient
from pymongo.errors import PyMongoError
from tabulate import tabulate
from bson import ObjectId



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


# list expense
def list_expense():
    table = []

    try:
        response = collection_name.find()
        for expense in response:
            table.append(
                [
                    str(expense["_id"]),
                    expense["amount"],
                    expense["category"],
                    expense["type"],
                    expense["description"],
                ]
            )

        (table.sort(reverse=True),)
        print(
            tabulate(
                table,
                headers=["ID", "Amount", "Category", "Type", "Description"],
                tablefmt="rounded_outline",
            )
        )

    except PyMongoError as e:
        print(f"Failed to list the expense: {e}")


# delete expense
def delete_expense(expense_id):
    try:
        data = collection_name.delete_one({"_id": ObjectId(expense_id)})
        if data.acknowledged:
            print("Delete successfully")
        else:
            print("No expense found or invalid expense id")
    except PyMongoError as e:
        print(f"Failed to delete expense: {e}")


# update expense
def update_expense(expense_id, amount, category, type, description):
    try:
        newUpdateData = {}

        if amount and amount != "":
            newUpdateData["amount"] = amount

        if category and category != "":
            newUpdateData["category"] = category

        if type and type != "":
            newUpdateData["type"] = type
        if description and description != "":
            newUpdateData["description"] = description

        data = collection_name.update_one(
            {"_id": ObjectId(expense_id)}, {"$set": newUpdateData}
        )
        print(data)
    except PyMongoError as e:
        print(f"Failed to delete expense: {e}")


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
            case "2":
                list_expense()
            case "3":
                list_expense()
                expense_id = input("Enter the Id you want to delete: ")
                delete_expense(expense_id)
            case "4":
                list_expense()
                expense_id = input("Enter the id you want to update: ")
                amount = input("Enter the ammount: ")
                category = input("Enter the category: ")
                type = input("Enter the type like incomming or outgoing: ")
                description = input("Enter the description: ")
                update_expense(expense_id, amount, category, type, description)
            case "5":
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
