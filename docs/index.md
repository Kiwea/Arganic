# Arganic

{==

***Arganic*** is a simple and lightweight **Python library** making it easy to manage **Arguments** for **Classes**, **Methods** or **Functions**.

==}

The library provides a very simple and comprehensive set of decorators with advanced features such as
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

``` bash
pip install arganic
```

### Git clone

Clone the github repository:

``` bash
git clone https://github.com/Kiwea/arganic
```

## Usage

### Decorators

Arganic provides 3 distinct types of decorators:

 - `@class_properties` : A decorator for class properties allowing you to define the data managed by the class during construction and then access these values within the class.
 - `@method_arguments` : A decorator for class methods allowing you to constrain the arguments provided during the call but also to find the correctly formatted values within the method.
 - `@function_arguments` : A decorator for functions allowing you to constrain the arguments provided during the call but also to find the correctly formatted values within the function.

### Decorating Class and Method

Example of a `class decorator` and a `method` of the same class, they can be used independently or together.

When initializing the class or calling the method, the values provided will be validated according to the parameters provided in the decorator.

!!! info

    It is important to note that if we wish to decorate a class, it must extend the base class [`ArgumentHandler`][arganic.arguments.ArgumentHandler],
    so it will implement the methods [`set()`][arganic.arguments.ArgumentHandler.set], [`get()`][arganic.arguments.ArgumentHandler.get] and the property
    [`values`][arganic.arguments.ArgumentHandler.values] allowing access to property values.

Within the method it is also possible to access the values of the arguments and thus benefit from the processing carried out, such for example as finding
a `default value` if no one was provided from the call.

!!! info

    It's also important to note that the `methods`, `functions` or `classes` that are decorated have the arguments `*args` and `**kwargs` declared in their signatures. 
    Currently support for other arguments in the signature is not supported.

``` py title="A simple Vehicle class decorated with three properties, and his decorated method drive() ." linenums="1" hl_lines="9-22 34-41"
--8<-- "tests/examples/class_vehicle.py"
```

### Decorating Class, Method and a function

Another example with also a simple function and some validating options.

``` py title="Another full-featured example decorating Class, Method and Function." linenums="1" hl_lines="18-40 50-69 74-82"
--8<-- "tests/examples/decorated.py"
```

### Arguments parameters

Another example of a class decorated with a full-featured property.

List of the available parameters the [`Argument`][arganic.arguments.Argument] can take:

 - [***default***][arganic.arguments.Argument.default]: (`Any`, `optional`) - The default value the argument will take if no value is provided.
 - [***read_only***][arganic.arguments.Argument.read_only]: (`bool`, `Default=True`) - The argument is read-only, so it can no longer be modified.
 - [***required***][arganic.arguments.Argument.required]: (`bool`, `default=True`) – The argument is required if the value is missing: an Exception will occur.
 - [***type***][arganic.arguments.Argument.type]: (`Type` | `tuple[Type]`, `optional`) – Defines the type(s) of values accepted for this argument, if the type provided is not valid an Exception will occur.
 - [***validator***][arganic.arguments.Argument.validator]: (`Validator` | `tuple[Validator]`, `optional`) – One or more instances of validators constraining the value that an argument can have.
 - [***choices***][arganic.arguments.Argument.choices]: (`tuple`, `optional`) – A list of choices limiting the values that the supplied arguments can have.

``` py title="Full featured argument.." linenums="1" hl_lines="6-15"
--8<-- "tests/examples/full_featured_argument.py"
```

### Custom validators

It's possible to define your own validators by extending the [***Validator class***][arganic.validators.Validator].

``` py title="A custom validator example." linenums="1" hl_lines="5-12 15-24"
--8<-- "tests/examples/custom_validator.py"
```

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
