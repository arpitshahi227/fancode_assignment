import helpers

def check_fancode_users_task_completion():
    """
    Main function to check task completion for users in FanCode.
    Fetches users and their to-dos, calculates completion percentage,
    and prints the results.
    """
    users = helpers.get_users()  # Fetch all users
    fancode_users = [user for user in users if helpers.is_fancode_city(user['address']['geo']['lat'], user['address']['geo']['lng'])]

    for user in fancode_users:
        todos = helpers.get_todos(user['id'])  # Fetch todos for each user
        completion_percentage = helpers.calculate_task_completion(todos)

        if completion_percentage > 50:
            print(f"User {user['name']} has completed {completion_percentage:.2f}% of their tasks.")
        else:
            print(f"User {user['name']} has NOT completed more than 50% of their tasks.")

if __name__ == "__main__":
    check_fancode_users_task_completion()  # Run the main function
