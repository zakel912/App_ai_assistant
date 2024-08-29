from database.user_handler import insert_user, find_user_by_name, update_user, delete_user
from utils.user_info_parser import extract_user_info
from utils.parser_tools import extract_fields, creation_check_missing_info, deletion_check_missing_info

# Work as the API which create an account
def create_account(user_info):
    user_id = insert_user(user_info)
    return f"Account created for {user_info['first_name']} {user_info['last_name']}, age {user_info['age']}. User ID: {user_id}"

def create_account_tool(user_message):
    user_info = extract_fields(user_message)
    if (creation_check_missing_info(user_info)):
        missing_fields_formatted = ', '.join(creation_check_missing_info(user_info))
        return (f"I still need the following information to create your account: {missing_fields_formatted}. Please provide it.")
    return create_account(user_info)
    
# Work as the API which delete an account
def delete_account(first_name, last_name, password):
    deleted_count = delete_user(first_name, last_name, password)
    if deleted_count > 0:
        return "User deleted successfully."
    else:
        return "User not found."
    
def delete_account_tool(user_message):
    user_info = extract_fields(user_message)
    first_name = user_info.get('first_name')
    last_name = user_info.get('last_name')
    password = user_info.get('password')
    user = find_user_by_name(first_name, last_name)
    verified_password = user['password']
    if verified_password == password :
        if (deletion_check_missing_info(user_info)):
            missing_fields_formatted = ', '.join(deletion_check_missing_info(user_info))
            return (f"I still need the following information to create your account: {missing_fields_formatted}. Please provide it.")
        else:
            return delete_account(first_name, last_name, password)
    else :
        return "Incorrect password, please check that you have entered your information and password correctly."
        

# Read User's Credentials
def read_account(user_message):
    user_info = extract_user_info(user_message)
    first_name = user_info.get('first_name')
    last_name = user_info.get('last_name')
    
    user = find_user_by_name(first_name, last_name)
    if user:
        return f"User found: Name: {user['first_name']} {user['last_name']}, Gender: {user['gender']}"
    else:
        return "User not found."

# Upadte User's Credentials
def update_account(user_message, update_message):
    name = extract_user_info(user_message)
    first_name = name.get('first_name')
    last_name = name.get('last_name')
    update_fields = extract_user_info(update_message)
    modified_count = update_user(first_name, last_name, update_fields)
    if modified_count > 0:
        return "User updated successfully."
    else:
        return "User not found or no changes made."
