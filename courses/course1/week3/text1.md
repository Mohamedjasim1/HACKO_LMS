#Conditional statements

**Conditional Statements in C**  programming are used to make decisions based on the conditions. These conditions are specified by a set of conditional statements having boolean expressions which are evaluated to a boolean value true or false. This process is called  **decision making or Conditional Execution in 'C'.**

![conditional statements in c](https://media.geeksforgeeks.org/wp-content/uploads/20230424101456/Conditional-Statements-in-c.webp)

## Types of conditional statements in C

1.  If statement
2.  If-Else statement
3.  Nested If-else statement
4.  If-Else If ladder


### "if" statement

The "if" statement is used to decide whether a certain statement or block of statements will be executed or not i.e if a certain condition is true then a block of statement is executed otherwise not.


![flowchart of if statement in C programming](https://www.programtopia.net/wp-content/uploads/2021/01/if_0.png)

**Syntax**

```if(expression) ```<br>
```{ ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` //code to be executed ```<br>
```}```

If the condition is evaluated as true, then the block statement is executed, but if the condition is evaluated as false, then control is passed to the next Statement following it.

**EXAMPLE**

```#include<stdio.h> ```<br>
```int main(){ ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` int num1=15; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` int num2=29; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` if(num1<num2) //test-condition ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` { ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("num1 is smaller than num2"); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` } ```<br>
```return 0; ```<br>
```}```


**Output**

```num1 is smaller than num2```

### "if-else" Statements 

**if-else Statement** allows two-way selection. If the given condition is true, then program control goes inside the if block and executes the Statement.

The condition is false, then program control goes inside the else block and executes the corresponding Statement.


![flowchart of if else statement in C programming](https://www.programtopia.net/wp-content/uploads/2021/01/ifelse_0.png)

**Syntax**

```if (test-expression) ```<br>
```{ ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` True block of statements ```<br>
```} ```<br>
```else ```<br>
```{ ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` False block of statements ```<br>
```} ```<br>


**EXAMPLE**

```#include<stdio.h> ```<br>
```int main() ```<br>
```{ ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` int num=57; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` if(num<20) ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` { ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("The value is less than 20"); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` } ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` else ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` { ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("The value is greater than 20"); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` } ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` return 0; ```<br>
```} ```<br>


**Output**

`The value is greater than 20`


### Nested if-else  Statements 

The nested if…else statement is used when a program requires more than one test expression. It is also called a multi-way selection statement. When a series of the decision are involved in a statement, we use if else statement in nested form.

  
![nested if statement in C programming](https://www.programtopia.net/wp-content/uploads/2021/01/nested-if_0.png)



**Syntax**

```if( expression ) ```<br>
```{  ```<br>
```  if( expression1 ) ```<br>
```  { ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` statement-block1; ```<br>
```  } ```<br>
```  else  ```<br>
```  { ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` statement-block 2; ```<br>
```  } ```<br>
```} ```<br>
```else ```<br>
```{ ```<br>
```   statement-block 3; ```<br>
```} ```<br>


The C if statements are executed from the top down. As soon as one of the conditions controlling the if is true, the statement associated with that if is executed, and the rest of the C else-if ladder is bypassed. If none of the conditions are true, then the final else statement will be executed.



**EXAMPLE**

```#include<stdio.h> ```<br>
```int main() ```<br>
```{ ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` int num=1; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` if(num<10) ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` { ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` if(num==1) ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` { ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("The value is:%d\n",num); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` } ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` else ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` { ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("The value is greater than 1"); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` } ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` } ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` else ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` { ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("The value is greater than 10"); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` } ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` return 0; ```<br>
```} ```<br>


**Output**

`The value is:1`



### "if-else if-else" ladder

The if-else-if conditional Statement in C is used to execute one code from multiple conditions. It is also known as a  **multi-path decision statement**. It is a sequence of if-else statements where every if statement is associated with else if Statement and last would be an else statement.



![flowchart for if...else if...else statement in C programming](https://www.programtopia.net/wp-content/uploads/2021/01/if..elseif_0.png)

The general  **syntax**  of how else-if ladders are constructed in ‘C’ programming is as follows:

`if (test - expression 1)`  
`{`  
`statement1;`  
`}`  
`else if (test - expression 2)`  
`{`  
`Statement2;`  
`}`  
`else if (test - expression 3)`  
`{`  
`Statement3;`  
`}`  
`else if (test - expression n)`  
`{`  
`Statement n;`  
`}`  
`else`  
`{`  
`default;`  
`}`  
`Statement x;`

Lets take an  **example**

<br>

```#include<stdio.h> ```<br>
```int main() ```<br>
```{ ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` int temperature = 35; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` if(marks>40) ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` { ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Extremely hot"); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` } ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` else if(marks>30) ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` { ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Mildly hot"); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` } ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` else if(marks>20) ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` { ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Comfortable"); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` } ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` else ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` { ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Cold"); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` } ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` return 0; ```<br>
```} ```<br>


**Output**

`Mildly hot`
