# Build Python Web Apps with flask - Tourist Attractions

## Tourist Attractions

Whenever you travel it is fun to make a list of places you want to visit. The application you are about to create looks at making this list and organizing locations into 3 categories: recommended places to visit, decided places to visit and places that have been visited. Within each category you will have the option to move a location up to the next category and also remove a location. Lastly, there is also the option to add new locations to any of the categories.

The application consists of 7 files, but we will only work on 3 of them. Let’s go over the files we won’t be working on:

**/static/styles.css**: Basic css files to give the application some style and show off the benefits of template inheritance.

**/templates/base.html**: Template header file that the main template file will inherit from.

**data.csv**: Dummy data we will use to show of the functionality of the application as we build it.

**location.py**: A module the application will rely on to add, modify and delete location data. Our application will instantiate a ```Locations()``` class from this module. With this instance we will rely on 3 methods:
* ```add()```: Add a location to the data
* ```moveup()```: Move the location up one category
* ```delete()```: Delete a location from the data

The files we will be working with are as follows:

**app.py**: The Flask application which consists of 3 routes:
* ```locations()```: The main route which will return return content associated with each category of location. This route is also responsible for handling the changing of categories and deletion of locations.
* ```add_location()```: A form handling route which will process the add location form and then redirect back to the ```locations()``` route.
* ```index()```: This route is the same path as the ```locations()``` route but without a category variable. It will automatically redirect to the recommended page of the ```locations()``` route.

**/templates/locations.html**: Template file that displays the tourist attractions data.

**forms.py**: A module that defines the form used in the application.

Now that we have described each file, feel free to walk through them yourself before you begin. This may help you understand what is happening as we accomplish each task.

Good luck and have fun. Let’s get started!!!

## Tasks

### render_template() and Template Variables


1. To start let’s get some content in the web browser.
      
   In **app.py** replace the empty string in the return statement of the ```locations()``` route with a call to ```render_template()```, using **locations.html** as an argument.
   
2. Good job. Our web content doesn’t look like much, just a couple buttons that are part of a web form. In order to work on our template we’ll need to create some template variables and assign the application data to them. Currently our application data consists of:
   * ```category```: The URL string variable that defines the current category page.
   * ```categories```: A dictionary with the ```category``` string as the keys and display ready categories as the items.
   * ```locations```: A list of ```Location()``` objects as defined in **locations.py**. This is a list of only the locations associated with the string variable ```category```.

   In app.py add 3 variables using keyword arguments:
   1. Create template variable ```category``` and assign it the app variable ```category```
   2. Create template variable ```categories``` and assign it the app variable ```categories```
   3. Create template variable ```locations``` and assign it the app variable ```locations```

### Populate the Template

3. With access to the three variables, we can start work on the template. Let’s start with the heading of the page. We will use the ```category``` and ```categories``` variables to display a string for the page heading.
   
   Inside the ```<h1>``` tags in **locations.html** insert the ```categories``` dictionary using the ```category``` string as a key. Be sure to use expression delimiters ```{{ }}```.
   
   When you are done, if you want to change the heading replace “recommended” at the end of the URL in the browser component with "tovisit" or "visited". These are the 3 category pages we'll be working with in this project.

4. Since we have a heading that tells us what category page we’re on, let’s create an easy way to move from page to page by creating a Navbar.
   
   In **locations.html** implement the Navbar:
   1. Inside the ```<div class="navbar">``` tags create a ```for``` loop that surrounds the ```<a>``` tag
   2. Iterate through the keys and values of ```categories``` using the ```items()``` object method
   3. Set the loop variables ```category``` as each key and ```label``` as each value
   4. Inside the ```for``` loop, set the ```href``` attribute to ```category``` and the text of the link as ```label```
   
   **Be sure to**:
   * Close the for loop
   * Use statement delimiters ```{% %}``` with the for loops
   * Use expression delimiters ```{{ }}``` for the standalone variables

5. Great work! You can now move to each category page using the Navbar. Let’s now populate the list of locations in each category using the ```locations``` variable.

   In **locations.html** implement the locations list:
   1. Inside the ```<tbody class="loctable">``` tags create a for loop that surrounds the ```<tr>``` tags
   2. Iterate through the objects in ```locations``` and define a loop variable ```location```
   3. Inside the ```<td class="loc">``` tags insert the ```name``` attribute of the ```location``` object
   4. Inside the ```<td class="desc">``` tags insert the description attribute of the ```location``` object

   **Be sure to**:
   * Close the for loop
   * Use statement delimiters ```{% %}``` with the for loops
   * Use expression delimiters ```{{ }}```

