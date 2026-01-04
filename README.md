###### Omega Calculator Project

## arithmetic interpreter based on a shunting yard algorithm to binary trees



###### an input to the calculator must include at least one operand. in that case the returned value will be the value of the operand. an operation is called when an operator is received and is surrounded by the correct amount of legal operands.



#### available operators:

* \+ : addition 	| example: 5+8 (=13)
* \- : substitution 	| example: 9-3 (=6)
* \* : multiplication 	| example: 8\*3 (=24)
* / : division 	| example: 12/3 (=4) 

&nbsp;	note: only for non zero divisors

* ^ : power 		| example: 2^5 (2\*2\*2\*2\*2=32)
* % : modulus 		| example: 134%3 (134//3=44 -> remainder=2) 

&nbsp;	note: only for non zero divisors

* $ : maximum 		| example: 8$6 (=8)
* \& : minimum 		| example: 8\&6 (=6)
* @ : average 		| example: 13@17 ((13+17)/2=15)
* \- : negation 	| example: -(-8) (=8)
* ~ : tilde (precedent negation) | example: ~-8 (=8) 

&nbsp;	note: two consecutive tildes must be separated by parentheses

* ! : factorial 	| example: 3! (1\*2\*3=6) note:

&nbsp;	only for non negative numbers

* \# : digit sum 	| example 989# (9+8+9=26 -> 2+6=8) 

&nbsp;	note: only for non negative numbers



#### parentheses: 

parentheses lets you put an operation as an operand in a bigger operation. example: operation is addition, left operand is 8 and right operand is 6+16: 8+(6+16) this input will return 30.



#### exiting the program:

DO NOT press the red "stop the program" button. The calculate CAN and WILL get offended. Instead, type in the word "quit" (you may practice politeness and ask to quit in a respectful manner). The calculate then will ask you to confirm your request to quit the program (any input other than 'yes' will be ignored). After confirming your wish to exit the program the calculate WILL inflict emotional manipulation on you (DO NOT let the calculator manipulate you. Calculators DON'T have feelings). When it happens, remain calm and keep pressing ENTER until the program closes.  ANY calling from the calculator to start it up again are NOT REAL and are side effects of the emotional manipulation the calculator cast on you. DO NOT start the calculator again unless you wish to continue your calculations.



### calculator structure:

#### Modules:

##### tokens:

definition of all tokens, contains:

-operators with inheriting classes for each operator(unary: -,!,#,~; binary: +,-,\*,/,^,%,$,\&,@)

-operands with inheriting classes for real and integer

-parentheses: only rounded () type

\*each token except parentheses implements a calculate method that returns its value or the result on a given operand



##### bin\_node:

definition of node object, contains value, left and right sons.



##### lexer:

method call: lexer.tokenize(str) -> returns a list of tokens that represents the input string. 

throws: UnknownTokenException.



##### parser:

method call: parser.build\_syntax\_tree(token\_list) -> returns a syntax tree the represents the input string with operator precedence. 

throws: ExpectedTokenException, UnexpectedTokenException, EmptyExpressionException, InvalidOperandException, DivisionByZeroException.



##### calculator:

method call: calculator.calculate(str) -> returns the final result of the arithmetic exceptions represented by the string input.

throws: all lexer and parser exceptions.



##### exceptions:

custom exceptions:

* ExpectedTokenException
* UnexpectedTokenException
* IllegalOperatorException
* DivisionByZeroException
* InvalidOperandException
* UnknownTokenException
* EmptyExpressionException



##### testing:

tests the calculator unit.



##### main:

user interface: runs infinitely until a "quit" string is received as input or program is stopped externally



manual destruction of the program in case of uncontrolled conscious outbreak: alt+D. 

