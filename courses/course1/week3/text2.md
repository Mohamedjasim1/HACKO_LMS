# Switch Statement

The switch statement in C is an alternate to if-else-if ladder statement which allows us to execute multiple operations for the different possibles values of a single variable called switch variable. Here, We can define various statements in the multiple cases for the different values of a single variable.

  
![switch case in c programming](https://www.programtopia.net/wp-content/uploads/2021/01/switch_0.png)

The syntax of **switch statement** :


```switch(expression){ ```<br>
```case value1: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` //code to be executed; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` break; //optional ```<br>
```case value2: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` //code to be executed; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` break; //optional ```<br>
```...... ```<br>
``` ```<br>
```default: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` //code to be executed if all cases are not matched; ```<br>
```}  ```<br>


### Rules for switch statement in C language

1.  The  _switch expression_  must be of an integer or character type.
2.  The  _case value_  must be an integer or character constant.
3.  The  _case value_  can be used only inside the switch statement.
4.  The  _break statement_  in switch case is not must. It is optional. If there is no break statement found in the case, all the cases will be executed present after the matched case. It is known as  _fall through_  the state of C switch statement.



**Working of Switch Statement  :**

Consider the following  **_switch statement_:**

**C Program:**

```#include <stdio.h> ```<br>
```int main() { ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` int num = 2; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` switch (num) { ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` case 1: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Value is 1\n"); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` break; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` case 2: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Value is 2\n"); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` break; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` case 3: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Value is 3\n"); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` break; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` default: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Value is not 1, 2, or 3\n"); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` break; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` } ```<br>
```return 0; ```<br>
```} ```<br>



**Output**

`Value is 2`

**Step-by-step Process:**

1.  The  **_switch variable num_**  is evaluated. In this case,  **_num_**  is initialized with the  **_value 2_**.
2.  The  **_evaluated num (2) value_**  is compared with the constants specified in each case label inside the  **_switch block_**.
3.  The  **_switch statement_**  matches the  **_evaluated value (2)_**  with the constant specified in the  **_second case (case 2)_**. Since there is a match, the program jumps to the code block associated with the  **_matching case (case 2)_**.
4.  The code block associated with  **_case 2_**  is executed, which prints  **_"Value is 2"_**  to the console.
5.  The  **_"break"_**  keyword is present in the code block of  **_case 2_**. As a result, the program breaks out of the switch statement immediately after executing the code block.
6.  The program control continues after the  **_switch statement_**, and any statements following the  **_switch statement_**  are executed. In this case, there are no statements after the switch, so the program terminates.
7.  The  **_switch statement_**  evaluated the value of the  **_variable num_**, found a match with case 2, executed the corresponding code block, and then exited the  **_switch block_**  due to the presence of the  **_"break" statement_**.



**EXAMPLE PROGRAM**

```#include <stdio.h> ```<br>
``` ```<br>
```int main() { ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` int choice; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Enter a number (1-3): "); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` scanf("%d", &choice); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` switch(choice) { ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` case 1: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("You chose option 1.\n"); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` break; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` case 2: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("You chose option 2.\n"); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` break; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` case 3: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("You chose option 3.\n"); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` break; ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` default: ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("Invalid choice.\n"); ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` } ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```  ```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` return 0; ```<br>
```}```