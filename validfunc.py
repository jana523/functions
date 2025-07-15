def validmail(email):
    if '@' in email and '.' in email:
        username, domain = email.split('@')
        if username and domain:
            x,y=domain.split('.')
            if x and y:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

emails = ["ali@gmail.com","sara@yahoo.com","mohamed@outlook.com","nohaiti.gov.eg"]
valid = filter(validmail,emails)
print(list(valid))