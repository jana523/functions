def emails_domain():
     emails = ["ali@gmail.com","sara@yahoo.com","mohamed@outlook.com","noha@iti.gov.eg"]
     domains = list(map(lambda x: x.split("@")[1], emails))
     print(domains)
emails_domain()
