# DUSTC - compiler for dust language

if you want to create a variable then specify its type and name
```ts
number num;
```

or create any quantity variable in one line
```ts
number num, num2, num3;
```

you cant init variable on the same line where variable created

if write '()' after variable name you create function
```ts
number sum();
```

in '()' you can via comma arguments for function
```ts
number sum(arg_type arg_name, second_arg_type second_arg_name);
```

you can also just prototype the function

if you want to init variable you must write the next line
```ts
var_name = value;
```
as value you can give functions, numbers or mathematical expression

