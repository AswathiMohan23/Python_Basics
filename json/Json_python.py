# json string to python object
import json
employee_details = '''
{
"employee":[
{
"emp_name":"Tom",
"emp_no":"12345",
"emp_email":["tom@gmail.com"]

},
{
"emp_name":"Ravi",
"emp_no":"56789",
"emp_email":["ravi@gmail.com"]

}
]
}
'''
data = json.loads(employee_details)
print(data)