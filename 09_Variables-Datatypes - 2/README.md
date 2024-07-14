### Composite Datatypes

1. List
    - List is a collection of values which can store any datatype values unlike C.
    - We can access items individual by Indexing
    ```py
    e = [10,9.5,True,'Python',50,9.5]
    print(e)
    print(e[2])
    ```
    Output:
    ```
    [10, 9.5, True, 'Python', 50, 9.5]
    True
    ```

2. Sets
    - Sets is a collection of values without duplicate values.Just like in Math
    - Values jumble when printed
    - Indexing can't be applied
    ```py
    f = {10,9.5,True,'Python',50,9.5}
    print(f)
    ```
    Output:
    ```
    {True, 50, 9.5, 10, 'Python'}
    ```

3. Tuple
    - Tuple is read-only version of list.
    - Once a tuple is created it cant be edited.
    - We can access items individual by Indexing
    ```py
    g = (10,9.5,True,'Python',50,9.5)
    print(g)
    print(g[2])
    # e[0] = 100 # Throws error
    ```
    Output:
    ```
    (10, 9.5, True, 'Python', 50, 9.5)
    True
    ```

4. Dictionary
    - Dictionary stores the values in Key-Value pairs
    - We can access items individual by Indexing(Not same as List)
    ```py
    h = {'One':1,'Two':2}
    print(h)
    print(h['One'])
    ```
    Output:
    ```
    {'One': 1, 'Two': 2}
    1
    ```
