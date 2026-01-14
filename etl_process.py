import pandas as pd 
import numpy as np 

#extract 
print('staring extract')
df = pd.read_csv('raw_employees.csv')
print('du lieu goc:')
print(df)

#transform 
#chuan hoa viet ten chu cai dau 
df['name'] = df['name'].str.title()

#dien bang luong trung binh 
avg_salary = df['salary'].mean()
df['salary'] = df['salary'].fillna(avg_salary)

#loai bo dong thieu ten 
df = df.dropna(subset=['name']) 

#load 
output_file = 'clean_employee.csv'
df.to_csv(output_file, index=False)

print('xu ly xong du lieu:')
print(df)
print(f'da luu du lieu vao: {output_file}')
