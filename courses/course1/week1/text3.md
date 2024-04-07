## Operators in C

<br>

In C, an operator is a symbol that facilitates the execution of particular mathematical, relational, bitwise, conditional, or logical operations on variables and values. Operands are the variables and values that are used with operators. Therefore, we can define the operators as the symbols that operate on operands.

### Types of Operators in C

C language provides a wide range of operators that can be classified into 6 types based on their functionality:

1.  Arithmetic Operators

2.  Relational Operators

3.  Logical Operators

4.  Bitwise Operators

5.  Assignment Operators
<br>

### 1. Arithmetic Operators

The arithmetic operators are used to perform arithmetic/mathematical operations on operands. There are 9 arithmetic operators in C language:

| S. No. | Symbol       | Operator    | Description                               | Syntax   |
|--------|--------------|-------------|-------------------------------------------|----------|
| 1      | +            | Plus        | Adds two numeric values.                  | a + b    |
| 2      | -            | Minus       | Subtracts right operand from left operand.| a - b    |
| 3      | *            | Multiply    | Multiply two numeric values.              | a * b    |
| 4      | /            | Divide      | Divide two numeric values.                | a / b    |
| 5      | %            | Modulus     | Returns the remainder after dividing the left operand with the right operand.| a % b    |
| 6      | +            | Unary Plus  | Used to specify positive values.           | +a       |
| 7      | -            | Unary Minus | Flips the sign of the value.               | -a       |
| 8      | ++           | Increment   | Increases the value of the operand by 1.  | a++      |
| 9      | --           | Decrement   | Decreases the value of the operand by 1.  | a--      |

<br>

### 2. Relational Operators

| S. No. | Symbol | Operator               | Description                                           | Syntax  |
|--------|--------|------------------------|-------------------------------------------------------|---------|
| 1      | <      | Less than              | Returns true if the left operand is less than the right operand. Else false | a < b   |
| 2      | >      | Greater than           | Returns true if the left operand is greater than the right operand. Else false | a > b   |
| 3      | <=     | Less than or equal to  | Returns true if the left operand is less than or equal to the right operand. Else false | a <= b  |
| 4      | >=     | Greater than or equal to| Returns true if the left operand is greater than or equal to the right operand. Else false | a >= b  |
| 5      | ==     | Equal to               | Returns true if both operands are equal.               | a == b  |
| 6      | !=     | Not equal to           | Returns true if both operands are NOT equal.          | a != b  |

<br>

### 3. Logical Operators

Logical Operators are used to combine two or more conditions/constraints or to complement the evaluation of the original condition in consideration. The result of the operation of a logical operator is a Boolean value either ****true**** or **false**.

| S. No. | Symbol | Operator     | Description                                     | Syntax  |
|--------|--------|--------------|-------------------------------------------------|---------|
| 1      | &&     | Logical AND  | Returns true if both operands are true.        | a && b  |
| 2      | \|\|   | Logical OR   | Returns true if both or any of the operands is true. | a \|\| b |
| 3      | !      | Logical NOT  | Returns true if the operand is false.           | !a      |

<br>

### 4.Bitwise Operators

The Bitwise operators are used to perform bit-level operations on the operands. The operators are first converted to bit-level and then the calculation is performed on the operands. Mathematical operations such as addition, subtraction, multiplication, etc. can be performed at the bit level for faster processing.

| S. No. | Symbol | Operator     | Description                                     | Syntax  |
|--------|--------|--------------|-------------------------------------------------|---------|
| 1      | &&     | Logical AND  | Returns true if both operands are true.        | a && b  |
| 2      | \|\|   | Logical OR   | Returns true if both or any of the operands is true. | a \|\| b |
| 3      | !      | Logical NOT  | Returns true if the operand is false.           | !a      |

<br>

### 5. Assignment Operators in C

Assignment operators are used to assign value to a variable. The left side operand of the assignment operator is a variable and the right side operand of the assignment operator is a value. The value on the right side must be of the same data type as the variable on the left side otherwise the compiler will raise an error.

| S. No. | Symbol | Operator               | Description                                                            | Syntax   |
|--------|--------|------------------------|------------------------------------------------------------------------|----------|
| 1      | =      | Simple Assignment      | Assign the value of the right operand to the left operand.             | a = b    |
| 2      | +=     | Plus and assign        | Add the right operand and left operand and assign this value to the left operand. | a += b   |
| 3      | -=     | Minus and assign       | Subtract the right operand and left operand and assign this value to the left operand. | a -= b   |
| 4      | *=     | Multiply and assign    | Multiply the right operand and left operand and assign this value to the left operand. | a *= b   |
| 5      | /=     | Divide and assign      | Divide the left operand with the right operand and assign this value to the left operand. | a /= b   |
| 6      | %=     | Modulus and assign     | Assign the remainder in the division of left operand with the right operand to the left operand. | a %= b   |
| 7      | &=     | AND and assign          | Performs bitwise AND and assigns this value to the left operand.       | a &= b   |
| 8      | ```|=```     | OR and assign           | Performs bitwise OR and assigns this value to the left operand.        | a ```|=``` b   |
| 9      | ^=     | XOR and assign          | Performs bitwise XOR and assigns this value to the left operand.       | a ^= b   |
| 10     | >>=    | Rightshift and assign   | Performs bitwise Rightshift and assigns this value to the left operand. | a >>= b  |
| 11     | <<=    | Leftshift and assign    | Performs bitwise Leftshift and assigns this value to the left operand.  | a <<= b  |
