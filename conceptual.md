### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
The important differences between Python and Javascript boil down to use case. Javascript is a powerful object oriented language, but it is mainly used in web development and front end applications. Python is an easier to read but equally as powerful if not more powerful language, capable of general programming and back end development. 

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
Using the get() method is an easy way to mitigate errors when looking for a value in an iterable. 
Another way could be just using a try and catch in Javascript or a try and except in Python.


- What is a unit test?
A unit test is testing a very small snippet of code such as a single function call for an expected return.

- What is an integration test?
Integration testing involves testing larger portions of code at once, such as adding in a new class and seeing if it does what is expected.

- What is the role of web application framework, like Flask?
The role of a web application framework like Flask is to help create a web application easier, and quicker than doing it without. They provide tools and methods for handling web pages without having to input things manually.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
Passing information to Flask through URL routes can be more encrypted and result in shorter URLs in general. Query params are seen and can become quite long. In general if there are required parameters using a route is preferable, however, when there are optional parameters a URL query parameter may be preferable.

- How do you collect data from a URL placeholder parameter using Flask?
By providing a placeholder variable in the route path corresponding the URL, and then using the variable accordingly.

- How do you collect data from the query string using Flask?
By using request.args[] method built into Flask

- How do you collect data from the body of the request using Flask?
By using request.data

- What is a cookie and what kinds of things are they commonly used for?
A cookie is data that is both shared and held locally by the client and the server. They are commonly used for things like login information or shopping cart information. 

- What is the session object in Flask?
The session object utilizes cookies, and should not be mistaken with the built in session on browsers. Sessions on flask allow us to encrypt and store data.

- What does Flask's `jsonify()` do?
Flasks jsonify helps convert data into a json formatted string and is retrievable later. It works with iterables and works to retrieve them as iterables.
