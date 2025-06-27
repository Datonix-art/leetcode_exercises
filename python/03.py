import pandas as pd

data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['Id', 'Salary']).astype({'Id':'Int64', 'Salary':'Int64'})

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N > len(employee) or N < 1:
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})
    nThSalary = employee['Salary'].drop_duplicates().sort_values(ascending=False).iloc[N - 1]
    return pd.DataFrame({f'getNthHighestSalary({N})': [nThSalary]})

print(nth_highest_salary(employee, 3))