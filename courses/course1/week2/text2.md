## Operator Precedence 

**Operator precedence** determines which operation is performed first in an expression with more than one operator with different precedence.

### **Example of Operator Precedence**

Let's try to evaluate the following expression,

**10 + 20 * 30**

The expression contains two operators,  +(plus), and *(multiply)  According to the given table, the operator has higher precedence than  + so, the first evaluation will be

**10 + (20 * 30)**

After evaluating the higher precedence operator, the expression is

**10 + 600**

Now, the + operator will be evaluated.

**610**


**C Program to illustrate operator precedence**

```#include <stdio.h>```<br>
```int main()```<br>
```{```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` // printing the value of same expression```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` printf("10 + 20 * 30 = %d", 10 + 20 * 30);```<br>
``` ```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``` return 0;```<br>
```}```

**Output**

```10 + 20 * 30 = 610```

As we can see, the expression is evaluated as, **10 + (20 * 30)** but  **not as (10 + 20) * 30** due to  operator having higher precedence.
