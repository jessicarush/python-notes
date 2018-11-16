# REST and API Design

## Table of contents

<!-- toc -->

- [Introduction](#introduction)
- [The Six Principles](#the-six-principles)
- [HTTP Verbs](#http-verbs)
- [Example](#example)
  * [Summarize the routes to be implemented](#summarize-the-routes-to-be-implemented)
  * [Create a skeleton structure (flask)](#create-a-skeleton-structure-flask)
  * [Decide on a JSON representation for each resource](#decide-on-a-json-representation-for-each-resource)
  * [Return the JSON representation in the route](#return-the-json-representation-in-the-route)
- [notes](#notes)

<!-- tocstop -->

## Introduction

Representational State Transfer (REST)  
Application Programming Interfaces (API)  

An API is a collection of HTTP routes that are designed as low-level entry points into an application. Instead of defining routes and view functions that return HTML pages to be consumed by web browsers, APIs allow the client to work directly with the application's resources, leaving the decision of how to present the information to the user entirely to the client. Clients access your service by making requests to URLs and getting back responses containing status and data. Instead of HTML pages, the data is in formats that are easier for programs to consume, such as JSON or XML. JSON is especially well suited to web client-server data interchange and is popular in web-based APIs, such as OpenStack.

Many products claim to have a REST or RESTful interface. In practice, this often only means that they have a web interface (definitions of URLs to access a web service). For a good overview see [Miguel's intro](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxiii-application-programming-interfaces-apis).

## The Six Principles

The REST architecture was proposed by Dr. Roy Fielding in his [doctoral dissertation](http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm). He presents six defining characteristics of REST in a fairly abstract and generic way:

1. Client-Server  
   Simply states that in a REST API the roles of the client and the server should be clearly differentiated. In practice, this means that the client and the server are in separate processes that communicate over a transport, which in the majority of the cases is the HTTP protocol over a TCP network.

1. Layered System  
   Basically means that if an intermediary is used between client and server, there's no difference in the way requests are sent or received and no assumptions are made as far whether or not there is an intermediary... it shouldn't make a difference. This is an important feature of REST, because being able to add intermediary nodes allows application architects to design large and complex networks that are able to satisfy a large volume of requests through the use of load balancers, caches, proxy servers, etc.

1. Cache  
   Indicates explicitly that the server or an intermediary is allowed to cache responses to requests that are received often to improve system performance.

1. Code on Demand  
   An optional requirement that states that the server can provide executable code in responses to the client. Because this principle requires an agreement between the server and the client on what kind of executable code the client is able to run, this is rarely used in APIs.

1. Stateless  
   A REST API should not save any client state to be recalled every time a given client sends a request. What this means is that none of the mechanisms that are common in web development to "remember" users as they navigate through the pages of the application can be used. In a stateless API, every request needs to include the information that the server needs to identify and authenticate the client and to carry out the request. It also means that the server cannot store any data related to the client connection in a database or other form of storage.

1. Uniform Interface  
   In A nutshell, unique URL's for each resource, a simple  data format (JSON), self-descriptive messages via the use of HTTP verbs listed below and *hypermedia* which is basically providing links to other resources. Few APIs actually do this.

## HTTP Verbs

A RESTful service uses the HTTP verbs in specific ways:

- HEAD - gets information about the resource, but not its data.

- GET - indicates the client wants to retrieve the resource's data from the server. This is the standard method used by a browser. Any time you see a URL with a question mark (?) followed by a bunch of arguments, that's a GET request. GET shouldn't be used to create, change, or delete data.

- POST - indicates a client wants create a new resource (data) on the server, often used by HTML forms and web APIs.

- PUT or PATCH  - requests define modifications to existing resources.

- DELETE - indicates a request to remove a resource.

## Example

### Summarize the routes to be implemented

HTTP Method | Resource URL | Notes
----------- | ------------ | -----
GET | /api/users/<id> | Return a user.
GET | /api/users | Return the collection of all users.
GET | /api/users/<id>/followers | Return the followers of this user.
GET | /api/users/<id>/following | Return the users this user is following.
POST | /api/users | Register a new user account.
PUT | /api/users/<id> | Modify a user.

### Create a skeleton structure (flask)

```python
@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    pass

@bp.route('/users', methods=['GET'])
def get_users():
    pass

@bp.route('/users/<int:id>/followers', methods=['GET'])
def get_followers(id):
    pass

@bp.route('/users/<int:id>/following', methods=['GET'])
def get_followed(id):
    pass

@bp.route('/users', methods=['POST'])
def create_user():
    pass

@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    pass
```

### Decide on a JSON representation for each resource

For example, the get_user route:
```json
{
    "id": 123,
    "username": "susan",
    "password": "my-password",
    "email": "susan@example.com",
    "last_seen": "2017-10-20T15:04:27Z",
    "about_me": "Hello, my name is Susan!",
    "post_count": 7,
    "follower_count": 35,
    "followed_count": 21,
    "_links": {
        "self": "/api/users/123",
        "followers": "/api/users/123/followers",
        "followed": "/api/users/123/followed",
        "avatar": "https://www.gravatar.com/avatar/..."
    }
}
```

If you are using database Model classes, you could create a method in that
class  which returns a Python dictionary (which in turn converts into JSON).

```python
class User(db.Model):
    # ...

    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'username': self.username,
            'last_seen': self.last_seen.isoformat() + 'Z',
            'about_me': self.about_me,
            'post_count': self.posts.count(),
            'follower_count': self.followers.count(),
            'following_count': self.following.count(),
            '_links': {
                'self': url_for('api.get_user', id=self.id),
                'followers': url_for('api.get_followers', id=self.id),
                'following': url_for('api.get_following', id=self.id),
                'avatar': self.avatar(128)
            }
        }
        if include_email:
            data['email'] = self.email
        return data
```

### Return the JSON representation in the route

The skeleton example from above could be fleshed out like this:

```python
@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())
```

## notes

A command-line HTTP client written in Python that makes it easy to send API requests:
```
$ pip install httpie
```
Once installed you can do something like this:
```
$ http GET http://localhost:5000/api/users/1
$ http POST http://localhost:5000/api/users username=bob password=cheese \
    email=bob@example.com "about_me=Hello, my name is Bob!"
$ http PUT http://localhost:5000/api/users/3 "about_me=Hi, I'm Scott"
$ http --auth <username>:<password> POST http://localhost:5000/api/tokens
$ http GET http://localhost:5000/api/users/1 "Authorization:Bearer <token>"
$ http DELETE http://localhost:5000/api/tokens "Authorization:Bearer <token>"
```
