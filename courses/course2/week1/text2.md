# Datatypes

Data types are means to identify type of data and set of valid operations for it. 

![Datatypes](https://imgs.search.brave.com/1gs7kGWbLtAYRMHvCJ4qI3Vfv8QgMovX7rxfUiwCzOg/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9waG9l/bml4bmFwLmNvbS9r/Yi93cC1jb250ZW50/L3VwbG9hZHMvMjAy/MS8wNC9QeXRob24t/RGF0YS1UeXBlcy1P/dmVydmlldy5wbmc)

### Numeric 
Python offers following data types to store and process different datatypes of numeric data:
* Integers – This value is represented by int class. It contains positive or negative whole numbers _(without fractions or decimals)_. In Python, there is no limit to how long an integer value can be.
* Float – This value is represented by the float class. It is a real number with a floating-point representation. It is specified by a decimal point. Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation.
* Complex Numbers – A complex number is represented by a complex class. It is specified as (real part) + (imaginary part)j. _For example – **2+3j**_

> Note : **_type()_** function is used to determine the type of data type
### Boolean
Data type with one of the two built-in values, True or False. Boolean objects that are equal to True are truthy (true), and those equal to False are falsy (false).
>Note – True and False with capital ‘T’ and ‘F’ are valid booleans otherwise python will throw an error. 
### Set
In Python, a Set is an unordered collection of data types that is iterable, mutable and has no duplicate elements.
Note: _A set cannot have mutable elements like a list or dictionary, as it is mutable._ 
>Set1 = {1, 2, 3, 4}
### Dictionary
A dictionary in Python is an unordered collection of data values, used to store data values like a map, unlike other Data Types that hold only a single value as an element, a Dictionary holds a **_key: value pair_**. Key-value is provided in the dictionary to make it more optimized. Each key-value pair in a Dictionary is separated by a colon : , whereas each key is separated by a _‘comma’_.
>vowels = {'a' : 1, 'e' : 2, 'i' : 3, 'o' : 4, 'u' : 5,}
### Sequence
* String - Strings in Python are arrays of bytes representing Unicode characters. A string is a collection of one or more characters put in a _single quote, double-quote, or triple-quote_. In Python there is no character data type, a character is a string of length one. It is represented by str class.
> String1 = 'Hello World!' 
* List - Lists are just like arrays, declared in other languages which is an ordered collection of data. It is very flexible as the items in a list do not need to be of the same type.  
>List = []
>List = [1,2,3,4,5]
* Tuples are represented as group of comma-seprated values of any data type within parenthesis
> Tuple1 = (1,2,3,4,5)