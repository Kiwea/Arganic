# Arganic

{==

***Arganic*** is a lightweight **Python library** making it easy to manage **Arguments** for **Classes**, **Methods** or **Functions**.

==}

The library provides a comprehensive set of decorators with advanced features such as
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
 - **Read/Write Access Control:** Define read-only or write-only properties for classes, methods, and functions as needed.
 - **Default Values:** Set default values for function arguments, method parameters, and class properties to streamline code logic.
 - **Choice Selection:** Specify a list of choices for method arguments and function parameters, restricting input values to predefined options.

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

The same example with a simple method.

``` py title="A simple method with two arguments."
--8<-- "examples/function_drive.py"
```

### Using library

### Customize validators

## Contributing