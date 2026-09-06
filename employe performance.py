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





#customer support ticket
ticket="Ticket-2026-DB-0456:Payment Failed"
ticket=ticket.strip()
year=ticket[7:11]
department=ticket[12:14]
ticket_number=ticket[15:19]
complaint=ticket[21:]
if ticket.startswith("TICKET"):
    valid_ticket="yes"
else:
    valid_ticket="No"
if "Failed" in complaint:
    failed="yes"
else:
    failed="no"
print("\nCUSTOMER SUPPORT TICKET REPORT")
print("--------------------")
print("ticket year:",year)
print("department code:",department)
print("ticket number:",ticket_number)
print("complaint:",complaint)
print("starts with TICKET:",valid_ticket)
print("contains failed:",failed)



#employe id and username
name="Vaishnavi Patil"
emp_ID=45757
cleaned_name=name.strip()
lower_name=name.strip()
parts=lower_name.split()
first_name=parts[0]
last_name=parts[-1]
username=first_name+""+last_name+"@company.com"
print("cleaned_name:",cleaned_name)
print("parts:",parts)
print("first_name:",first_name)
print("last_name:",last_name)
print("username:",username)



product="elec-tv-2025-001"
product=product.strip()
product=product.upper()
if product.startswith("ELEC"):
    starts_elec=True
else:
    starts_elec=False
category=product[:4]
product_type=product[5:8]
year=product[9:13]
product_number=product[14:]
hyphen_count=product.count("-")
contains_hyphen="-"in product
if starts_elec and contains_hyphen and hyphen_count==3:
    result="VALID"
else:
    result="INVALID"
print("\nPRODUCT CODE REPORT")
print("---------------")
print("product code:",product)
print("category:",category)
print("product type:",product_type)
print("year:",year)
print("product number:",product_number)
print("contains'-':",contains_hyphen)
print("number of'-':",hyphen_count)
print("status:",result)





