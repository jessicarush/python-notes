# Flask-SocketIO

Read the [documentation here](https://flask-socketio.readthedocs.io/en/latest/).
See the [code on Github here](https://github.com/miguelgrinberg/Flask-SocketIO).

## Table of contents

<!-- toc -->

- [Introduction](#introduction)
- [Install](#install)
- [Instantiate and include](#instantiate-and-include)
- [Client side](#client-side)
- [Server side](#server-side)
- [Notes](#notes)

<!-- tocstop -->

## Introduction

WebSocket is a new communication protocol introduced with HTML5, mainly to be implemented by web clients and servers, though it can also be implemented outside of the web.

Unlike HTTP connections, a WebSocket connection is a permanent, bi-directional communication channel between a client and the server, where either one can initiate an exchange. Once established, the connection remains available until one of the parties disconnects from it.

WebSocket connections are useful for games or web sites that need to display live information with very low latency.

## Install

```
pip install flask-socketio
```

## Instantiate and include

- import eventlet and call `eventlet.monkey_patch()`
- import SocketIO, emit
- Instantiate socketio
- replace `app.run()` with `socket.run()`

Eventlet needs to monkey patch some of the python standard built-in library to place coroutines where there were none. It's important to call monkey_patch() as early in the lifetime of the application as possible.

`__init__.py`
```python
import eventlet
from flask_socketio import SocketIO

eventlet.monkey_patch()

app = Flask(__name__)
async_mode = None
socketio = SocketIO(app, async_mode=async_mode)
```

`run.py`
```python
from app import app, socketio


if __name__ == '__main__':
    # app.run(port=5000, debug=False)
    # app.run(host='0.0.0.0', port=5000, debug=True, ssl_context='adhoc')
    socketio.run(app)
    socketio.run(app, host='0.0.0.0', port=80, debug=True, ssl_context='adhoc')
```

`routes.py`
```python
from flask_socketio import emit
from app import socketio
```


## Client side

Miguel Grinberg's tutorial uses jquery and the cloudflare cdn for socket.io, so he includes the script like so in the `<head>`:

```html
<script src="//code.jquery.com/jquery-1.12.4.min.js" integrity="sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ=" crossorigin="anonymous"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/socket.io/2.2.0/socket.io.js" integrity="sha256-yr4fRk/GU1ehYJPAs8P4JlTgu0Hdsp4ZKrx8bDEDC3I=" crossorigin="anonymous"></script>
```

I prefer not to use jquery these days as vanilla javascript can accomplish the same thing, is faster and reduces dependencies. In addition, I'll host my own `socket.io.js`. In order to avoid a browser warning about source mapping, I'll also include a file called `socket.io.js.map` in the same directory (you don't need to add it to your html, it is only referenced in socket.io.js).

```html
<script src="{{ url_for('static', filename='js/socket.io.js' )}}" defer></script>
```

In the html page that will be recieving and sending messages, we create another `<script>`. The following examples (first in jquery, then vanilla javascript) will:

- create a socket.io connection
- create an event handler that will listen for events called 'my_reponse' then place the message data into the DOM
- create an event listener on a button that that will send data from a form field in an event called 'my_event'

jquery
```html
<script type="text/javascript" charset="utf-8">
  $(document).ready(function(){
    // create a socket.io connection
    let namespace = '/test';
    var socket = io(namespace);

    // listen for events called 'my_reponse'
    socket.on('my_response', function(msg) {
      $('#log').append( msg.count + ' Received: ' + msg.data + '</br>');
    });

    // send an event called 'my_event'
    $('form#emit').submit(function(event) {
      socket.emit('my_event', {data: $('#emit_data').val()});
      return false;
    });
  });
</script>

<div id="log"><!-- my_response messages will go here--></div>
```

javascript
```html
<script type="text/javascript" charset="utf-8">
  document.addEventListener('DOMContentLoaded', function() {
    // create a socket.io connection
    let namespace = '/test';
    const socket = io(namespace);

    // listen for events called 'my_reponse'
    socket.on('my_response', function(msg, cb) {
      const logItem = document.createElement('p');
      logItem.textContent = `${msg.count} Received: ${msg.data}`
      document.getElementById('log').appendChild(logItem);
      if (cb) {
        cb();
      }
    });

    // send an event called 'my_event'
    document.getElementById('emit').addEventListener('submit', function(e) {
      e.preventDefault();
      const data = document.getElementById('emit_data').value;
      socket.emit('my_event', {data: data});
    }, false);
  });
</script>

<div id="log"><!-- my_response messages will go here--></div>>
```

The socket variable is initialized with a SocketIO connection to the server. Note how the namespace `/test` is specified in the connection URL. To connect without using a namespace it is sufficient to call io.connect() without any arguments.

`socket.on(eventName, callback)` - The socket.on() syntax is used in the client side to define an event handler. In this example a custom event with name 'my_response' is handled by adding the data attribute of the message payload to the contents of a page element with id log. This element is defined in the HTML portion of the page.

The next block overrides the behavior of a form submit button so that instead of submitting a form over HTTP it triggers the execution of a callback function.

For the form with id emit the submit handler emits a message to the server with name 'my_event' that includes a JSON payload with a data attribute set to the value of the input field in that form.

If you look at the server code you can see the handler for this custom event. For 'my_event' the server just echoes the payload back to the client in a message sent under event name 'my_response', which is handled by showing the payload in the page.

## Server side

To receive WebSocket messages from the client the application defines event handlers using the socketio.on decorator.

The first argument to the decorator is the event name. Event names 'connect', 'disconnect', 'message' and 'json' are special events generated by SocketIO. Any other event names are considered custom events.

The 'connect' and 'disconnect' events are self-explanatory. The 'message' event delivers a payload of type string, and the 'json' and custom events deliver a JSON payload, in the form of a Python dictionary.

Events can be defined inside a namespace by adding the namespace optional argument to the socketio.on decorator. Namespaces allow a client to open multiple connections to the server that are multiplexed on a single socket. When a namespace is not specified the events are attached to the default global namespace.

To send events a Flask server can use the send() and emit() functions provided by Flask-SocketIO. The send() function sends a standard message of string or JSON type to the client.

The emit() function sends a message under a custom event name.

Messages are sent to the connected client by default, but when including the broadcast=True optional argument all clients connected to the namespace receive the message.

```python
def test_callback():
    '''A test callback function for sending responses with emit()'''
    print('This is my callback test!')


@socketio.on('my_event', namespace='/test')
def test_message(message):
    '''A test function for receiveing client messages'''
    print(f'Recieved: {message["data"]}')
    session['receive_count'] = session.get('receive_count', 0) + 1
    response_data = {'data': message['data'], 'count': session['receive_count']}
    emit('my_response', response_data, callback=test_callback)


@socketio.on('connect', namespace='/test')
def test_connect():
    '''This function is called when there is a succesfull connection'''
    print('Server connected')
    emit('my_response', {'data': 'Server connected', 'count': 0})


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    '''This function is called when the client disconnects'''
    print('Client disconnected', request.sid)
```


## Notes

`request.sid` - This variable only exists in the context of a socketio event handler and will not be present in an HTTP handler. It is defined as the unique session ID for the client connection.

`request.event` - The message and data arguments of the current request can also be inspected with the request.event variable, which is useful for error logging and debugging outside the event handler.

Re SSL, the `ssl_context` option applies to the Flask development server only. For eventlet you have to pass the `keyfile` and `certfile` options. PyopenSSL can be used to create self-signed certificates with this command:

```
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```

Then:
```python
socketio.run(app,
             host='0.0.0.0',
             port=80,
             debug=True,
             certfile='cert.pem',
             keyfile='key.pem')
```
