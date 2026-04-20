Feature: Users API
  As a QA engineer
  I want to validate the Users API
  So that I can ensure data integrity

  Scenario: Get all users
    Given the API is available
    When I request all users
    Then the response status should be 200
    And the response should return 10 users

  Scenario: Get user by id
    Given the API is available
    When I request user with id 1
    Then the response status should be 200
    And the user should have name, email and username

  Scenario: User not found
    Given the API is available
    When I request user with id 9999
    Then the response status should be 404
