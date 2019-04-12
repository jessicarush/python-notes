# Ajax

## Table of contents

<!-- toc -->

- [Some background](#some-background)
- [Summary of Events](#summary-of-events)
- [Example 1: request to a file](#example-1-request-to-a-file)
  * [Trigger the request](#trigger-the-request)
  * [Issue the request](#issue-the-request)
  * [Handle the request](#handle-the-request)
- [Example 2: request to a server](#example-2-request-to-a-server)
  * [Trigger the request](#trigger-the-request-1)
  * [Issue the request](#issue-the-request-1)
  * [Handle the request](#handle-the-request-1)
- [Example 3: send JSON data with request to a server](#example-3-send-json-data-with-request-to-a-server)
  * [Trigger the request](#trigger-the-request-2)
  * [Issue the request](#issue-the-request-2)
  * [Handle the request](#handle-the-request-2)
- [Example 4: send form data as request to a server](#example-4-send-form-data-as-request-to-a-server)
- [XMLHttpRequest Object Methods](#xmlhttprequest-object-methods)
- [XMLHttpRequest Object Properties](#xmlhttprequest-object-properties)
- [GET or POST?](#get-or-post)

<!-- tocstop -->

## Some background

In the traditional server-side model there is a client (a web browser commanded by a user) making HTTP requests to an application server. In this model the server does all the work, while the client just displays the web pages and accepts user input.

There is a different model in which the client takes a more active role. In this model, the client issues a request to the server and the server responds with a web page, but unlike the previous case, not all the page data is HTML, there is also sections of the page with code, typically written in Javascript. Once the client receives the page it displays the HTML portions, and executes the code. From then on you have an active client that can do work on its own with little or no contact with the server.

In a strict client-side application the entire application is downloaded to the client with the initial page request, and then the application runs entirely on the client, only contacting the server to retrieve or store data and making dynamic changes to the appearance of that first and only web page. These type of applications are called Single Page Applications or SPAs.

Most applications are a hybrid between the two models and combine techniques of both. As an example of client-side action, the client browser can send asynchronous requests to the server, to which the server will respond without causing a page refresh. The client will then insert something into the current page dynamically. This technique is known as Ajax, which is short for Asynchronous JavaScript and XML (even though these days XML is often replaced with JSON).

> In the Flask Mega Tutorial microblog we implemented live, automated translations of user posts as an Ajax service. When the user clicks on a translation link, we send the Ajax request to the server, and the server contacts a third-party translation API. Once the server sends back a response with the translated text, the client-side javascript code dynamically inserts this text into the page.

When working with JavaScript in the browser, the page currently being displayed is internally represented as the Document Object Model or just the DOM. This is a hierarchical structure that references all the elements that exist in the page. The JavaScript code running in this context can make changes to the DOM to trigger changes in the page.

## Summary of Events

1. An event occurs in a web page (the page is loaded, a button is clicked)
2. An XMLHttpRequest object is created by JavaScript
3. The XMLHttpRequest object sends a request to a web server
4. The server processes the request
5. The server sends a response back to the web page
6. The response is read by JavaScript
7. Some kind of action (like a DOM change) is performed by JavaScript

## Example 1: request to a file

This example will be really simple in that we'll send a request to get the contents of a text file instead of a server.

### Trigger the request

To trigger the request I'll create a button with a unique id or classname. While I'm at it, an element to receive the data:

```html
<button id="js-ajax-requester" type="button">Get data</button>
<div id="js-ajax-response"></div>
```

In my javascript I'll create an event listener for the button:

```javascript
// Event listener
window.addEventListener('click', function(e) {
  if (e.target.matches('#js-ajax-requester')) {
    ajaxRequest();
  }
}, false);
```

This way works too:
```javascript
// Event listener
document.getElementById('js-ajax-requester').addEventListener('click', ajaxRequest);
```

### Issue the request

Then the function that issues the request:

```javascript
function ajaxRequest() {
  let el = document.getElementById('js-ajax-response');

  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      el.innerHTML = this.responseText;
    }
  };

  xhttp.open('GET', 'ajax_demo.json', true);
  xhttp.send();
}
```

The XMLHttpRequest object is used to exchange data with a web server behind the scenes. All modern browsers support the XMLHttpRequest object.

See a list of XMLHttpRequest Object Methods & Properties below.

### Handle the request

As I said, this example is going to be really simple. Instead of handling the request on a server we're just reaching out to a JSON file located in the same directory as the html. It should be noted that for security reasons, browsers do not allow *access across domains*. This means that both the web page and the JSON file it tries to load, must be located on the same server. Example JSON file contents:

```json
{
 "hello": "this is a test",
 "foo": "bar"
}
```


## Example 2: request to a server

Now we'll do the same thing but instead send the request to the server running Flask.

### Trigger the request

Same as Example 1.

### Issue the request

The only thing we need to change here is to add the endpoint (`app.route`) name for the second url parameter of the `open()` method.

```javascript
function ajaxRequest() {
  let el = document.getElementById('js-ajax-response');

  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      el.innerHTML = this.responseText;
    }
  };

  xhttp.open('GET', '/ajax_demo', true);  // <--- only this changed
  xhttp.send();
}
```

### Handle the request

To handle the Ajax request, set up an endpoint similar to any other route or view function in the application, with the only difference being that instead of returning HTML or a redirect, it just returns data, formatted as JSON using Flask's `jsonify` method (don't forget to import it).

```python
@app.route('/ajax_demo', methods=['GET'])
def ajax_demo():
    response = {
        'name': 'jessica',
        'date': '2019-04-11',
        'stuff': [100, 'hello', 2.5]
        }
    return jsonify(response)
```


## Example 3: send JSON data with request to a server

### Trigger the request

Same as Example 1.


### Issue the request

This time we'll add a Request Header using `setRequestHeader()`. This method must come after the `open()` method but before the `send()` method. We'll set the value to `application/json`. Next we need to `stringify` whatever data we want to send then pass that data to the `send()` method:

```javascript
function ajaxRequest() {
  let el = document.getElementById('js-ajax-response');

  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      el.innerHTML = this.responseText;
    }
  };

  let data = JSON.stringify({'fruit': 'apples'});             // <--- data

  xhttp.open('POST', '/ajax_demo', true);
  xhttp.setRequestHeader('Content-Type', 'application/json'); // <--- header
  xhttp.send(data);                                           // <--- send
}
```


### Handle the request

We can receive our request data using the `request.get_json()` method:

```python
@app.route('/ajax_demo', methods=['POST'])
def ajax_demo():
    data = request.get_json()

    print(type(data), data)  
    # <class 'dict'> {'fruit': 'apples'}

    if data['fruit'] == 'apples':
        response = {'have some': 'oranges'}
    else:
        response = {'have some': 'bananas'}
    return jsonify(response)
```


## Example 4: send form data as request to a server



## XMLHttpRequest Object Methods

Method | Description
------ | -----------
new XMLHttpRequest() | Creates a new XMLHttpRequest object
abort() | Cancels the current request
getAllResponseHeaders() | Returns header information
getResponseHeader() | Returns specific header information
open(*method, url, async, user, psw*) | Specifies the request <br> *method:* the request type GET or POST <br> *url:* the file location <br> *async:* true (asynchronous) or false (synchronous) <br> *user:* optional user name <br> *psw:* optional password
send() | Sends the request to the server <br> Used for GET requests
send(*string*) | Sends the request to the server <br> Used for POST requests
setRequestHeader() | Adds a label/value pair to the header to be sent


## XMLHttpRequest Object Properties

Property | Description
-------- | -----------
onreadystatechange | Defines a function to be called when the readyState property changes
readyState | Holds the status of the XMLHttpRequest. <br> 0: request not initialized <br> 1: server connection established <br> 2: request received <br> 3: processing request <br> 4: request finished and response is ready
responseText | Returns the response data as a string
responseXML | Returns the response data as XML data
status | Returns the status-number of a request <br> 200: "OK" <br> 403: "Forbidden" <br> 404: "Not Found" <br> For a complete list see the [http Messages Reference](https://www.w3schools.com/tags/ref_httpmessages.asp)
statusText | Returns the status-text (e.g. "OK" or "Not Found")


## GET or POST?

GET is simpler and faster than POST, and can be used in most cases.

However, always use POST requests when:
- A cached file is not an option
- Sending a large amount of data to the server (POST has no size limitations).
- Sending user input (which can contain unknown characters), POST is more robust and secure than GET
