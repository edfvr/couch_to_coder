import data
#------BASE TASK-------
#1: Name of employee with biggest salary
highest_earner = data.employees[0]

for employee in data.employees:
    if (employee['salary'] > highest_earner['salary']):
        highest_earner = employee

print(f"{highest_earner['first_name']} {highest_earner['last_name']}\n")

#2
combined_years_experience = 0

for employee in data.employees:
    combined_years_experience += employee['years_of_experience']

print(combined_years_experience)

#3 No email
employees_without_emails = []

for employee in data.employees:
    if (not employee['email']):
        employees_without_emails.append(employee)
#print(employees_without_emails)

#4 
business_salaries = 0
product_salaries = 0

for employee in data.employees:
    if (employee['department'] == "Business"):
        business_salaries += employee['salary']
    elif (employee['department'] == "Product"):
        product_salaries += employee['salary']

if business_salaries > product_salaries:
    print(f"\nBusiness dept: {business_salaries}\nProduct dept: {product_salaries}\nBusiness department salaries cost more!")
elif product_salaries > business_salaries:
    print(f"\nBusiness dept: {business_salaries}\nProduct dept: {product_salaries}\nProduct department salaries cost more!")
else:
    print(f"\nBusiness dept: {business_salaries}\nProduct dept: {product_salaries}\nThey cost the company equally")


#------EXTENSIONS-------

#5. 
over_thirty = []
total_salary = 0
employee_count = 0

for employee in data.employees:
    if employee['age'] > 30:
        over_thirty.append(employee)

for employee in over_thirty:
    total_salary += employee['salary']
    employee_count += 1

average = total_salary / employee_count
rounded_average = round(average, 2)

print(f"\nAverage salary for people over 30 yrs is {rounded_average}\n")

#6
job_titles_dict = {}

for employee in data.employees:
    job_title = employee.get('job_title')
    if job_title in job_titles_dict:
        job_titles_dict[job_title] += 1
    else:
        job_titles_dict[job_title] = 1

print(job_titles_dict)    