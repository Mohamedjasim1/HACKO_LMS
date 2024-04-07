# Conditionals in Python: Explanation and Examples

## Introduction:

Conditionals, also known as control flow statements, are the cornerstones of decision-making in Python. They enable your code to execute different blocks of code based on whether certain conditions are true or false, making your programs more flexible and adaptable.



## 1. if Statement:

**Explanation:** The if statement checks if a single condition is true. If it is, the code block following the if is executed.

**Example:**

```age = 18 ```<br>
``` ```<br>
```if age >= 18: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` print("You are eligible to vote.") ```<br>
```else: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` print("You are not eligible to vote yet.") ```<br>


**Output:** If age is 18 or older, the first line prints, otherwise the second line prints.

## 2. if-else Statement:

**Explanation:** The if-else statement checks if a single condition is true. If it is, the if block is executed; otherwise, the else block is executed.
**Example:**

```grade = 85 ```<br>
``` ```<br>
```if grade >= 90: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` print("Excellent work! You got an A.") ```<br>
```elif grade >= 80: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` print("Great job! You got a B.") ```<br>
```else: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` print("Keep practicing! You got a C or lower.")```

**Output:** Depending on the value of grade, one of the three lines will print.
## 3. Nested if Statements:

**Explanation:** You can nest if statements to create more complex decision-making logic.
**Example:**

```username = "admin" ```<br>
```password = "secret123" ```<br>
``` ```<br>
```if username == "admin": ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` if password == "secret123": ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` print("Welcome, administrator!") ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` else: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` print("Incorrect password.") ```<br>
```else: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` print("Invalid username.")```


**Output:** If both username and password match, the first line prints; otherwise, an appropriate error message is displayed.
## 4. elif Statement:

**Explanation:** The elif statement allows you to check multiple conditions sequentially.
**Example:**

```score = 70 ```<br>
``` ```<br>
```if score >= 90: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` print("You earned an A.") ```<br>
```elif score >= 80: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` print("You earned a B.") ```<br>
```elif score >= 70: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` print("You earned a C.") ```<br>
```else: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` print("You earned a D or F.") ```<br>


**Output:** Depending on the value of score, one of the four lines will print.
## 5. else Statement:

**Explanation:** The else statement is optional, but it can be useful as a default case when none of the if or elif conditions are met.
**Example:**

```number = 5 ```<br>
``` ```<br>
```if number > 0: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` print("The number is positive.") ```<br>
```elif number < 0: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` print("The number is negative.") ```<br>
```else: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` print("The number is zero.") ```<br>


**Output:** Depending on the value of number, one of the three lines will print.
## 6. and & or Operators:

**Explanation:** You can combine conditions using and (both conditions must be true) and or (at least one condition must be true).
**Example:**

```x = 5 ```<br>
```y = 5 ```<br>
``` ```<br>
```# Using and logic ```<br>
```if x == 5 and y == 5: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` print("True") ```<br>
``` ```<br>
``` ```<br>
```# Using or logic ```<br>
```if x == 5 or y == 4: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` print("True")```


**Using `and` logic:**

Here, an `if` statement checks whether both `x` and `y` are equal to `5`. If this condition is true (both `x` and `y` are `5`), the program prints "True". The `and` logical operator requires both conditions to be true for the overall condition to be true. In this case, since both `x` and `y` are indeed `5`, the condition is true, and "True" is printed.

**Using `or` logic:**

In this `if` statement, the condition checks if either `x` is equal to `5` or `y` is equal to `4`. If at least one of these conditions is true, the program prints "True". The `or` logical operator requires only one of the conditions to be true for the overall condition to be true. Since `x` is indeed equal to `5`, the first condition is satisfied, and "True" is printed.



**Truthiness and Falsiness:** In Python, some values are considered "truthy" (e.g., non-zero numbers, strings, lists) and others are "falsy" (e.g., 0, None, ""). An if statement evaluates to True if the condition is truthy, and False otherwise.
Remember:

Indent code blocks properly to define their scope.
Use the appropriate combination of if, elif, and else statements to achieve your desired logic.


