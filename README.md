# api_final\napi final\n

# REST API for Yatube Project

## Description

The project is a REST API for the Youtube project, a social network for publishing personal diaries.

This API implements the following functionality:
* Authorization by JWT (JSON Web Token) token
* View, create, delete and modify records (publications)
* View, create, delete and edit comments
* View and create groups
* User subscription


## Libraries

* Django 2.2
* Python 3.8
* Django Rest Framework
* ReDoc

## Install

Clone this repository to your computer and go to the project folder.
<pre><code>git clone ...</code>
<code>cd api_final_yatube</code></pre>

Create and activate a virtual environment:

<pre><code>python -m venv venv</code>
<code>source ./venv/Scripts/activate  #Windows</code>
<code>source ./venv/bin/activate      #Linux и macOS</code></pre>

Install the required dependencies:

<pre><code>pip install -r requirements.txt</code></pre>

Apply migrations:

<pre><code>python manage.py migrate</code></pre>

Start the django server:

<pre><code>python manage.py runserver</code></pre>

## API

The structure of API requests and responses is documented in ReDoc.

After the project is launched, the documentation is available at http://localhost:8000/redoc/

## Examples

* ### Getting an authorization token
    **Request**
    ```
        POST /api/v1/token/
        body: {"username": "string", "password": "string"}
    ```
    **Response**
    ```
        {
          "refresh": "<JRW-refresh-token>",
          "access": "<JRW-access-token>",
        }
    ```

* ### Token Update
    **Request**
    ```
        POST /api/v1/token/refresh/
        body: {"refresh": "JRW-refresh-token"}
    ```
    **Response**
    ```
        {
          "access": "<new-JRW-access-token>"
        }
    ```

* ### Getting a list of all publications
    **Request**
    ```
        GET /api/v1/posts/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 200
        [
            {
                "id": 0,
                "text": "string",
                "author": "string",
                "pub_date": "2019-08-24T14:15:22Z"
            },
            ...
        ]
    ```

* ### Creating a new publication
    **Request**
    ```
        POST /api/v1/posts/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": 0,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Getting a publication by its id
    **Request**
    ```
        GET /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": <post_id>,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Updating a publication by its id
    #### Request
    ```
        PUT /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "new_string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": <post_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Partial update of the publication by its id
    **Request**
    ```
        PATCH /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "new_string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": <post_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Deleting a post by its id
    **Request**
    ```
        DELETE /api/v1/posts/{post_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "new_string"}
    ```
    **Response**
    ```
        status_code: 204
    ```

* ### Getting a list of all comments
    #### Request
    ```
        GET /api/v1/posts/{post_id}/comments/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 200
        [
            {
                "id": 0,
                "text": "string",
                "author": "string",
                "pub_date": "2019-08-24T14:15:22Z"
            },
            ...
        ]
    ```

* ### Creating a new comment
    **Request**
    ```
        POST /api/v1/posts/{post_id}/comments/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text": "string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": 0,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Getting a comment by its id
    **Request**
    ```
        POST /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": <comment_id>,
            "text": "string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Updating a comment by its id
    #### Request
    ```
        PUT /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text: "new_string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": <comment_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }
    ```

* ### Partial update of the comment by its id
    **Request**
    ```
        PATCH /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"text: "new_string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "id": <comment_id>,
            "text": "new_string",
            "author": "string",
            "pub_date": "2019-08-24T14:15:22Z"
        }

* ### Deleting a comment by its id
    #### Request
    ```
        DELETE /api/v1/posts/{post_id}/comments/{comment_id}/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 204
    ```

* ### Getting a list of all subscribers
    **Request**
    ```
        GET /api/v1/follow/?search={username_string}
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 200
        [
            {
                "user": "string",
                "following": "string"
            },
            ...
        ]
    ```

* ### Creating a subscription
    **Request**
    ```
        POST /api/v1/follow/?user={username_string}
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"following": "string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "user": "string",
            "following": "string"
        }
    ```

* ### Getting a list of all groups
    **Request**
    ```
        GET /api/v1/follow/group/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
    ```
    **Response**
    ```
        status_code: 200
        [
            {
                "title": "string"
            },
            ...
        ]
    ```

* ### Creating a new group
    **Request**
    ```
        POST /api/v1/follow/group/
        headers: {"Authorization": "Bearer <JRW-access-token>"}
        body: {"title": "string"}
    ```
    **Response**
    ```
        status_code: 200
        {
            "title": "string"
        }
    ```