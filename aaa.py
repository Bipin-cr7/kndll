import pandas as pd


data = {
    'Employee': ['Alice', 'Bob', 'Alice', 'Charlie', 'bipin', 'Alice', 'Charlie', 'Bob', 'David', 'Alice'],
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03',
             '2024-01-03', '2024-01-03', '2024-01-04', '2024-01-04', '2024-01-04'],
    'Hours_Worked': [9, 7, 10, 8, 12, 9, 9, 11, 6, 10]
}


df = pd.DataFrame(data)


overtime_threshold = 8


df['Overtime_Hours'] = df['Hours_Worked'].apply(lambda x: max(0, x - overtime_threshold))


overtime_sum = df.groupby('Employee')['Overtime_Hours'].sum().reset_index()


max_overtime = overtime_sum['Overtime_Hours'].max()


max_overtime_employees = overtime_sum[overtime_sum['Overtime_Hours'] == max_overtime]


if len(max_overtime_employees) > 1:
    
    avg_hours = df.groupby('Employee')['Hours_Worked'].mean().reset_index()
   
    max_overtime_employees = max_overtime_employees.merge(avg_hours, on='Employee', suffixes=('', '_Avg'))
    
    result_employee = max_overtime_employees.loc[max_overtime_employees['Hours_Worked_Avg'].idxmax()]
else:
    result_employee = max_overtime_employees.iloc[0]


print(f"The employee who worked the most overtime hours is: {result_employee['Employee']} "
      f"with {result_employee['Overtime_Hours']} overtime hours.")