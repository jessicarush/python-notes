# User Roles in Flask

There are a number of ways of implementing user roles in a Flask app. The best method will largely depend on how many different roles need to be supported and how elaborate they are. For example, a simple app may need only two roles, regular users and admin. In this case, having a simple `is_admin` boolean in the `User` model may be all that is necessary.

In more complex apps, you may need several roles with varying levels of access. In some cases it may make more sense to discard the idea of individual roles and instead give users a set of individual permissions.

## Table of contents

<!-- toc -->

- [Simple Solution 1 - limit access in templates](#simple-solution-1---limit-access-in-templates)
- [Simple Solution 2 - limit access in routes using redirects](#simple-solution-2---limit-access-in-routes-using-redirects)
- [Roles & permissions - Chapter 9 Flask Web directive](#roles--permissions---chapter-9-flask-web-directive)
- [User roles - Flask-User library](#user-roles---flask-user-library)

<!-- tocstop -->

## Simple Solution 1 - limit access in templates

In any Jinja template, you could pass the user data and show different things depending on the access level.

For example:

```Jinja
{% if current_user.is_admin %}
  ...Admin only content...
{% endif %}
```

This is safe because the templates are rendered in the server. The user cannot modify their access level or show and hide elements through the Developer Tools in the browser.

## Simple Solution 2 - limit access in routes using redirects

In any endpoint, you could check for a condition and simply redirect if it is not met.

For example:

```python
@app.route('/admin')
def admin():
    '''View function for the admins only.'''
    if not current_user.is_admin:
        flash('Sorry, only admins can access that page.', category='auth-fail')
        return redirect(url_for('index'))
    return render_template('admin.html')
```

## Roles & permissions - Chapter 9 Flask Web directive

## User roles - Flask-User library