6. In the web browser component, to the right of each location description is a pair of buttons: one to move the location up one and one to delete the location. In the template these are ```<input type="submit"``` tags which are in the ```<form>``` that is inside the 3rd ```<td>``` tag. We need to add a little more info to the form in order for our application to work.
   
   In **locations.html** add the location name to each of the input elements. You can do this by setting the name attribute for each ```<input type="submit"``` in the form to the ```name``` attribute of the ```location``` object.

   **Be sure to**:
   * Use expression delimiters ```{{ }}```

7. We now have a clear heading to tell us what category page we’re on, a Navbar, a list of locations and buttons to perform actions on our locations. The button functionality is unnecessary for the visited locations, so let’s keep them from appearing on that page.

   In **locations.html** implement an ```if``` statement to only have the Move Up and Delete buttons on the "recommended" and "tovisit" pages:
   1. Inside the ```<td class="btns">``` tags create an if statement that surrounds the ```<form>``` tags.
   2. The if condition should check if the ```category``` attribute of the location object is in this list: ```["recommended", "tovisit"]```

   **Be sure to**:
   * Close the if statement
   * Use statement delimiters ```{% %}``` with the if statement

8. Now that the first part of the template is finished, let’s use inheritance to complete the template and add some styling to the page.

   In **locations.html** inherit from another template:
   1. At the top of **locations.html** insert an ```extends``` statement that extends **base.html**
   2. Now surround the rest of the content in **locations.html** with a ```block``` statement named ```content```

   **Be sure to**:
   * Surround the filename with quotes
   * Close the ```block``` statement
   * Use statement delimiters ```{% %}``` with the extends and block statements.

### Handle the Move Up and Delete Form

9. When the user pushes one of the location form buttons, a request will be sent to the server with ```name``` and ```value``` attributes of the associated ```<input>```. One way to test for a form submission in our application is to test the method attribute of the request object. If the ```method``` is ```"POST"``` we know a form has been submitted.
    
    In **app.py** test for a form submission. Inside the ```locations()``` route function replace the ```False``` condition of the ```if``` statement with a check that the ```request``` object's ```method``` attribute equals ```"POST"```

10. Excellent! Now we need to collect the data in order to process it. If you look in the ```locations()``` route function of **app.py** you will see that some of the data processing has been done already. The two things to know about the submitted data are that the ```form``` attribute of the request object is a dictionary and it will only contain one key-value pair within it. Knowing this we can use the ```items()``` method to extract that pair using a single line of code.

    In **app.py** collect the ```name``` and ```value``` data from the submitted form. Replace the ```[(None, None)]``` statement with the output of the ```items()``` method of the ```request``` objects ```form``` attribute.

    When you are done you can test out the functionality by clicking the buttons next to each location. If you delete all the data you can refresh it by running the code again.


### Create A Form in Python

11. Amazing! Already this is a properly functioning application.
    
    Now it is time for us to create a form to add a location. We’ll define the form in the **forms.py** file and add a name field, a description field, radio buttons for the category and a submit button.

    Note: Provided in **forms.py** is a new form class, ```FieldsRequiredForm```, that inherits from ```FlaskForm```. This new type of form will allow us to require data for radio button form fields.

    In **forms.py** start by defining the form and adding a ```StringField```
    1. Create a form class named ```AddLocationForm()``` that inherits from ```FieldsRequiredForm```
    2. Define an attribute name and assign it an instance of ```StringField()``` with the label ```"Location Name"``` and a ```DataRequired()``` validator.

12. Good job! Now let’s complete the form.

    In **forms.py** create 3 more field attributes:
    1. Define an attribute ```description``` and assign it an instance of ```TextAreaField()``` with the label ```"Location Description"``` and a ```DataRequired()``` validator.
    2. Define an attribute category and assign it an instance of ```RadioField()``` with the label ```"Category"``` and set ```choices``` equal to the defined variable ```categories```
    3. Define an attribute ```submit``` and assign it an instance of ```SubmitField()``` with the label ```"Add Location"```

13. Now that the form is done let’s set it up in our application so we can implement it in the template.

    In **app.py** import the form and assign it to a template variable:
    1. Write an import statement that imports ```AddLocationForm``` from the forms file. Reference the ```locations``` import statement if necessary.
    2. Note that ```app.config['SECRET_KEY']``` is already set. Remember this is necessary to protect against a Cross-Site Request Forgery attack
    3. Now define a template variable in the call to ```render_template()``` within the ```locations()``` route. The template variable should be named ```add_location``` and assign it an instance of ```AddLocationForm()```

