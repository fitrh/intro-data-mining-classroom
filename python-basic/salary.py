salary = float(input("Salary\t\t\t: "))
salary_increasing = 0
new_salary = 0
total_salary = 0

if salary > 2000:
    salary_increasing = salary * 0.4
    new_salary = salary + salary_increasing
    total_salary = new_salary + 750
elif salary > 1200:
    salary_increasing = salary * 0.7
    new_salary = salary + salary_increasing
    total_salary = new_salary + 500
elif salary > 800:
    salary_increasing = salary * 0.10
    new_salary = salary + salary_increasing
    total_salary = new_salary + 200
elif salary > 400:
    salary_increasing = salary * 0.12
    new_salary = salary + salary_increasing
    total_salary = new_salary + 150
else:
    salary_increasing = salary * 0.15
    new_salary = salary + salary_increasing
    total_salary = new_salary + 100

print("Salary Increasing\t: %.2f" % salary_increasing)
print("New Salary\t\t: %.2f" % new_salary)
print("Total\t\t\t: %.2f" % total_salary)
