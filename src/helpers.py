import requests

BASE_URL = "http://jsonplaceholder.typicode.com"


def is_fancode_city(lat, lng):
    """
    Check if the user's coordinates fall within the FanCode city limits.
    """
    lat_cond = -40 < float(lat) < 5
    lng_cond = 5 < float(lng) < 100

    # Returns True when both conditions are valid else False
    return lat_cond and lng_cond


def get_users():
    """
    Fetch all users from the API.
    Returns a list of user data.
    """
    response = requests.get(f"{BASE_URL}/users")
    response.raise_for_status()
    return response.json()

def get_todos(user_id):
    """
    Fetch to-do tasks for a specific user by user ID.
    Returns a list of to-do tasks.
    """
    response = requests.get(f"{BASE_URL}/todos", params={'userId': user_id})
    response.raise_for_status()
    return response.json()

def calculate_task_completion(todos):
    """
    Calculate the percentage of completed tasks for a user.
    Returns the completion percentage as a float.
    """
    total_tasks = len(todos)
    completed_tasks = len([task for task in todos if task['completed']])

    if total_tasks == 0:
        return 0
    return (completed_tasks / total_tasks) * 100
