from behave import when, then
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@when("I request all users")
def step_get_all_users(context):
    context.response = requests.get(f"{context.base_url}/users")

@when("I request user with id {user_id:d}")
def step_get_user_by_id(context, user_id):
    context.response = requests.get(f"{context.base_url}/users/{user_id}")

@then("the response should return 10 users")
def step_check_10_users(context):
    assert len(context.response.json()) == 10

@then("the user should have name, email and username")
def step_check_user_fields(context):
    data = context.response.json()
    for field in ["name", "email", "username"]:
        assert field in data, f"Missing field: {field}"
