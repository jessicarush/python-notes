# REST and API Design


## Web APIs and Representational State Transfer (REST)

An API (Application Programming Interface) is a collection of HTTP routes that are designed as low-level entry points into an application. Instead of defining routes and view functions that return HTML pages to be consumed by web browsers, APIs allow the client to work directly with the application's resources, leaving the decision of how to present the information to the user
entirely to the client. Clients access your service by making requests to URLs and getting back responses containing status and data. Instead of HTML pages, the data is in formats that are easier for programs to consume, such as JSON or XML. JSON is especially well suited to web client-server data interchange and is popular in web-based APIs, such as OpenStack.

Many products claim to have a REST or RESTful interface. In practice, this often only means that they have a web interface (definitions of URLs to access a web service).

A RESTful service uses the HTTP verbs in specific ways:

- HEAD - gets information about the resource, but not its data.

- GET - retrieves the resource's data from the server. This is the standard
      method used by a browser. Any time you see a URL with a question mark
      (?) followed by a bunch of arguments, that's a GET request. GET should
      not be used to create, change, or delete data.

- POST - updates data on the server, often used by HTML forms and web APIs.

- PUT - creates a new resource

- DELETE - deletes

A RESTful client can also request one or more content types from the server by using HTTP request headers.
