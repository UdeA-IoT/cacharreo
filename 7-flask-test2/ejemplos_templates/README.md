# Ejemplos templates

>> **Cheatsheets/Introduction to Flask**: [Jinja2 Templates and Forms](https://www.codecademy.com/learn/paths/build-python-web-apps-flask/tracks/introduction-to-flask/modules/flask-templates-and-forms/cheatsheet)

## 01 - Introduction

When you navigate through a website you may notice that many of the pages on the site have a similar look and feel. This aspect of a website can be achieved with the use of templates. In this lesson the term template refers to an HTML file that can represent multiple web pages with the same structure and functionality.

We will be using the Flask framework for our application in this lesson. Flask uses the Jinja2 template engine to render HTML files that include application variables and control structures. The [Jinja2 template engine](https://jinja.palletsprojects.com/en/2.11.x/) is a powerful tool that supports an organized and growth oriented application.

In this lesson we will look at:
* How to organize our site file structure
* Use our application data with our templates
* Leverage control structures within our templates
* Share common elements across many templates

The application we will be building in the following exercises is a cookbook site that consists of a main page and individual recipe pages. Currently our app consists of 2 routes that return HTML strings for the browser to display. Explore the application to begin your path to learning templates!

## 02 - Rendering Templates

Having routes return full web pages as strings is not a realistic way to build our site. Containing our HTML in files is the standard and more organized approach to structuring our web app.

To work with files, which we will call templates, we use the Flask function ```render_template()```. Used in the return statement, this function takes a template file name as an argument and returns the content to send to the client. It uses the Jinja2 template engine to generate HTML using the template file as blueprint.

```py
return render_template("my_template.html")
```

```py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
```

## 03 - Template Variables

```py
flask_variable = "Text for my template"

render_template("my_template.html", 
                 template_variable=flask_variable)

```

```py
render_template("my_template.html", 
                template_var1="A string!", 
                template_var2=100)
```

```html
{{ template_variable }}
```

```html
<h1>My Heading: {{ template_variable }}</h1>
```

```html
<p>Template number plus ten: {{ template_variable + 10 }}</p>

OUTPUT
Template number plus ten: 30
```

```html
<p>Element at index 1: {{ template_list[1] }}</p>

OUTPUT
Element at index 1: B
```

## 04 - Variable Filters

```html
{{ variable | filter_name }}
```

```html
{{ template_heading |  title }}

OUTPUT
My Very Interesting Website
```

```html
{{ no_template_variable | default("I am not from a variable.") }}

OUTPUT
I am not from a variable.
```

The ```default``` filter does not work on empty strings ```""``` or ```None``` values. We will look at this scenario in the next exercise.

While filters perform more complex functions than simple operators, they are still small, focused actions. Here is a list of commonly applied filters and their descriptions. More information can be found in the [Jinja2 documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/#builtin-filters)
* ```title```: Capitalizes the first letter of each word in a string, known as titlecase
* ```capitalize```: Capitalizes the first character of a string, such as in a sentence
* ```lower/upper```: Makes all the characters in a string lowercase/uppercase
* ```int/float```: Changes any number variable to an integer/float
* ```default```: Defines a default string if the variable is not defined
* ```length```: Calculates the length of a string, list or dictionary variable
* ```dictsort```: Sorts a dictionary by its keys

## 05 - If Statements

```html
{% if condition %}
  <p>This text will output if condition is True</p> 
{% endif %}
```

```html
{% if template_variable == "Hello" %}
  <p>{{template_variable}}, World!</p> 
{% endif %}
```

```html
{% if template_number < 20 %}
  <p>{{ template_number }} is less than 20.</p> 
{% elif template_number > 20 %}
   <p>{{ template_number }} is greater than 20.</p> 
{% else %}
   <p>{{ template_number }} is equal to 20.</p> 
{% endif %}

OUTPUT
20 is equal to 20.
```

## 06 - For Loops

```html
<ol>
{% for x in range(3) %}
  <li>{{ x }}</li>
{% endfor%}
</ol>

OUTPUT
1. 0
2. 1
3. 2
```

**Iterate through a list variable**:

```html
{% for element in template_list %}
```

**Iterate through a string**:

```html
{% for char_in_string in “Hello!” %}
```

**Iterate through the keys of a dictionary variable**:

```html
{% for key in template_dict %}
```

**Iterate through keys AND values of a dictionary with ```items()```**:

```html
{% for key, value in template_dict.items() %}
```

## 07 - Inheritance

**base.html**:

```html
<html>
  <head>
    <title>MY WEBSITE</title>
  </head>
  <body>
  {% block content %}{% endblock %}
  </body>
</html>
```

**index.html**:

```html
{% extends "base.html"  %}

{% block content %}
    <p>This is my paragraph for this page.</p>
{% endblock %}
```

El resultado de renderizar **index.html**: es el siguiente:

```html
<html>
  <head>
    <title>MY WEBSITE</title>
  </head>
  <body>
    <p>This is my paragraph for this page.</p>
  </body>
</html>
```

## 08 - Review

Congratulations, this concludes the lesson on Flask templates. In this lesson we:
* Created a file structure that works with the Jinja2 template engine
* Rendered pages in our browser using files called templates
* Shared our application data for use within templates
* Applied filters to our data within our templates
* Utilized if statements to bring decision making to our templates
* Implemented for loops to perform repetitive tasks in our templates
* Moved common content to separate files to be shared by many templates

To show the power of what we have learned let’s add a simple navigation bar to the app.