### Implement the Form in the Template

14. Now that we have access to the form in the template we need to tell the form what route will be handling the submission. We also need to implement the other part of the CSRF protection by inserting the form’s ```hidden_tag()``` method.
    
    In **locations.html** initialize the add location form:
    1. Inside the ```<form class="addform">``` tag set the ```action``` attribute to ```url_for()``` with the add_location route as an argument
    2. On the following line use the form template variable ```add_location``` and call the ```hidden_tag()``` method

    **Be sure to**:
    * Use ```url_for()``` inside double quotes
    * Use single quotes for the route function name
    * Use expression delimiters ```{{ }}```

15. The structure of the form is created using an HTML table. The first row will be for the labels, the second for the fields and the third for the submit button.

    In **locations.html** populate the first row of the table with the field labels:
    1. Insert the ```name``` field ```label``` into the first ```<td>``` tag using the ```add_location``` template variable
    2. Insert the ```description``` field ```label``` into the second ```<td>``` tag using the ```add_location``` template variable
    3. Insert the ```category``` field ```label``` into the third ```<td>``` tag using the ```add_location``` template variable

    **Be sure to**:
    * Use expression delimiters ```{{ }}```

16. Now we'll move onto inserting the name and description fields into the second row of the table.

    In **locations.html** start to populate the second row of the table with the below fields:
    1. Insert the ```name``` field into the first ```<td>``` tag of the second row using the ```add_location``` template variable
    2. Insert the ```description``` field into the second ```<td>``` tag of the second row using the ```add_location``` template variable

    **Be sure to**:
    * Use expression delimiters ```{{ }}```

17. For the ```category``` ```RadioField()``` buttons we need to iterate through the variable to insert the button elements
    
    In **locations.html** populate the third ```<td>``` column of the second row of the table with the ```RadioField()``` elements:
    1. Create a for loop inside the third ```<td>``` tag in the second row, making sure to surround the ```<div>``` tags
    2. Iterate through the ```category``` field using the ```add_location``` template variable and create a loop variable button
    3. Inside the ```<div>``` tags insert the field using the loop variable ```button```
    4. On the same line insert the field ```label``` using the loop variable button

    **Be sure to**:
    * Close the for loop
    * Use statement delimiters ```{% %}``` with the for loops
    * Not use parentheses ```()``` when iterating through the ```category``` variable
    * Use expression delimiters ```{{ }}``` for the standalone variables

18. Now let's finish the form with the submit button.
    
    In **locations.html** populate the third row with an ```add_location``` button. Insert the ```submit``` field into the single ```<td>``` tag of the third row using the ```add_location``` template variable.

    **Be sure to**:
    * Use expression delimiters ```{{ }}```

### Collect Form Data and Finalize Applicaiton

19. Great work! Now let's finish the application off by implementing the form collection.
    
    In **app.py** inside the ```add_location``` route function create a form instance and validate the submission:
    1. Create an ```AddLocationForm()``` instance with the argument ```csrf_enabled=False``` and assign it to a variable named ```add_form```.
    2. Replace the ```True``` condition with the form instance’s ```validate_on_submit()``` function

20. Now its time to collect the data!
    
    In **app.py** inside the ```add_location()``` route and within the ```if``` statement, collect the form data:
    3. Replace the ```None``` and assign the variable ```name``` to the ```name``` field ```data```
    4. Replace the ```None``` and assign the variable ```description``` to the ```description``` field ```data```
    5. Replace the ```None``` and assign the variable ```category``` to the ```category``` field ```data```

21. When a location is added we want to redirect to the category page the location was added. We will also set up a redirect from the ```/``` path without a variable.
    
    In **app.py** use ```redirect()``` to complete the application flow:
    1. In the ```add_location()``` route function replace the empty string in the ```return``` statement with ```redirect()```
    2. As the argument for ```redirect``` use ```url_for()``` and pass the locations route function and set the ```category``` keyword argument to the local variable ```category```. Set the ```_external``` and ```_scheme``` keyword arguments to load an HTTPS URL.
    3. In the ```index()``` route function replace the empty string in the ```return``` statement with ```redirect()```
    4. As the argument for ```redirect``` use ```url_for()``` and pass the locations route function and set the ```category``` keyword argument to ```"recommended"```. Set the ```_external``` and ```_scheme``` keyword arguments to load an HTTPS URL.

## Solucion completa

[Link solucion](https://gist.github.com/codecademydev/a9a5c7e0df46ad351b8e0f67306c2489)

```
python -m venv myapp
cd myapp
```
