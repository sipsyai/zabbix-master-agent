---
title: Mathematical functions
source: https://www.zabbix.com/documentation/current/en/manual/appendix/functions/math
downloaded: 2025-11-14 10:47:44
---

# 6 Mathematical functions

All functions listed here are supported in:

  * [Trigger expressions](/documentation/current/en/manual/config/triggers/expression)
  * [Calculated items](/documentation/current/en/manual/config/items/itemtypes/calculated)
  * [Expression macros](/documentation/current/en/manual/config/macros/expression_macros)

Mathematical functions are supported with float and integer value types, unless stated otherwise.

The functions are listed without additional information. Click on the function to see the full details.

abs | The absolute value of a value.  
---|---  
acos | The arccosine of a value as an angle, expressed in radians.  
asin | The arcsine of a value as an angle, expressed in radians.  
atan | The arctangent of a value as an angle, expressed in radians.  
atan2 | The arctangent of the ordinate (value) and abscissa coordinates specified as an angle, expressed in radians.  
avg | The average value of the referenced item values.  
cbrt | The cube root of a value.  
ceil | Round the value up to the nearest greater or equal integer.  
cos | The cosine of a value, where the value is an angle expressed in radians.  
cosh | The hyperbolic cosine of a value.  
cot | The cotangent of a value, where the value is an angle expressed in radians.  
degrees | Converts a value from radians to degrees.  
e | The Euler's number (2.718281828459045).  
exp | The Euler's number at a power of a value.  
expm1 | The Euler's number at a power of a value minus 1.  
floor | Round the value down to the nearest smaller or equal integer.  
log | The natural logarithm.  
log10 | The decimal logarithm.  
max | The highest value of the referenced item values.  
min | The lowest value of the referenced item values.  
mod | The division remainder.  
pi | The Pi constant (3.14159265358979).  
power | The power of a value.  
radians | Converts a value from degrees to radians.  
rand | Return a random integer value.  
round | Round the value to decimal places.  
signum | Returns '-1' if a value is negative, '0' if a value is zero, '1' if a value is positive.  
sin | The sine of a value, where the value is an angle expressed in radians.  
sinh | The hyperbolical sine of a value, where the value is an angle expressed in radians.  
sqrt | The square root of a value.  
sum | The sum of the referenced item values.  
tan | The tangent of a value.  
truncate | Truncate the value to decimal places.  
  
### Function details

Some general notes on function parameters:

  * Function parameters are separated by a comma
  * Expressions are accepted as parameters
  * Optional function parameters (or parameter parts) are indicated by `<` `>`

##### abs(value)

The absolute value (from 0) of a value.

Parameter:

  * **value** \- the value to check

For example, the absolute value of either '3' or '-3' will be '3'.

Example:
    
    
    abs(last(/host/key))>10

Copy

✔ Copied

##### acos(value)

The arccosine of a value as an angle, expressed in radians.

Parameter:

  * **value** \- the value to check

The value must be between -1 and 1. For example, the arccosine of a value '0.5' will be '2.0943951'.

Example:
    
    
    acos(last(/host/key))

Copy

✔ Copied

##### asin(value)

The arcsine of a value as an angle, expressed in radians.

Parameter:

  * **value** \- the value to check

The value must be between -1 and 1. For example, the arcsine of a value '0.5' will be '-0.523598776'.

Example:
    
    
    asin(last(/host/key)) 

Copy

✔ Copied

##### atan(value)

The arctangent of a value as an angle, expressed in radians.

Parameter:

  * **value** \- the value to check

The value must be between -1 and 1. For example, the arctangent of a value '1' will be '0.785398163'.

Example:
    
    
    atan(last(/host/key))

Copy

✔ Copied

##### atan2(value,abscissa)

The arctangent of the ordinate (value) and abscissa coordinates specified as an angle, expressed in radians.

Parameters:

  * **value** \- the value to check;
  * **abscissa** \- the abscissa value.

For example, the arctangent of the ordinate and abscissa coordinates of a value '1' will be '2.21429744'.

Example:
    
    
    atan2(last(/host/key),2)

Copy

✔ Copied

##### avg(<value1>,<value2>,...)

The average value of the referenced item values.

Parameter:

  * **valueX** \- the value returned by another function that is working with item history.

Example:
    
    
    avg(avg(/host/key),avg(/host2/key2))

Copy

✔ Copied

##### cbrt(value)

The cube root of a value.

Parameter:

  * **value** \- the value to check

For example, the cube root of '64' will be '4', of '63' will be '3.97905721'.

Example:
    
    
    cbrt(last(/host/key))

Copy

✔ Copied

##### ceil(value)

Round the value up to the nearest greater or equal integer.

Parameter:

  * **value** \- the value to check

For example, '2.4' will be rounded up to '3'. See also floor().

Example:
    
    
    ceil(last(/host/key))

Copy

✔ Copied

##### cos(value)

The cosine of a value, where the value is an angle expressed in radians.

Parameter:

  * **value** \- the value to check

For example, the cosine of a value '1' will be '0.54030230586'.

Example:
    
    
    cos(last(/host/key))

Copy

✔ Copied

##### cosh(value)

The hyperbolic cosine of a value. Returns the value as a real number, not as scientific notation.

Parameter:

  * **value** \- the value to check

For example, the hyperbolic cosine of a value '1' will be '1.54308063482'.

Example:
    
    
    cosh(last(/host/key))

Copy

✔ Copied

##### cot(value)

The cotangent of a value, where the value is an angle expressed in radians.

Parameter:

  * **value** \- the value to check

For example, the cotangent of a value '1' will be '0.54030230586'.

