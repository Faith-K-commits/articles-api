# Articles API Project

## Overview

This is a Django-based RESTful API that allows users to perform CRUD (Create, Read, Update, Delete) operations on programming articles. The API also supports filtering articles by programming language, keywords, and tags. The project is designed to help developers manage and discover programming tips efficiently.

## Features

- **CRUD Operations**: Create, retrieve, update, and delete articles.
- **Filtering**: Search for articles based on programming language, keywords, and tags.
- **Data Validation**: Ensure data integrity through validation checks.

## API Endpoints

### Create an Article

- Method: POST
- Endpoint: `api/articles/`
- Description: Create a new article
- Example Request: `http://127.0.0.1:8000/api/articles/`
  ```json
  {
    "title": "How to Set Up a Custom User Model in Django",
    "description": "A step-by-step guide on creating and using a custom user model in Django, which allows for more flexibility in authentication and user data management.",
    "programming_language": "Python",
    "tags_input": "django, user model, authentication, python"
  }
  ```
- Example Response:
  ```json
  {
    "status": "success",
    "message": "Article posted successfully",
    "data": {
      "title": "How to Set Up a Custom User Model in Django",
      "description": "A step-by-step guide on creating and using a custom user model in Django, which allows for more flexibility in authentication and user data management.",
      "programming_language": "Python",
      "tags": [
        {
          "name": "django"
        },
        {
          "name": "user model"
        },
        {
          "name": "authentication"
        },
        {
          "name": "python"
        }
      ]
    }
  }
  ```

### Retreive all articles

- Method: GET
- Endpoint: `api/articles/`
- Description: Retrieve all created articles
- Example Request: `http://127.0.0.1:8000/api/articles/`
- Example Response:
  ```json
  {
    "status": "success",
    "message": "Articles fetched successfully",
    "data": [
      {
        "title": "Introduction to Flask: A Lightweight Web Framework",
        "description": "Flask is a lightweight WSGI web application framework in Python. This article introduces the basics of Flask, including how to set up a simple web application, handle routes, and manage templates.",
        "programming_language": "Python",
        "tags": [
          {
            "name": "Flask"
          },
          {
            "name": "Web Development"
          },
          {
            "name": "Python"
          },
          {
            "name": "Microframework"
          }
        ]
      },
      {
        "title": "Understanding React Hooks: useState and useEffect",
        "description": "React Hooks revolutionized the way developers write components. This article focuses on two fundamental hooks, `useState` and `useEffect`, explaining how they work and how they can be used to manage state and side effects in functional components.",
        "programming_language": "JavaScript",
        "tags": [
          {
            "name": "Web Development"
          },
          {
            "name": "React"
          },
          {
            "name": "Hooks"
          },
          {
            "name": "JavaScript"
          },
          {
            "name": "Frontend Development"
          }
        ]
      },
      {
        "title": "Mastering JavaScript Closures",
        "description": "Closures are one of the most powerful features of JavaScript, allowing functions to have private variables and maintain state across executions. This article explains how closures work in JavaScript and provides practical examples of their usage.",
        "programming_language": "JavaScript",
        "tags": [
          {
            "name": "Web Development"
          },
          {
            "name": "JavaScript"
          },
          {
            "name": "Closures"
          },
          {
            "name": "Functional Programming"
          }
        ]
      },
      {
        "title": "How to Set Up a Custom User Model in Django",
        "description": "A step-by-step guide on creating and using a custom user model in Django, which allows for more flexibility in authentication and user data management.",
        "programming_language": "Python",
        "tags": [
          {
            "name": "django"
          },
          {
            "name": "user model"
          },
          {
            "name": "authentication"
          },
          {
            "name": "python"
          }
        ]
      }
    ]
  }
  ```

### Update an article

- Method: PATCH
- Endpoint: `api/articles/<int:pk>/update/`
- Description: Update an article
- Example Request: `http://127.0.0.1:8000/api/articles/2/update/`
  ```json
  {
    "title": "React Hooks"
  }
  ```
- Example Response
  ```json
  {
    "status": "success",
    "message": "Article updated successfully",
    "data": {
      "title": "React Hooks",
      "description": "React Hooks revolutionized the way developers write components. This article focuses on two fundamental hooks, `useState` and `useEffect`, explaining how they work and how they can be used to manage state and side effects in functional components.",
      "programming_language": "JavaScript",
      "tags": [
        {
          "name": "Web Development"
        },
        {
          "name": "React"
        },
        {
          "name": "Hooks"
        },
        {
          "name": "JavaScript"
        },
        {
          "name": "Frontend Development"
        }
      ]
    }
  }
  ```

### Delete an Article

- Method: DELETE
- Endpoint: `api/articles/<int:pk>/delete/`
- Description: Remove an article
- Example Request: `http://127.0.0.1:8000/api/articles/2/delete/`
- Exampe Response:
  ```json
  {
    "message": "Article deleted successfully."
  }
  ```

### Filtering articles

- Method: GET
- Endpoint: `api/articles/language/<str:language>/`
- Description: Retrieve articles based on programming language
- Example Request: `http://127.0.0.1:8000/api/articles/language/python`
- Example Response:
  ```json
  {
    "status": "success",
    "message": "python articles retrieved successfully",
    "data": [
      {
        "title": "Introduction to Flask: A Lightweight Web Framework",
        "description": "Flask is a lightweight WSGI web application framework in Python. This article introduces the basics of Flask, including how to set up a simple web application, handle routes, and manage templates.",
        "programming_language": "Python",
        "tags": [
          {
            "name": "Flask"
          },
          {
            "name": "Web Development"
          },
          {
            "name": "Python"
          },
          {
            "name": "Microframework"
          }
        ]
      },
      {
        "title": "How to Set Up a Custom User Model in Django",
        "description": "A step-by-step guide on creating and using a custom user model in Django, which allows for more flexibility in authentication and user data management.",
        "programming_language": "Python",
        "tags": [
          {
            "name": "django"
          },
          {
            "name": "user model"
          },
          {
            "name": "authentication"
          },
          {
            "name": "python"
          }
        ]
      }
    ]
  }
  ```

### Search Articles

- Method: GET
- Endpoint: `api/articles/search/`
- Description: Retrieve articles based on programming language, keyword or tags
- Example Request: `http://127.0.0.1:8000/api/articles/search/?keywords=flask&language=python`
- Example Response:
  ```json
  {
    "status": "success",
    "message": "Articles retrieved successfully",
    "data": [
      {
        "title": "Introduction to Flask: A Lightweight Web Framework",
        "description": "Flask is a lightweight WSGI web application framework in Python. This article introduces the basics of Flask, including how to set up a simple web application, handle routes, and manage templates.",
        "programming_language": "Python",
        "tags": [
          {
            "name": "Flask"
          },
          {
            "name": "Web Development"
          },
          {
            "name": "Python"
          },
          {
            "name": "Microframework"
          }
        ]
      }
    ]
  }
  ```
