# BDD Tests with Behave

BDD test suite using Behave and Gherkin syntax — human-readable scenarios with Given/When/Then for API testing.

## Stack

| Tool | Purpose |
|------|---------|
| Behave | BDD test framework |
| Gherkin | Human-readable test scenarios |
| Requests | HTTP client |
| GitHub Actions | CI/CD |

## Structure

```
bdd-behave-tests/
├── features/
│   ├── posts.feature       # Post scenarios
│   ├── users.feature       # User scenarios
│   └── steps/
│       ├── posts_steps.py  # Step definitions for posts
│       └── users_steps.py  # Step definitions for users
└── requirements.txt
```

## Run locally

```bash
pip install -r requirements.txt
behave
```
