import uuid

def user_input(execution_id):
    print("USER INPUT \n")
    user_name = input("User Name: ")
    user_email = input("User Email: ")
    user_age = int(input("User Age: "))
    user_gender = input("User Gender: ")
    user_id = uuid.uuid4()

    return user_id, user_name, user_email, user_age, user_gender



