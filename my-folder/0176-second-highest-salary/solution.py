import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_values = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if len(sorted_values) >= 2:
        return pd.DataFrame({'SecondHighestSalary': [sorted_values.iloc[1]]})
    return pd.DataFrame({'SEcondHighestSalary': [None]})
