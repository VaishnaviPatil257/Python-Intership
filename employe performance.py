employee = "EMP 60|VAISHNAVI|Python Developer|Excellent"

# Find positions of |
first = employee.find("|")
second = employee.find("|", first + 1)
third = employee.find("|", second + 1)

# Extract information
employee_id = employee[:first]
employee_name = employee[first + 1:second]
job_role = employee[second + 1:third]
performance = employee[third + 1:]

# Convert name to title case
employee_name = employee_name.title()

# Convert job role to lowercase
job_role = job_role.lower()

# Check performance
if performance == "Excellent":
    status = "High Performer"
else:
    status = "Needs Improvement"

# Display report
print("\nEMPLOYEE PERFORMANCE REPORT")
print("---------------------------")
print("Employee ID  :", employee_id)
print("Employee Name:", employee_name)
print("Job Role     :", job_role)
print("Performance  :", performance)
print("Status       :", status)
















