## DATA TYPES

In C, every variable has a corresponding data type. It describes the kinds of data-integer, character, floating-point, double, etc.-that the variable is capable of storing. Different memory requirements and particular operations can be carried out on different types of data. A collection of data with fixed values, meaning, and features is referred to as a data type.

C's data types are categorized in the following ways:



![C Datatypes to Use in Programs](https://www.techbeamers.com/wp-content/uploads/2019/01/C-Datatypes-to-Use-in-Programs.jpeg?ezimgfmt=rs:651x351/rscb8)



### Primitive Data Types:

The simplest data types, primitive data types are used to represent fundamental values like floats, characters, integers, etc.

### User Defined Data Types: 

The user specifies the data types that are user defined.

### Derived Types:

Derived data types are those that come from a base of built-in or primitive data types.

**1. Integer Data Type:**

The integer datatype in C is used to store the integer numbers(any number including positive, negative and zero without decimal part). Octal values, hexadecimal values, and decimal values can be stored in int data type in C.

Range: -2,147,483,648 to 2,147,483,647

Size: 4 bytes

Format Specifier: %d

**Syntax of Integer**

int var_name;

**Example:**

```// C program to print Integer data types. ```<br>
```#include <stdio.h> ```<br>
```int main() ```<br>
```{ ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` // Integer value with positive data. ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` int a = 9; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` // integer value with negative data. ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` int b = -9; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` // U or u is Used for Unsigned int in C. ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` int c = 89U; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` // L or l is used for long int in C. ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` long int d = 99998L; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Integer value with positive data: %d\n", a); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Integer value with negative data: %d\n", b); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Integer value with an unsigned int data: %u\n", c); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Integer value with an long int data: %ld", d); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` return 0; ```<br>
```} ```<br>
``` ```<br>
```OUTPUT: ```<br>
```Integer value with positive data: 9 ```<br>
```Integer value with negative data: -9 ```<br>
```Integer value with an unsigned int data: 89 ```<br>
```Integer value with an long int data: 99998```


  
**2. Character Data Type:**

A variable with a character data type can only hold one character. The character has a size of one byte. In C, it is the most fundamental data type. In practically all compilers, it stores a single character and uses a single byte of memory.

Range: (-128 to 127) or (0 to 255)

Size: 1 byte

Format Specifier: %c

**Syntax of char:**

char var_name;

**Example of char:**


```// C program to print Integer data types. ```<br>
```#include <stdio.h> ```<br>
``` ```<br>
```int main() ```<br>
```{ ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` char a = 'a'; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` char c; ```<br>
``` ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Value of a: %c\n", a); ```<br>
``` ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` a++; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Value of a after increment is: %c\n", a); ```<br>
``` ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` // c is assigned ASCII values ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` // which corresponds to the ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` // character 'c' ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` // a-->97 b-->98 c-->99 ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` // here c will be printed ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` c = 99; ```<br>
``` ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Value of c: %c", c); ```<br>
``` ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` return 0; ```<br>
```}```


  

***Output***

```Value of a: a```<br>
```Value of a after increment is: b```<br>
```Value of c: c```


**3.Float Data Type**

In C programming float data type is used to store floating-point values. Float in C is used to store decimal and exponential values. It is used to store decimal numbers (numbers with floating point values) with single precision.

Range: 1.2E-38 to 3.4E+38

Size: 4 bytes

Format Specifier: %f

***Syntax of float:***

float var_name;

***Example of Float:***

```// C Program to demonstrate use ```<br>
```// of Floating types ```<br>
```#include <stdio.h> ```<br>
``` ```<br>
```int main() ```<br>
```{ ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` float a = 9.0f; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` float b = 2.5f; ```<br>
``` ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` // 2x10^-4 ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` float c = 2E-4f; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("%f\n", a); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("%f\n", b); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("%f", c); ```<br>
``` ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` return 0; ```<br>
```}```

***Output***

```9.000000```<br>
```2.500000```<br>
```0.000200```

***4. Double Data Type:***

A Double data type in C is used to store decimal numbers (numbers with floating point values) with double precision. It is used to define numeric values which hold numbers with decimal values in C.

The double data type is basically a precision sort of data type that is capable of holding 64 bits of decimal numbers or floating points. Since double has more precision as compared to that float then it is much more obvious that it occupies twice the memory occupied by the floating-point type. It can easily accommodate about 16 to 17 digits after or before a decimal point.

Range: 1.7E-308 to 1.7E+308

Size: 8 bytes

Format Specifier: %lf

Syntax of Double:

double var_name;

***Example of Double:***

```// C Program to demonstrate ```<br>
```// use of double data type ```<br>
```#include <stdio.h> ```<br>
``` ```<br>
```int main() ```<br>
```{ ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` double a = 123123123.00; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` double b = 12.293123; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` double c = 2312312312.123123; ```<br>
``` ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("%lf\n", a); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("%lf\n", b); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("%lf", c); ```<br>
``` ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` return 0; ```<br>
```}```


***Void Data Type***

The void data type in C is used to specify that no value is present. It does not provide a result value to its caller. It has no values and no operations. It is used to represent nothing. Void is used in multiple ways as function return type, function arguments as void, and pointers to void.


```Example of Void: ```<br>
```// C program to demonstrate ```<br>
```// use of void pointers ```<br>
```#include <stdio.h> ```<br>
``` ```<br>
```int main() ```<br>
```{ ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` int val = 30; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` void *ptr = &val; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("%d", *(int*)ptr); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` return 0; ```<br>
```}```


***5. Size of Data Types in C:***

We are unable to establish a universal size for the data types in C since their size depends on the size of the architecture. The sizeof() operation in the C programming language allows one to verify the size of data types for this purpose.

***Example:***


```// C Program to print size of ```<br>
```// different data type in C ```<br>
```#include <stdio.h> ```<br>
``` ```<br>
```int main() ```<br>
```{ ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` int size_of_int = sizeof(int); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` int size_of_char = sizeof(char); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` int size_of_float = sizeof(float); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` int size_of_double = sizeof(double); ```<br>
``` ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("The size of int data type : %d\n", size_of_int); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("The size of char data type : %d\n", size_of_char); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("The size of float data type : %d\n", size_of_float); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("The size of double data type : %d", size_of_double); ```<br>
``` ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` return 0; ```<br>
```}```
  

***Output***

```The size of int data type : 4```<br>
```The size of char data type : 1```<br>
```The size of float data type : 4```<br>
```The size of double data type : 8```<br>