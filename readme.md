# Python Garden Module - Python Module 01

A comprehensive educational Python project demonstrating fundamental programming concepts through a garden management system.

## Overview

This project is a series of progressive exercises that build upon each other to teach Python fundamentals. Each exercise (`ex0` through `ex6`) introduces new concepts and builds a complete garden management application.

## Project Structure
```
Python-Module-01/
├── ex0/
│ └── ft_garden_intro.py # Basic variables and print statements
├── ex1/
│ └── ft_garden_data.py # Classes and object creation
├── ex2/
│ └── ft_plant_growth.py # Methods and object state management
├── ex3/
│ └── ft_plant_factory.py # Factory pattern and data structures
├── ex4/
│ └── ft_garden_security.py # Properties, validation, and data protection
├── ex5/
│ └── ft_plant_types.py # Inheritance and polymorphism
└── ex6/
└── ft_garden_analytics.py # Advanced OOP, composition, and analysis
```

## Exercises

### Exercise 0: Garden Introduction (`ex0/ft_garden_intro.py`)
**Concepts:** Variables, print statements, basic I/O

Demonstrates basic Python syntax with simple variables and formatted output. A good starting point for beginners.

**Key Features:**
- Variable declaration and initialization
- String formatting
- Conditional execution with `if __name__ == "__main__"`

### Exercise 1: Garden Data (`ex1/ft_garden_data.py`)
**Concepts:** Classes, object initialization, iteration

Introduces Object-Oriented Programming by creating a `Plant` class and instantiating multiple plant objects.

**Key Features:**
- Class definition with `__init__` constructor
- Instance attributes
- Object collection management with lists
- String interpolation in loops

### Exercise 2: Plant Growth (`ex2/ft_plant_growth.py`)
**Concepts:** Instance methods, state modification, loops

Extends the Plant class with growth-related methods and simulates plant growth over time.

**Key Features:**
- Instance methods (`grow()`, `grow_age()`)
- Method chaining and state updates
- Dictionary comprehension
- Conditional loops

### Exercise 3: Plant Factory (`ex3/ft_plant_factory.py`)
**Concepts:** Factory pattern, data structures, dynamic object creation

Demonstrates creating multiple plant objects from a data dictionary using the factory pattern.

**Key Features:**
- Dictionary-based data storage
- Factory pattern implementation
- Loop-based object instantiation
- Counter patterns

### Exercise 4: Garden Security (`ex4/ft_garden_security.py`)
**Concepts:** Properties, validation, data encapsulation, private attributes

Implements data protection mechanisms using Python properties and private attributes.

**Key Features:**
- Private attributes (name mangling with `__` prefix)
- `@property` decorators
- Setter methods with validation
- Security validation logic

### Exercise 5: Plant Types (`ex5/ft_plant_types.py`)
**Concepts:** Inheritance, polymorphism, method overriding

Creates a hierarchy of plant types using inheritance to demonstrate OOP principles.

**Key Features:**
- Base class definition
- Subclass inheritance with `super()`
- Specialized plant types (Flower, Tree, Succulent, Vegetable)
- Polymorphic methods (`bloom()`, `produce_shade()`, etc.)

### Exercise 6: Garden Analytics (`ex6/ft_garden_analytics.py`)
**Concepts:** Complex inheritance chains, composition, analytics, scoring

Implements a comprehensive garden management system with analytics, scoring, and validation.

**Key Features:**
- Multi-level inheritance hierarchies
- Static methods
- Complex composition patterns
- Garden-level analytics and scoring
- Plant validation and health tracking

## Running the Exercises

Each exercise can be run independently:

```bash
# Run individual exercises
python3 ex0/ft_garden_intro.py
python3 ex1/ft_garden_data.py
python3 ex2/ft_plant_growth.py
python3 ex3/ft_plant_factory.py
python3 ex4/ft_garden_security.py
python3 ex5/ft_plant_types.py
python3 ex6/ft_garden_analytics.py