Example:
    
    
    cot(last(/host/key))

Copy

✔ Copied

##### degrees(value)

Converts a value from radians to degrees.

Parameter:

  * **value** \- the value to check

For example, a value '1' converted to degrees will be '57.2957795'.

Example:
    
    
    degrees(last(/host/key))

Copy

✔ Copied

##### e

The Euler's number (2.718281828459045).

Example:
    
    
    e()

Copy

✔ Copied

##### exp(value)

The Euler's number at a power of a value.

Parameter:

  * **value** \- the value to check

For example, Euler's number at a power of a value '2' will be '7.38905609893065'.

Example:
    
    
    exp(last(/host/key))

Copy

✔ Copied

##### expm1(value)

The Euler's number at a power of a value minus 1.

Parameter:

  * **value** \- the value to check

For example, Euler's number at a power of a value '2' minus 1 will be '6.38905609893065'.

Example:
    
    
    expm1(last(/host/key))

Copy

✔ Copied

##### floor(value)

Round the value down to the nearest smaller or equal integer.

Parameter:

  * **value** \- the value to check

For example, '2.6' will be rounded down to '2'. See also ceil().

Example:
    
    
    floor(last(/host/key))

Copy

✔ Copied

##### log(value)

The natural logarithm.

Parameter:

  * **value** \- the value to check

For example, the natural logarithm of a value '2' will be '0.69314718055994529'.

Example:
    
    
    log(last(/host/key))

Copy

✔ Copied

##### log10(value)

The decimal logarithm.

Parameter:

  * **value** \- the value to check

For example, the decimal logarithm of a value '5' will be '0.69897000433'.

Example:
    
    
    log10(last(/host/key))

Copy

✔ Copied

##### max(<value1>,<value2>,...)

The highest value of the referenced item values.

Parameter:

  * **valueX** \- the value returned by another function that is working with item history.

Example:
    
    
    max(avg(/host/key),avg(/host2/key2))

Copy

✔ Copied

##### min(<value1>,<value2>,...)

The lowest value of the referenced item values.

Parameter:

  * **valueX** \- the value returned by another function that is working with item history.

Example:
    
    
    min(avg(/host/key),avg(/host2/key2))

Copy

✔ Copied

##### mod(value,denominator)

The division remainder.

Parameters:

  * **value** \- the value to check;
  * **denominator** \- the division denominator.

For example, division remainder of a value '5' with division denominator '2' will be '1'.

Example:
    
    
    mod(last(/host/key),2)

Copy

✔ Copied

##### pi

The Pi constant (3.14159265358979).

Example:
    
    
    pi()

Copy

✔ Copied

##### power(value,power value)

The power of a value.

Parameters:

  * **value** \- the value to check;
  * **power value** \- the Nth power to use.

For example, the 3rd power of a value '2' will be '8'.

Example:
    
    
    power(last(/host/key),3)

Copy

✔ Copied

##### radians(value)

Converts a value from degrees to radians.

Parameter:

  * **value** \- the value to check

For example, a value '1' converted to radians will be '0.0174532925'.

Example:
    
    
    radians(last(/host/key))

Copy

✔ Copied

##### rand

Return a random integer value. A pseudo-random generated number using time as seed (enough for mathematical purposes, but not cryptography).

Example:
    
    
    rand()

Copy

✔ Copied

##### round(value,decimal places)

Round the value to decimal places.

Parameters:

  * **value** \- the value to check;
  * **decimal places** \- specify decimal places for rounding (0 is also possible).

For example, a value '2.5482' rounded to 2 decimal places will be '2.55'.

Example:
    
    
    round(last(/host/key),2)

Copy

✔ Copied

##### signum(value)

Returns '-1' if a value is negative, '0' if a value is zero, '1' if a value is positive.

Parameter:

  * **value** \- the value to check.

Example:
    
    
    signum(last(/host/key))

Copy

✔ Copied

##### sin(value)

The sine of a value, where the value is an angle expressed in radians.

Parameter:

  * **value** \- the value to check

For example, the sine of a value '1' will be '0.8414709848'.

Example:
    
    
    sin(last(/host/key))

Copy

✔ Copied

##### sinh(value)

The hyperbolical sine of a value, where the value is an angle expressed in radians.

Parameter:

  * **value** \- the value to check

For example, the hyperbolical sine of a value '1' will be '1.17520119364'.

Example:
    
    
    sinh(last(/host/key))

Copy

✔ Copied

##### sqrt(value)

The square root of a value.  
This function will fail with a negative value.

Parameter:

  * **value** \- the value to check

For example, the square root of a value '3.5' will be '1.87082869339'.

Example:
    
    
    sqrt(last(/host/key))

Copy

✔ Copied

##### sum(<value1>,<value2>,...)

The sum of the referenced item values.

Parameter:

  * **valueX** \- the value returned by another function that is working with item history.

Example:
    
    
    sum(avg(/host/key),avg(/host2/key2))

Copy

✔ Copied

##### tan(value)

The tangent of a value.

Parameter:

  * **value** \- the value to check

For example, the tangent of a value '1' will be '1.55740772465'.

Example:
    
    
    tan(last(/host/key))

Copy

✔ Copied

##### truncate(value,decimal places)

Truncate the value to decimal places.

Parameters:

  * **value** \- the value to check;
  * **decimal places** \- specify decimal places for truncating (0 is also possible).

For example, a value '2.5482' truncated to 2 decimal places will be '2.54'.

Example:
    
    
    truncate(last(/host/key),2)

Copy

✔ Copied

See [all supported functions](/documentation/current/en/manual/appendix/functions).