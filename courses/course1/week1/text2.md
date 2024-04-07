## Variables

<br>

### What is variable in c?

A variable in C is a memory location with some name that helps store some form of data and retrieves it when required. We can store different types of data in the variable and reuse the same variable for storing some other data any number of times.

***C Variable Syntax***

data_type variable_name = value;

data_type variable_name1, variable_name2;

**Example**

```int var; ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` // integer variable   ```<br>
```char a; ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  // character variable   ```<br>
```float fff;  // float variables```

### How to use variables in C?

The below example demonstrates how the use variables in C language.


```// C program to demonstrate the  ```<br>
```// declaration, definition and ```<br>
```// initialization ```<br>
```#include <stdio.h> ```<br>
```int main() ```<br>
```{ ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` // declaration with definition ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` int defined_var; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Defined_var: %d\n", defined_var); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` // initialization ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` defined_var = 12; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` // declaration + definition + initialization ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` int ini_var = 25; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Value of defined_var after initialization: %d\n", defined_var); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Value of ini_var: %d", ini_var); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` return 0; ```<br>
```}```


***Output***

```Defined_var: 0```<br>
```Value of defined_var after initialization: 12```<br>
```Value of ini_var: 25```

### Rules for Naming Variables in C

**You can assign any name to the variable as long as it follows the following rules:**

1.  A variable name must only contain alphabets, digits, and underscore.

2.  A variable name must start with an alphabet or an underscore only. It cannot start with a digit.

3.  No whitespace is allowed within the variable name.

4.  A variable name must not be any reserved word or keyword.

---
