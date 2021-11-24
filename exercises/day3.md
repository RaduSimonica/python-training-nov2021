### Functions exercises
1. Write a function that takes a number as a parameter and prints its square.
1. Write another function that takes a number as a parameter and returns the square. 
Are the results of the two functions different? 
1. Write a function that takes any number of strings and an integer `n` as parameters.
`n` should be an optional parameter. Return the list of strings longer than `n`. 
By default, it should return a list containing all words.

    E.g. 
    * `f('hello', 'hi', 'bye', n=2)` -> `['hello', 'bye']`
    * `f('hello', 'hi')` -> `['hello', 'hi']`
    * `f()` -> `[]`
    * `f(n=10)` -> `[]`
1. Write a function that builds html tags. Apply html escaping for html special chars. 
The function will receive 2 parameters – tag type and tag content and will return the generated html as a string. 
    
    E.g.: `f('b', 'Ham&Eggs')` returns `"<b>Ham&amp;Eggs</b>"`
    
    HTML char escaping:
    * `<` becomes `&lt`;
    * `>` becomes `&gt`;
    * `"` becomes `&quot`;
    * `&` becomes `&amp`;

### Modules and packages exercises
1. Create a Python package with a module in it where you place one of the functions defined above.
1. Create a Python module where you import and call the functions defined above 
(the one from the package and the remaining ones from `<functions_exercises_module>`).
