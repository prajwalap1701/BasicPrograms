import json
 
# Create sample_fun function
 
 
def sample_fun():
 
    # Define Variable
    language = "Python"
    company = "MyCompany"
    Itemid = 1
    price = 0.00
 
    # Create Dictionary
    value = {
        "language": language,
        "company": company,
        "Itemid": Itemid,
        "price": price
    }
 
    # Dictionary to JSON Object using dumps() method
    # Return JSON Object
    return json.dumps(value)
 
 
# Call Function and Print it.
print(sample_fun())
