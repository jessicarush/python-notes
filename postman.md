# Postman App for API testing


https://www.getpostman.com/

Postman is an API development application that makes it easy to create, save and test your API requests during development. Once you've downloaded the software for your OS, launch it. You don't have to create an account but you should create a project folder in collections. Note you can also create sub folders. Once you're ready to test:

- Make sure your web server is running.
- Choose the http verb you want to test (GET, POST, etc).
- Enter the address (ie http://localhost:5000/store).
- Press the send button to test out your request.
- Save your requests to the appropriate collection/sub-collection so you don't need to type it out again.
- Once saved, select it in the sidebar to edit or duplicate it to create more variations.

Testing GET requests is pretty straightforward but testing POST requests requires a little more information. Go to the headers tab (the first thing flask does when it gets a request, is look at the headers to see what sort of data it's getting). Here you can add key-value pairs like:

```
Content-Type        application/json
```

With this information in, we can now go to the body tab and enter in the data that we want to send with the POST request. For example, choose the 'raw' option and type something like:

```
{"name": "Flying Potato"}
```

> :warning: JSON always uses double quotes.

If you're working with JWT for authorization, you will need to add the token by clicking on the headers tab, type Authorization for the key and for the value type JWT followed by one space, then the token (no quotes).

```
JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

> :bookmark: If you're sick of seeing/typing the main part of the url in your endpoints, you can always set up an environment variable. When you do this, all your endpoints can be changed from the first example to the second:

```
http://localhost:5000/item/<name>
{{url}}/item/<name>
```

To set up an environment variable in postman, first you'll need to create a new environment. Click the 'eye' icon in the top right corner. Add an environment, give it a name. You can switch environments using the select menu beside the eye icon.

In the same menu, you can add global variables to your active environment. For example, with the url above we'd set `url` as they variable and `http://localhost:5000` as the value. Don't forget to hit the **save** button.

You can set up something similar for JWT tokens so you're not copying and pasting all the time. Where you would normally enter the token value, enter instead:

```
JWT {{token}}
```

Go to the end point that produces the token {{url}}/auth and click on the Tests tab. This area is for Javascript code. It will run after the request has been processed by the server and sent back to us. What we can do in the test area is use the token thats just been issued and use it to change the environment variable {{token}}. In the test area:

```Javascript
pm.test("Access Token Test", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.access_token).to.not.eql(null);
    pm.environment.set("token", jsonData.access_token);
});
```

This comes from the snippets: "Response Body:JSON value check" and "Set an environment variable".

Now when you send the /auth endpoint, you should see "Test Results 1/1" passed at the bottom where the return data is displayed. And, when you send your endpoint that requires the token, it should now pick up the current environment variable. Note you can always see your variables by clicking the eye icon.
