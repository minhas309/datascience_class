import pandas as pd
# Start coding here...

office_add = pd.read_csv('./datasets/office_addresses.csv')
employee_roles = pd.read_json('./datasets/employee_roles.json', orient='index')
employee_info = pd.read_excel('./datasets/employee_information.xlsx')
column = ['employee_id', 'employee_last_name', 'employee_first_name', 'emergency_contact', 'emergency_contact_number', 'relationship']
employee_contacts = pd.read_excel('./datasets/employee_information.xlsx', sheet_name='emergency_contacts', header=None, names=column )


employees_final = pd.concat([employee_info, employee_contacts], ignore_index=True)

employee_roles = employee_roles.reset_index()
employee_roles.columns = ['employee_id'] + list(employee_roles.columns[1:])

employees_final = employees_final.merge(employee_roles, left_on='employee_id', right_on='employee_id')

print(employees_final)
employees_final = employees_final.merge(office_add,how='inner', left_on='employee_country', right_on='office_country')

# Rename columns as required
employees_final.rename(columns={
    'employee_last_name': 'last_name',
    'employee_first_name': 'first_name',
}, inplace=True)

# Reorder columns as specified
desired_columns = ['employee_id', 'first_name', 'last_name', 'employee_country', 'employee_city', 'employee_street',
                   'employee_street_number', 'emergency_contact', 'emergency_contact_number', 'relationship',
                   'monthly_salary', 'team', 'title', 'office', 'office_country', 'office_city', 'office_street',
                   'office_street_number']

employees_final = employees_final[desired_columns]
employees_final.set_index('employee_id', inplace=True)
