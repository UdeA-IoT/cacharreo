# Ejemplos forms


>> **Cheatsheets/Introduction to Flask**: [Jinja2 Templates and Forms](https://www.codecademy.com/learn/paths/build-python-web-apps-flask/tracks/introduction-to-flask/modules/flask-templates-and-forms/cheatsheet)


## 01 - Introduction

The use of forms in a site can be an involved process. The designer must gather the right information, display the fields in a pleasing manner and ensure the data is collected correctly. Over the years this has become easier thanks to frameworks like Flask, which help streamline the process of displaying fields and gathering data.

## 02 - Flask Request Object

```py
@app.route("/", methods=["GET", "POST"])
```


```py
from flask import request
```


```py
text_in_field = request.form["my_text"]
```

## 03 - Route Selection

```py
@app.route('/')
def index:
```

```html
<a href="/">Index Link</a>

<a href="{{ url_for('index') }}">Index Link</a>
```

```html
<a href="{{ url_for('my_page', id=1) }}">One</a>
```

```py
@app.route("/my_path/<int:my_id>"), methods=["GET", "POST"])
def my_page(my_id):
    # Access flask_name in this function
    new_variable = my_id
    ...
```

## 04 - FlaskForm Class

```py
class MyForm(FlaskForm):
    my_textfield = StringField("TextLabel")
    my_submit = SubmitField("SubmitName")
```

```py
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret"

class MyForm(FlaskForm):
    my_textfield = StringField("TextLabel")
    my_submit = SubmitField("SubmitName")

@app.route("/")
def my_route():
    flask_form = MyForm()
    return render_template("my_template", template_form=flask_form)
```

```py
app.config["SECRET_KEY"] = "my_secret"
```

## 05 - Template Form Variables

```py
class MyForm(FlaskForm):
    my_textfield = StringField("TextLabel")
    my_submit = SubmitField("SubmitName")

```

```py
my_form = MyForm()

return render_template(template_form=my_form)
```

```html
<form action="/" method="post">
    {{ template_form.hidden_tag() }}
    {{ template_form.my_textfield.label }}
    {{ template_form.my_textfield() }}
    {{ template_form.my_submit() }}
</form>
```

```html
<form action="/" method="post">
    <input id="csrf_token" name="csrf_token" type="hidden" value="ImI1YzIxZjUwZWMxNDg0ZDFiODAyZTY5M2U5MGU3MTg2OThkMTJkZjQi.XupI5Q.9HOwqyn3g2pveEHtJMijTu955NU">
    <label for="my_textfield">TextLabel</label>
    <input id="my_textfield" name="my_textfield" type="text" value="">
    <input id="my_submit" name="my_submit" type="submit" value="SubmitName">
</form>
```

## 06 - Handling FlaskForm Data

```py
form_data = flask_form.my_textfield.data
```

```py
methods=["GET", "POST"]
```

## 07 - Validation

```py
from wtforms.validators import DataRequired
```

```py
my_textfield = StringField("TextLabel", validators=[DataRequired()])
```

```py
if my_form.validate_on_submit():
    # get form data
```

## 08 - More Form Fields

### TextAreaField

```py
#### Form class declaration
my_text_area = TextAreaField("Text Area Label")
```

### BooleanField

```py
#### Form class declaration
my_checkbox = BooleanField("Checkbox Label")
```

### RadioField

```py
#### Form class declaration
my_radio_group = RadioField("Radio Group Label", choices=[("id1", "One"), ("id2","Two"), ("id3","Three")])
```

## 09 - Redirecting

```py
redirect("url_string")
```

```py
redirect(url_for("new_route", _external=True, _scheme='https'))
```

```py
redirect(url_for("new_route", new_var=this_var, _external=True, _scheme='https'))
```


## 10 - Review

In this lesson we learned:
* How to access form data using the ```request``` object
* Control path selection with route function names using ```url_for()```
* Create a web form structure using ```FlaskForm``` and WTForm fields
* Create a web form in the templates using ```FlaskForm``` variables
* Utilize field validators for increased data integrity
* Use ```redirect()``` to change paths easily within the app

Being able to utilize Python classes to handle forms is a very efficient process. Organizing form data using the functionality of FlaskWTF and WTForms can be easily achieved.

Navigate through the site and review the files to look at what you accomplished in this lesson.