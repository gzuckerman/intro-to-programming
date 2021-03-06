Turtles
*******

Turtle objects know how to draw. Here we explore creating and
manipulating them to draw on the screen.

We also look at the two ways the `python3` interpreter can execute your python code:

* The interactive interpreter
* Calling the python interpreter on a file that contains code.

.. tip::

    Don't just read! Type everything and experiment.


Interactive interpreter 
=======================

We launch the python interpreter through `cmd.exe`:

1. Press the two keys 'Windows + R' together
2. Enter `cmd.exe` in the search prompt and enter.

A window will appear with a prompt:: 

    C:\Users\greg-lo>

Type `python3` to enter the interactive shell::

    C:\Users\greg-lo>python
    Python 3.4.2 (v3.4.2:8711a0951384, Sep 21 2014, 21:16:45) [MSC v.1600 32 b
    it (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.

    >>> print('Hi') 


Now type::

    >>> from turtle import Turtle
    >>> tess = Turtle()

.. image:: /images/turtle-init.png

::

    >>> tess.forward(100)

.. image:: /images/turtle-forward.png

::

    >>> tess.left(30)

.. image:: /images/turtle-left.png

Lets call some more methods on the tess our turtle object::

    >>> tess.shape('turtle')
    >>> tess.color('green')
    
Lets create 'bob' a new turtle object::

    >>> bob = Turtle()
    >>> bob.shape('circle')
    >>> bob.color('red')
    >>> bob.backward(100)


Exercise
--------

Experiment drawing shapes in different colours.

Documentation
-------------

Visit the `turtle` online documentation and explore what Turtle objects can do. 

|turtle_docs|

.. |turtle_docs| raw:: html

    <a href="https://docs.python.org/3/library/turtle.html" target="_blank">https://docs.python.org/3/library/turtle.html</a>


Questions:

* What different colors does a turtle's `color` method recognise?
* What shapes does a trutle's `shape` method recognise?

Find some new turtle object methods and experiment.

.. tip::

    As you experiment you will want to do know how to do new things. Get into
    the habit of exploring the documenation to see what you can do.


Turtles
=======

Lets revise what we have learnt in the light of object oriented terminology.

An object can be created. It has a type, and this type determines its methods
(behaviours).

Creation
--------

::

    >>> from turtle import Turtle
    >>> tess = Turtle()

Breakdown:

1. We import an object called Turtle from somewhere called turtle. 
2. Turtle is called, creates a new object of type turtle, and returns it.
3. This returned object is assigned to the name tess.

.. tip::
    We call an object by adding parenthesis at the end of its name. Here the
    parenthesis are empty but then often aren't.

Lets confirm the type of tess::

    >>> type(tess)
    turtle.Turtle

.. tip:: 
    The function `type` returns the type of a passed object.

Turtle is a special kind of object in that it produces new objects. We call it
a constructor object.

Methods
-------

Methods are functions attached to objects. We will explore functions later.

::

    >>> tess.forward(100)

Braces `()` have a special meaning. They indicate calling. You can think of
this as effecting an action.

The effect of calling the method `forward` on an object of type `Turtle` is to
draw a line.

What other methods (behaviours) do turtle objects have?

Code in files
=============

Most code is written and executed from a file. 

Using SublimeText create a file named `my_turtle_file.py` with this code:: 

    from turtle import Turtle, exitonclick

    tess = Turtle()
    tess.shape("turtle")
    tess.forward(100)

    exitonclick()  # Why this? Experiment by commenting it out.

.. tip::

    All word document file names end with .doc, 
    all files names with python code must end with .py

In cmd.exe call the python command with the filename `my_turtle_file.py` as parameter::
  
    C:\Users\greg-lo> python3 my_turtle_file.py


.. tip::

    Make sure the file you created exists in the location where you execute this
    command. The location is given by the prompt.

Questions/Practicals
--------------------

1. What are the differences between using `python3` interactively and using files? When would you use one or the other?

2. Challenge yourself to find as many different ways of drawing with a turtle object.

3. Take your time to draw something useful and/or crazy.



Shape Exercises
===============

Lets program some shapes. We do this by breaking down into step by step instructions principles of geometry.

Put all code inside a file named `shapes.py` to be executed using::
    
    python shapes.py


Shapes:

* Draw a square as in the following picture. 
  
.. tip:: Squares have right angles which are 90 degrees.

.. image:: /images/turtle-square.png


* Draw a rectangle.

.. image:: /images/turtle-rectangle.png


* Draw an equilateral triangle. 

.. tip:: An equilateral triangle has 3 sides of equal length and each corner has an angle of 60 degrees.

* Draw many squares. Each square should be tilted left of the previous. 

.. image:: /images/turtle-many-squares.png

Experiment with the angles between the individual squares. The picture shows three 20 degree turns. You could try 30 and 40...

* Draw a simple house.

.. tip:: Reuse the code you have already written.

