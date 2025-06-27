import pandas as pd

""" Combine two tables """

data = [[1, 'Wang', 'Alen'], [2, 'Alice', 'Bob']]

person = pd.DataFrame(data, columns=['personId', 'firstName', 'lastName']).astype({'personId':'Int64', 'firstName':'object', 'lastName':'object'})

data = [[1, 2, 'New York City', 'New York'], [2, 3, 'Leetcode', 'California']]

address = pd.DataFrame(data, columns=['addressId', 'personId', 'city', 'state']).astype({'addressId':'Int64', 'personId':'Int64', 'city':'object', 'state':'object'})

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(person, address, on='personId', how='left')
    return merged[['firstName', 'lastName', 'city', 'state']]

print(combine_two_tables(person, address))

