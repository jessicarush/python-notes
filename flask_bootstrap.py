'''Flask Bootstrap'''

# https://getbootstrap.com/docs/3.3/getting-started/

# For people who don't want to write their own CSS, a CSS framework can be
# used to simplify the task. You will be losing some creative freedom by
# taking this path but you will gain the ease of having things look fairly
# consistent in all browsers as well as handling for smartphone and tablet.

# A CSS framework provides a collection of high-level CSS classes with pre-made
# styles for common types of user interface elements. Most of these frameworks
# also provide JavaScript add-ons for things that cannot be done strictly with
# HTML and CSS. Bootstrap, created by facebook, is a popular CSS framework.

# The most direct way to use Bootstrap is to simply import bootstrap.min.css
# file in your base template (and bootstrap.min.js file so that you can also
# use the most advanced features). Or, you can use the flask extension:

# (venv) $ pip install flask-bootstrap

# In yur project, Flask-Bootstrap needs to be initialized like most other
# Flask extensions:

# from flask_bootstrap import Bootstrap
# bootstrap = Bootstrap(app)

# With the extension initialized, a bootstrap/base.html template becomes
# available, and can be referenced from your templates with the extends
# clause. In our own base template, we would basically remove our <html>,
# <head> and <body> tags and replace these with the following block structure.
# Note that flask-bootstrap uses the name content in {% block content %}.
# This mean we have to rename ours. Any {% block content %}{% endblock %} we
# had in our base.html will need to change to another name like:
# {% block app_content %}{% endblock %}. This will also need to be changed in
# all the individual templates.

# With this method, I'm not sure how you would include other head section
# elements like meta data or favicons.

'''
{% extends 'bootstrap/base.html' %}

    {% block title %}
        Page title goes here (no html tags)
    {% endblock %}

    {% block navbar %}
        <nav class="navbar navbar-default"> </nav>
    {% endblock %}

    {% block content %}
        <div class="container">
            <div class="alert alert-info" role="alert"> </div>
            {% block app_content %}{% endblock %}
        </div>
    {% endblock %}

{% endblock %}
'''


# Form handling
# -----------------------------------------------------------------------------
# An area where Flask-Bootstrap does a fantastic job is in rendering of forms.
# Instead of having to style the form fields one by one, Flask-Bootstrap comes
# with a macro that accepts a Flask-WTF form object as an argument and renders
# the complete form using Bootstrap styles. Essentailly, all our normal code
# is replaced from something like this:

'''
{% extends "base.html" %}

{% block content %}
    <h1>Register</h1>
    <form action="" method="post">
        {{ form.hidden_tag() }}
        <p>
            {{ form.username.label }}
            <!-- Display error message if field empty or username taken -->
            {% for error in form.username.errors %}
            <span class="error"> : {{ error }}</span>
            {% endfor %}<br>
            {{ form.username(class="single") }}<br>
        </p>
        <p>
            {{ form.email.label }}
            <!-- Display error message if field empty or email registered -->
            {% for error in form.email.errors %}
            <span class="error"> : {{ error }}</span>
            {% endfor %}<br>
            {{ form.email(class="single") }}<br>
        </p>
        <p>
            {{ form.password.label }}
            <!-- Display error message if field empty -->
            {% for error in form.password.errors %}
            <span class="error"> : {{ error }}</span>
            {% endfor %}<br>
            {{ form.password(class="single") }}<br>
        </p>
        <p>
            {{ form.password2.label }}
            <!-- Display error message if field empty -->
            {% for error in form.password2.errors %}
            <span class="error"> : {{ error }}</span>
            {% endfor %}<br>
            {{ form.password2(class="single") }}<br>
        </p>

        <p class="button">{{ form.submit(class="button") }}</p>
    </form>
{% endblock %}
'''

# To this:

'''
{% extends "base.html" %}
{% import 'bootstrap/wtf.html' as wtf %}

{% app_content content %}
    <h1>Register</h1>
    <div class="row">
        <div class="col-md-4">{{ wtf.quick_form(form) }}</div>
    </div>
{% endblock %}
'''

# Basically, your entire form is replaced by:

# {% import 'bootstrap/wtf.html' as wtf %}
# {{ wtf.quick_form(form) }}

# In the example above the two div classes appear to be simply applying some
# width control.


# Pagination handling
# -----------------------------------------------------------------------------
# Pagination is apparently another area where Bootstrap provides direct
# support.

# Before:
'''
<div class="pagination">
    {% if prev_url %}
        <a href="{{ prev_url }}">newer posts</a>
    {% else %}
        <span class="inactive_link">newer posts</span>
    {% endif %}

    {% if next_url %}
        <a href="{{ next_url }}">older posts</a>
    {% else %}
        <span class="inactive_link">older posts</span>
    {% endif %}
</div>
'''

# Bootstrap:
'''
<nav aria-label="...">
    <ul class="pager">
        <li class="previous{% if not prev_url %} disabled{% endif %}">
            <a href="{{ prev_url or '#' }}">
                <span aria-hidden="true">&larr;</span> newer posts
            </a>
        </li>
        <li class="next{% if not next_url %} disabled{% endif %}">
            <a href="{{ next_url or '#' }}">
                older posts <span aria-hidden="true">&rarr;</span>
            </a>
        </li>
    </ul>
</nav>
'''

# TBH this is a perfect example of why I don't like pre-made CSS/HTML
# frameworks. The code here is actually less readable to me, and who knows
# what each class is doing. The amount of time it would take to study the
# documentation to figure out how to implement all this stuff in the end is
# just not worth it for someone like me who is comfortable with CSS and HTML.

# As mentioned above, you give up control when working with these things. If
# you want to change anything, it's a headache. I'd rather work with my own
# "template" than try to decrypt a foreign walled garden.
