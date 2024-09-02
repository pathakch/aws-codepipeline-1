from datetime import datetime
current_datetime = datetime.now()

def lambda_fn(event, context):
    print(f"This is the current datetime {current_datetime} in region ap-south-1 ")

lambda_fn(None,None)