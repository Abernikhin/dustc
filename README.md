# DUSTC - compiler for dust language

if you want to create a variable then specify its type and name
```cpp
number num;
```

or create any quantity variable in one line
```cpp
number num, num2, num3;
```

you cant init variable on the same line where variable created

if write '()' after variable name you create function
```cpp
number sum();
```

in '()' you can via comma arguments for function
```cpp
number sum(arg_type arg_name, second_arg_type second_arg_name);
```

you can also just prototype the function

if you want to init variable you must write the next line
```cpp
var_name = value;
```
as value you can give functions, value or mathematical expression