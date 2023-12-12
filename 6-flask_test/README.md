# Ensayos Flask

- [ ] Aprender el procedimiento basico
- [ ] Documentar lo que se pueda sobre el procedimiento basico
- [ ] Montar ejemplo Flask

![http_request_codeacademy](https://content.codecademy.com/courses/updated_images/NodeBackEndFrontEnd_Update_1.gif)

![relational_no_relational](https://content.codecademy.com/courses/updated_images/Node_4_v4_Updated_1.svg)

![API](https://content.codecademy.com/courses/updated_images/Node_5v2__Updated_1.gif)

![Authorization_and_Authentication](https://content.codecademy.com/courses/server-side-web-dev/NodeAnimation_6.gif)

**Nota**: Todo este contenido se tomo de codecademy.com

In order to have consistent ways of interacting with data, a back-end will often include a web API. API stands for Application Programming Interface and can mean a lot of different things, but a web API is a collection of predefined ways of, or rules for, interacting with a web application’s data, often through an HTTP request-response cycle. Unlike the HTTP requests a client makes when a user navigates to a website’s URL, this type of request indicates how it would like to interact with a web application’s data (create new data, read existing data, update existing data, or delete existing data), and it receives some data back as a response.


Unlike the front-end, which must be built using HTML, CSS, and JavaScript, there’s a lot of flexibility in which technologies can be used in order to create the back-end of a web application. Developers can construct back-ends in many different languages like PHP, Java, JavaScript, Python, and more.

You don’t need to reinvent the wheel to create a robust back-end. Instead, most developers make use of frameworks which are collections of tools that shape the organization of your back-end and provide efficient ways of accomplishing otherwise difficult tasks.

The collection of technologies used to create the front-end and back-end of a web application is referred to as a stack. This is where the term full-stack developer comes from; rather than working in either the front-end or the back-end exclusively, a full-stack developer works in both.

## Review

In order to deliver the front-end of a website or web application to a user, a lot needs to happen behind the scenes on the back-end! Understanding what makes up the back-end can be overwhelming because the back-end has a lot of different parts, and different websites or web applications can have dramatically different back-ends.

![imagen_completa](https://content.codecademy.com/courses/server-side-web-dev/Node_8.svg)

We covered a lot in this lesson, so let’s review what we learned:

* The front-end of a website or application consists of the HTML, CSS, JavaScript, and static assets sent to a client, like a web browser.
* A web server is a process running on a computer somewhere that listens for incoming requests for information over the internet and sends back responses.
* Storing, accessing, and manipulating data is a large part of a web application’s back-end
* Data is stored in databases which can be relational databases or NoSQL databases.
* The server-side of a web application, sometimes called the application server, handles important tasks such as authorization and authentication.
* The back-end of web application often has a web API which is a way of interacting with an application’s data through HTTP requests and responses.
* Together the technologies used to build the front-end and back-end of a web application are known as the stack, and many different languages and frameworks can be used to build a robust back-end.



## Diferentes terminos

* HTTP Requests [[link]](https://www.codecademy.com/article/http-requests)
* HTTP Requests [[link]](https://www.codecademy.com/paths/build-python-web-apps-flask/tracks/introduction-to-flask/modules/introduction-to-flask/articles/http-requests)
* What is REST? [[link]](https://www.codecademy.com/article/what-is-rest)
* HTTP Errors: 404 [[link]](https://www.codecademy.com/article/http-errors-404)
* What is a Relational Database Management System? [[link]](https://www.codecademy.com/article/what-is-rdbms-sql)
* SQL:
  * MySQL
  * PostgreSQL 
* NoSQL:
  *  MongoDB
  *  Redis
* API:
  * https://developers.facebook.com/docs/instagram
* Different Back-end Stacks
    
  |Framework|Language|
  |---|---|
  |Laravel|	PHP|
  |Express.js|	JavaScript (runs in the Node environment)|
  |Ruby on Rails|	Ruby|
  |Spring|	Java|
  |JSF|	Java|
  |Flask|	Python|
  |Django|	Python|
  |ASP.NET|	C#|
* Stack
  * MEAN (MongoDB, Express.js, AngularJS, Node.js) [[MEAN (solution stack)]](https://en.wikipedia.org/wiki/MEAN_(solution_stack)) 
  * LAMP ((Linux, Apache, MySQL, PHP/Perl/Python)  [[LAMP (software bundle)]](https://en.wikipedia.org/wiki/LAMP_(software_bundle))

## Usando Flask

**Referencia principal**: Introduction to Flask ([link](https://www.codecademy.com/learn/paths/build-python-web-apps-flask/tracks/introduction-to-flask/modules/introduction-to-flask/cheatsheet))

### Variable rules

```py
@app.route('/orders/<user_name>/<int:order_id>')
def orders(user_name, order_id):
    return f'<p>Fetching order #{order_id} for {user_name}.</p>'
```

Note that we can also optionally enforce the type of the variable being accepted using the syntax: ```<converter:variable_name>```. The possible converter types are:

|string|accepts any text without a slash (default)|
|---|---|
|int|accepts positive integers|
|float|accepts positive floating point values|
|path|like string but also accepts slashes|
|uuid|accepts UUID strings|




## Referencias

1. https://blog.adafruit.com/2017/07/07/create-a-basic-python-web-server-with-flask-piday-raspberrypi-raspberry_pi/
2. https://learn.adafruit.com/raspipe-a-raspberry-pi-pipeline-viewer-part-2/miniature-web-applications-in-python-with-flask
3. https://www.sparkfun.com/wish_lists/141975
4. https://learn.sparkfun.com/tutorials/using-flask-to-send-data-to-a-raspberry-pi
5. https://www.sparkfun.com/news/3360
6. https://www.sparkfun.com/python
7. https://github.com/sparkfun/SparkFun_SPI_SerialFlash_Arduino_Library
8. https://realpython.com/tutorials/flask/
9. https://realpython.com/learning-paths/flask-by-example/
10. https://realpython.com/html-css-python/
11. https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Web_frameworks#a_few_good_web_frameworks
