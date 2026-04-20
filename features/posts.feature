Feature: Posts API
  As a QA engineer
  I want to validate the Posts API
  So that I can ensure correct behavior

  Scenario: Get all posts
    Given the API is available
    When I request all posts
    Then the response status should be 200
    And the response should contain a list of posts

  Scenario: Get a single post
    Given the API is available
    When I request post with id 1
    Then the response status should be 200
    And the post should have a title and body

  Scenario: Create a new post
    Given the API is available
    When I create a post with title "BDD Test Post" and body "Created with Behave"
    Then the response status should be 201
    And the created post should have the same title

  Scenario Outline: Get multiple posts by id
    Given the API is available
    When I request post with id <post_id>
    Then the response status should be 200

    Examples:
      | post_id |
      | 1       |
      | 5       |
      | 10      |
