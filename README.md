# Arganic

***Arganic*** is a simple and lightweight **Python library** making it easy to manage **Arguments** for **Classes**, **Methods** or **Functions**.

The library provides a very simple and comprehensive set of decorators with advanced features such as
**required arguments**, **validators**, **type checking**,
**read/write accesses**, **default values**, and **choices**.

By leveraging Python's `*args` and `**kwargs`, *Arganic*
empowers developers to enhance the readability and functionality of
their codebase with ease.

[**Read the full documentation**](https://kiwea.github.io/Arganic/)

## Key Features:

 - **Decorators for Classes, Methods, and Functions**: Apply decorators to classes, methods, and functions to extend their functionality and behavior.
 - **Required Parameters:** Define required parameters for methods and functions to ensure essential inputs are provided.
 - **Validator Support:** Validate method arguments, function parameters, and class properties using built-in or custom validators.
 - **Type Checking:** Enforce type constraints and ensure type consistency with flexible type checking capabilities.
 - **Read/Write Access Control:** Define read-only properties for classes, methods, and functions as needed.
 - **Default Values:** Set default values for function arguments, method parameters, and class properties to streamline code logic.
 - **Choice Selection:** Specify a list of choices for method arguments and function parameters, restricting input values to predefined options.

### Decorators

Arganic provides 3 distinct types of decorators:

 - `@class_properties` : A decorator for class properties allowing you to define the data managed by the class during construction and then access these values within the class.
 - `@method_arguments` : A decorator for class methods allowing you to constrain the arguments provided during the call but also to find the correctly formatted values within the method.
 - `@function_arguments` : A decorator for functions allowing you to constrain the arguments provided during the call but also to find the correctly formatted values within the function.


## Installation

### Pip

Install Arganic via the pip command:


    pip install arganic


### Git clone

Clone the github repository:

    git clone https://github.com/Kiwea/arganic

## Contributing

This project is open and gratefully accepts any form of contribution.

### Contributing to the code

Create a virtual env:

    cd Arganic
    python -m venv venv
    source venv/bin/activate

Test the code:

    pytest --cov=arganic/

Create a feature branch:

    git checkout -b my-feature

Add your code and test it again
Update the documentation under the docs/

    mkdocs serve

Submit a push request...

### Issues

If you find a bug, please post an issue on the [issue tracker on GitHub](https://github.com/Kiwea/Arganic/issues).

To help reproduce the bug, please provide a minimal reproducible example, including a code snippet and the full error message.
