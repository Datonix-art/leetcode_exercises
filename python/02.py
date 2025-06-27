import pandas as pd

data = [[1, 100]]

employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id': 'int64', 'salary': 'int64'})

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_values = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if len(sorted_values) >= 2:
        return pd.DataFrame({'SecondHighestValue': [sorted_values.iloc[1]]})
    return pd.DataFrame({'SEcondHighestValue': [None]})
    

print(second_highest_salary(employee=employee))
