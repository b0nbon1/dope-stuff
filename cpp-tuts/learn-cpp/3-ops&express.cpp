#include <iostream>
#include <math.h>

/*
**************** operators *****************
  Arithmetic => +, -, *, /, %
  relational => <, <=, >, >=, ==
  logical => &&, ||, !
  bitwise => &, |, ~, ^
  increment/Decrement => --, ++ 
  assignment => =

**************** operator precedence **********
the steps for taking arithmetic operATIONS.
example:
x = a + b * c - d / e;
      |   |       |
      1   2       2
*/

double quadratic(double a, double b, double c) {
   double r1 = (-b+ sqrt(b*b-4*a*c))/(2 * a);
   double r2 = (-b - sqrt(b*b-4*a*c))/(2 * a);
  return r1;
}

double speed(double v, double u, double a) {
  return (pow(v,2) - pow(u,2))/(2 * a);
}

double triangle(double b, double h) {
  return (b*h)/2;
}


int sumNaturalNumbers(int n) {
  return n * ( n + 1)/2;
}

float distance(int x1,int y1,int x2,int y2)
{
    float dist;
    
    dist=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
    
    return dist;
}

/*
********************** compound assignment **********************
            +=
            -=
            *=
            /=
            %=

        __________
            &=
            |=
            <<=
            >>=

  example:
    sum+=10; ==== sum = sum + 10 
*/

/*
  ************************** increment/decrement ********************
          pre incr/decr === ++x / --X
          post ```      === x++ / x++

      on pre incr we will increment first then other ops while post we will inc later after the ops.
      j=5 i=10

      ++j*i =60
      j++*i= 51
*/

/*
************************ overflow *****************************

  once it goes beyond maximum, goes to negative eg. char x =127; ++x; x = -128;
*/

/*
**************** Bitwise ops *****************************
            & and 
            | Or
            ^ x-or
            ~ not
            << 
            >>

    | bit 1 | bit 2 | bit 1 & bit 2
     ------------------------------
    |  0    |   0   |     0
     ------------------------------
    |   1   |    0  |     0
     ------------------------------
    |   0   |    1  |     0
     ------------------------------
    |   1   |    1  |     1
     -------------------------------

    | bit 1 | bit 2 | bit 1 | bit 2
     ------------------------------
    |  0    |   0   |     0
     ------------------------------
    |   1   |    0  |     1
     ------------------------------
    |   0   |    1  |     1
     ------------------------------
    |   1   |    1  |     1
     -------------------------------

    | bit 1 | bit 2 | bit 1 ^ bit 2
     ------------------------------
    |  0    |   0   |     0
     ------------------------------
    |   1   |    0  |     1
     ------------------------------
    |   0   |    1  |     1
     ------------------------------
    |   1   |    1  |     0
     -------------------------------


     example usage: x = 11 , y = 5
     y & x = 1


     >> left shift
     
  
*/


int main()
{
  int a, b, c;
  a = 10;
  b = 5;
  c = a + b; // 15
  c = a - b; // 5
  c = a * b; // 50
  c = a / b; // 2
  c = a % b; // this is remainder after division == 0

  return 0;
}
