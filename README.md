# FastAPI-social-network
Social networking application based on FastAPI

# Content
- [Task](#task)
- [Endpoints](#endpoints)
- [How to run](#how-to-run)
- [Documentation](/docs/)
- [Examples](#examples)

# Task
Description
- Create a simple RESTful API using FastAPI for a social networking application
Functional requirements:
    - There should be some form of authentication and registration (JWT, Oauth, Oauth 2.0, etc..)
    - As a user I need to be able to signup and login
    - As a user I need to be able to create, edit, delete and view posts
    - As a user I can like or dislike other users’ posts but not my own 
    - The API needs a UI Documentation (Swagger/ReDoc)

___
# Endpoints
|Method|Endpoint|Descriprion|Body| Query parametres|
|------|--------|-----------|----|-----------------|
|**POST**| localhost:8000/auth/register| Creates an user| email: str,<br>password: str,<br>username: str|
|**POST**| localhost:8000/auth/jwt/login| Login | email: str,<br>password: str|
|**POST**| localhost:8000/auth/jwt/logout| Logout| |
|**POST**| localhost:8000/create_post| Creates a post | title: str, <br>text: str|
|**GET**| localhost:8000/get_posts| Returns a list of all posts| |
|**GET**| localhost:8000/get_user_posts| Return a list of an user`s posts | |
|**DELETE**| localhost:8000/delete_post| Deletes an user`s post | | post_id: int
|**PUT**| localhost:8000/update_post| Edites an user`s post| post_id: int,<br> title: str, <br>text: str|
|**POST**| localhost:8000/like| Edites an user`s post|  | post_id: int, <br> like: bool, <br>dislike: bool|


___
# How to run
To run application use Makefile:
```
make linux_up (if you are using linux)
or
make windows_up (if you are using windows)
```
If there are any problems with Makefile use commands:
```
docker-compose up -d
cd app
alembic upgrade head
uvicorn main:app --reload
``` 

___
# Examples
For example if you are using the Postman you will get result like this after using localhost:8000/get_posts:
![The Postman result](/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202023-07-03%2014-59-10.png)
