# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
from sqlalchemy import create_engine
import requests
from functools import reduce


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('Shiva !')

    # Variables are like containers that store data values in a program
    # In this example, age is an integer, name is a string, height is a float, and is_student is a boolean. You can change their values throughout your program.
    age = 30
    name = "Alice"
    height = 5.7
    is_student = False

    #In Python, lists are used to store collections of items. They are ordered, mutable, and allow duplicate values.
    fruits = ["apple", "banana", "cherry"]
    print(fruits[0])  # access items using their index

    fruits.append("orange")
    print(fruits)  # Lists can also be manipulated

    #Lists can also be nested, meaning you can have lists within lists ?

    #Mutable list
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list)  # Output: [1, 2, 3, 4]

    #Immutable tuple
    my_tuple = (1, 2, 3)
    # my_tuple.append(4)  # This would raise an error

    #Dictionaries: Collections of key-value pairs. You can add, change, or remove entries.
    my_dict = {"a": 1, "b": 2}
    my_dict["c"] = 3  # Add new key-value pair
    print(my_dict)

    #Sets: Collections of unique items. You can add or remove items
    my_set = {1, 2, 3}
    my_set.add(4)  # Add an item
    my_set.add(4)  # try to add duplicate to see if it adds to print duplicate value in set
    print(my_set)

    #Strings: You can't change a string in place. Any operation that modifies a string actually creates a new one. (Immutable)
    my_string = "hello"
    # my_string[0] = "H"  # This would raise an error

    #Frozen sets: Immutable versions of sets.
    my_frozenset = frozenset([1, 2, 3])
    # my_frozenset.add(4)  # This would raise an error


    # Read the CSV file with header
    df = pd.read_csv('Data/orders.csv')
    # Convert status to lowercase
    df['status'] = df['status'].str.lower()
    # Drop rows with missing values
    df.dropna(inplace=True)
    # Group by category_name and sum grand_total
    result = df.groupby('category_name')['grand_total'].sum()
    print(result)


    # engine = create_engine('sqlite:///mydatabase.db')
    # df.to_sql('table_name', engine, index=False)

    # response = requests.get('https://api.example.com/data')
    # data = response.json()

    #Basic Joins
    # Sample data
    df1 = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
    df2 = pd.DataFrame({'id': [1, 2, 4], 'age': [24, 27, 30]})

    # Inner join on 'id'
    inner_join_result = pd.merge(df1, df2, on='id', how='inner')
    print(inner_join_result)

    print("---------------------")

    right_join_result = pd.merge(df1, df2, on='id', how='right')
    print(right_join_result)

    print("---------------------")

    outer_join_result = pd.merge(df1, df2, on='id', how='outer')
    print(outer_join_result)

    # Filter rows where age is greater than 25
    filtered_df = df2[df2['age'] > 25]
    print(filtered_df)

    # Filter rows where age is greater than 25 and id is less than 4
    filtered_df = df2[(df2['age'] > 25) & (df2['id'] < 4)]

    # Select only 'id' and 'name' columns
    selected_columns = df1[['id', 'name']]
    print(selected_columns)

    # Sort by age in ascending order
    sorted_df = df2.sort_values(by='age')

    # Sort by age in descending order
    sorted_df = df2.sort_values(by='age', ascending=False)
    print(sorted_df)

    # Query for rows where age > 25
    query_filtered_df = df2.query("age > 25")
    print(query_filtered_df)

    # Multiple aggregations
    agg_df = df2.groupby('id').agg(
        avg_age=('age', 'mean'),
        max_age=('age', 'max'),
        min_age=('age', 'min')
    )

    # Merge the DataFrames to include names
    merged_df = pd.merge(df1, agg_df, on='id', how='left')
    print(merged_df)

    import pandas as pd

    # Sample data
    df2 = pd.DataFrame({'id': [1, 2, 4], 'age': [24, 27, 30]})

    print('------------------')

    # Calculating mean, max, and min individually
    mean_age = df2['age'].mean()
    max_age = df2['age'].max()
    min_age = df2['age'].min()

    print(f"Mean Age: {mean_age}")
    print(f"Max Age: {max_age}")
    print(f"Min Age: {min_age}")

    numbers = [1, 2, 3, 4]

    # List Comprehensions
    squares = [x ** 2 for x in numbers]
    print(squares)

    # Get squares only for even numbers
    squares_of_evens = [x ** 2 for x in numbers if x % 2 == 0]
    print(squares_of_evens)

    #Enhanced For Loop (Using Enumerate and Zip)
    # Loop with index
    words = ['apple', 'banana', 'cherry']
    for index, word in enumerate(words):
        print(index, word)

    #The zip function lets you loop through multiple iterables at once.
    names = ['Alice', 'Bob', 'Charlie']
    ages = [24, 27, 22]
    for name, age in zip(names, ages):
        print(name, age)

    #Lambda Functions: Lambda functions are anonymous, single-line functions defined with the lambda keyword. They’re commonly used for small, one-time operations.
    # Basic lambda function
    square = lambda x: x ** 2
    print(square(5))

    # Using lambda with map to square a list
    numbers = [1, 2, 3, 4]
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    print(squared_numbers)

    # Functional Programming (map, filter, reduce)
    numbers = [2, 4, 3, 4]
    sum_numbers = list(map(lambda x: x + 2, numbers))
    print(sum_numbers)

    #Filters elements based on a condition.
    numbers = [1, 2, 3, 4]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(evens)

    #Reduce: Reduces a sequence to a single value (requires importing from functools).
    numbers = [1, 2, 3, 4]
    product = reduce(lambda x, y: x * y, numbers)
    print(product)

    # Generator Expressions: Generator expressions are similar to list comprehensions but create generators instead of lists. Generators are more memory-efficient for large datasets.
    # Generator to yield squares
    squares_gen = (x ** 2 for x in range(1, 10000))
    # Print each square
    for square in squares_gen:
        print(square)

    #Dictionary Comprehensions
    # Creating a dictionary of numbers and their squares
    squares_dict = {x: x ** 2 for x in range(1, 6)}
    print(squares_dict)

    #Any and All Functions
    nums = [1, 2, 3, 0]
    has_positive = any(num > 0 for num in nums)
    print(has_positive)




























