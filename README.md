###### Omega Calculator Project

## arithmetic interpreter based on a shunting yard algorithm to binary trees



#### classes:

###### token - implements interface calculatable

fields:

value



inheritors: operator, operand, parentheses



###### operator 

fields: 

operation

precedence

inheritors:

Binary operator 

Unary operator  



###### operand -

fields:

value

inheritors:

Integer

Real





#### Utility Classes / Interfaces:

###### Lexer - 

methods:

tokenize - builds and return a list of tokens with elimination of whitespaces 



###### Parser - 

methods:

build\_AST - builds an abstract syntax tree of the tokens so that the left hand subtree is precedent to the right hand subtree.



###### calculatable -

abstract method:

operate - receives two operands and returns the result



###### Calculator:

static method:

calculate - gets a string representing an arithmetic expression, calls the lexer and parser methods, and then the evaluate method

evaluate - gets a tree of operators and operands, calculates the result via the calculatable.operate method and returns the result. 

