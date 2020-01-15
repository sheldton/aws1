import boto3

session = boto3.Session(profile_name = 'test')

ec2 = session.resource('ec2')

for item in ec2.instances.all():
    print(item)
