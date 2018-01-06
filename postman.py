'''Postman App for API testing'''

# https://www.getpostman.com/

# Postman is an API development application that makes it easy to create, save
# and test your API requests during development. Once you've downloaded the
# software for your OS, launch it. You don't have to create an account but you
# should create a project folder in collections. Note you can also create sub
# folders. Once you ready to test:

# - make sure you're flask server is running
# - choose the http verb you want to test (GET, POST, etc)
# - type the address (ie http://127.0.0.1:5000/store)
# - press the send button to test out your request
# - you can save your requests to the appropriate collection/sub-collection
#   so you don't need to type it out again
# - once saved, you can select it in the sidebar and choose to edit or
#   duplicate it to create more variations.

# Testing GET requests is pretty straightforward but testing POST requests
# requires a little more information:
# - go to the headers tab (the first thing flask does when it gets a request,
#   is it looks at the headers to see what sort of data its getting). Here you
#   can add key-value pairs like:

#   Content-Type        application/json

# With this information in, we can now go to the body tab and enter in the
# data that we want to send with the POST request. For example, choose the
# 'raw' option and type something like:

# {"name": "Flying Potato"}

# NOTE: JSON always uses double quotes.

# more to come...
