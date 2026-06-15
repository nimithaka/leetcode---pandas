import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee, department, left_on="departmentId", right_on="id", how="inner", suffixes=("_emp", "_dept"))
    max_salary = merged.groupby('departmentId')["salary"].transform("max")
    result = merged[merged["salary"] == max_salary]
    return result[['name_dept', 'name_emp', 'salary']].rename(columns={
        'name_dept': 'Department', 'name_emp': 'Employee', 'salary_emp': 'Salary'})


    