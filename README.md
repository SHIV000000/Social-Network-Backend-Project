# Social-Network-Backend-Project
This project is a backend system for a social network application. It allows users to create accounts, post discussions, follow other users, and interact with posts and comments. The system is built with a microservice architecture for scalability and maintainability.

## Table of Contents
- Introduction
- Features
- Tech Stack
- Architecture
- Database Schema
- API Documentation
- Setup Instructions
- Postman Collection
- Submission Guidelines

Introduction
This project is a backend system for a social network application. It allows users to create accounts, post discussions, follow other users, and interact with posts and comments. The system is built using Django, with a clear structure for handling various functionalities.

Features
User Management:

Create, update, delete, and search users.
Users can log in and sign up.
Post Management:

Users can create, update, delete, and search for discussions.
Discussions can include text and images, and multiple hashtags.
Users can see the view count of a post.
Interaction:

Users can follow other users.
Users can like, comment, and reply to posts.
Users can like comments and replies.
Users can modify or delete their posts and comments.
Tech Stack
Backend: Django
Database: SQLite (can be replaced with PostgreSQL/MySQL)
Storage: Local storage (can be integrated with AWS S3 for images)
Architecture
The system is structured into different Django apps: users and discussions.

## Components

User App:
Handles user creation, authentication, and profile management.
Relevant files: users/models.py, users/serializers.py, users/views.py, users/urls.py


Discussion App:
Manages posts, including creation, modification, and deletion.
Relevant files: discussions/models.py, discussions/serializers.py, discussions/views.py, discussions/urls.py
Diagram

Database Schema:

User Model
```python

class User(models.Model):
    name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
```
Post Model
```python

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    hashtags = models.ManyToManyField('Hashtag')
    view_count = models.IntegerField(default=0)
```
Comment Model
```python

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
```
## API Documentation

## Create User

`POST /api/users`

Request:
```json

{
  "name": "John",
  "mobile_no": "1234567890",
  "email": "john@example.com",
  "password": "password123"
}
```
Response:
```json
{
  "id": "uuid",
  "name": "John",
  "mobile_no": "1234567890",
  "email": "john@example.com"
}
```
## Update User

`PUT /api/users/:id`

Request:
```json
{
  "name": "John Doe"
}
```
Response:
```json

{
  "id": "uuid",
  "name": "John Doe"
}
```
## Delete User

`DELETE /api/users/:id`

Response:
```json

{
  "message": "User deleted successfully"
}
```
## Show List of Users

`GET /api/users`

Response:
```json

  {
    "id": "uuid",
    "name": "John Doe",
    "email": "john@example.com"
  },

```
## Search User by Name

`GET /api/users?name=John`

Response:
```json

  {
    "id": "uuid",
    "name": "John Doe",
    "email": "john@example.com"
  },

```
Post API

## Create Post

`POST /api/posts`

Request:
```json
{
  "user_id": "uuid",
  "text": "Hello World!",
  "image_url": "http://example.com/image.jpg",
  "hashtags": ["#hello", "#world"]
}
```
Response:
```json

{
  "id": "uuid",
  "user_id": "uuid",
  "text": "Hello World!",
  "image_url": "http://example.com/image.jpg",
  "created_on": "2023-06-14T12:00:00Z"
}
```
## Update Post

`PUT /api/posts/:id`

Request:
```json
{
  "text": "Hello Updated World!"
}
```
Response:
```json
{
  "id": "uuid",
  "text": "Hello Updated World!"
}
```
## Delete Post

`DELETE /api/posts/:id`

Response:
```json
{
  "message": "Post deleted successfully"
}
```
## Get Posts by Tag

`GET /api/posts?tag=world`

Response:
```json

  {
    "id": "uuid",
    "text": "Hello World!",
    "hashtags": ["#hello", "#world"]
  },

```
## Get Posts by Text

`GET /api/posts?text=Hello`

Response:
```json


  {
    "id": "uuid",
    "text": "Hello World!",
    "hashtags": ["#hello", "#world"]
  },

```
Interaction API
## Like Post

`POST /api/posts/:id/like`

Request:
```json
{
  "user_id": "uuid"
}
```
Response:
```json

{
  "message": "Post liked successfully"
}
```
## Comment on Post

`POST /api/posts/:id/comment`

Request:
```json
{
  "user_id": "uuid",
  "text": "Nice post!"
}
```
Response:

```json
{
  "id": "uuid",
  "post_id": "uuid",
  "user_id": "uuid",
  "text": "Nice post!",
  "created_on": "2023-06-14T12:00:00Z"
}
```
## Like Comment

`POST /api/comments/:id/like`

Request:

```json

{
  "user_id": "uuid"
}
```

Response:
```json
{
  "message": "Comment liked successfully"
}
```

## Setup Instructions

Clone the repository:
```bash
git clone https://github.com/SHIV000000/Social-Network-Backend-Project.git
```

### Navigate to the project directory:

```bash
cd social-network-backend
```

### Set up environment variables: `python -m venv env` , Activate the virtual environment `env\scripts\activate`

### Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the application:

```bash
python manage.py runserver
```
