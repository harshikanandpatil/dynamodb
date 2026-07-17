import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Student')

table.put_item(
 Item={
  'StudentID':'STU002',
  'Name':'Atul amble',
  'City':'burhanpur'
 }
)

print("Student Added Successfully")
