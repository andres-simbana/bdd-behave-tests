from behave import given, when, then
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@given("the API is available")
def step_api_available(context):
    context.base_url = BASE_URL

@when("I request all posts")
def step_get_all_posts(context):
    context.response = requests.get(f"{context.base_url}/posts")

@when("I request post with id {post_id:d}")
def step_get_post_by_id(context, post_id):
    context.response = requests.get(f"{context.base_url}/posts/{post_id}")

@when('I create a post with title "{title}" and body "{body}"')
def step_create_post(context, title, body):
    context.title = title
    context.response = requests.post(
        f"{context.base_url}/posts",
        json={"title": title, "body": body, "userId": 1}
    )

@then("the response status should be {status_code:d}")
def step_check_status(context, status_code):
    assert context.response.status_code == status_code, \
        f"Expected {status_code}, got {context.response.status_code}"

@then("the response should contain a list of posts")
def step_check_posts_list(context):
    data = context.response.json()
    assert isinstance(data, list)
    assert len(data) > 0

@then("the post should have a title and body")
def step_check_post_fields(context):
    data = context.response.json()
    assert "title" in data
    assert "body" in data

@then("the created post should have the same title")
def step_check_created_title(context):
    data = context.response.json()
    assert data["title"] == context.title
