# Arganic

{==

***Arganic*** is a lightweight **Python library** making it easy to manage **Arguments** for **Classes**, **Methods** or **Functions**.

==}

The library provides a very simpel and comprehensive set of decorators with advanced features such as
**required arguments**, **validators**, **type checking**,
**read/write accesses**, **default values**, and **choices**.

By leveraging Python's `*args` and `**kwargs`, *Arganic*
empowers developers to enhance the readability and functionality of
their codebase with ease.

## Key Features:

 - **Decorators for Classes, Methods, and Functions**: Apply decorators to classes, methods, and functions to extend their functionality and behavior.
 - **Required Parameters:** Define required parameters for methods and functions to ensure essential inputs are provided.
 - **Validator Support:** Validate method arguments, function parameters, and class properties using built-in or custom validators.
 - **Type Checking:** Enforce type constraints and ensure type consistency with flexible type checking capabilities.
 - **Read/Write Access Control:** Define read-only properties for classes, methods, and functions as needed.
 - **Default Values:** Set default values for function arguments, method parameters, and class properties to streamline code logic.
 - **Choice Selection:** Specify a list of choices for method arguments and function parameters, restricting input values to predefined options.

<p style="text-align: center" markdown>
 [Read the full documentation](https://kiwea.github.io/Arganic/){ .md-button .md-button--primary }
</p>
## Installation

### Pip

Install Arganic via the pip command:

    pip install arganic

### Git clone

Clone the github repository:

    git clone https://github.com/Kiwea/arganic

## Usage

### Decorating Classes

Example on how to decorate a Class and access the arguments as class properties.

Note: the class need to extends ArgumentHandler to implement get and set methods.

``` py title="A simple Vehicle class with three arguments/properties."
--8<-- "examples/class_vehicles.py"
```

### Decorating Methods

Example with a class method decorator

``` py title="A simple method with two arguments."
--8<-- "examples/class_method_drive.py"
```

### Decorating functions

The same example with a simple function.

``` py title="A simple function with two arguments."
--8<-- "examples/function_drive.py"
```

### Arguments parameters

List of the available parameters the Arguments class can take:

 - ***default***: (Any, optional) - The default value of the argument.
 - ***read_only***: (bool, Default=True) - The default value of the argument.
 - ***required***: (bool, default=True) – Whether the argument is required.
 - ***type***: (Type | tuple[Type], optional) – The data type(s) the argument value can take.
 - ***validator***: (Validator | tuple[Validator], optional) – A Validator object or list of Validator objects used to validate the argument value.
 - ***choices*** (tuple, optional) – A tuple of choices the argument value can take.

### Custom validators

It's possible to define your own validators by extending the Validator class.

``` py title="A custom validator example."
--8<-- "examples/custom_validator.py"
```

## Contributing

This project is open to contributors :

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

Submit a push request

Issues

If you find a bug, please post an issue on the [issue tracker on GitHub](https://github.com/Kiwea/Arganic/issues).

To help reproduce the bug, please provide a minimal reproducible example, including a code snippet and the full error message.
