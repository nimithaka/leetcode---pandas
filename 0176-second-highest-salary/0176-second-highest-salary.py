import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    second_highest = employee['salary'].drop_duplicates().nlargest(2)
    second_highest = second_highest.iloc[-1] if len(second_highest) == 2 else None
    return pd.DataFrame({'secondHighestSalary':[second_highest]})
    
    