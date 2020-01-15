import boto3
# import sys
import click

session = boto3.Session(profile_name = 'test')
ec2 = session.resource('ec2')

@click.command()
def list_instances():
    for item in ec2.instances.all():
        print(', '.join((
            item.id,
            item.instance_type,
            item.placement['AvailabilityZone'])))
    return

if __name__ == '__main__':
#    print(sys.argv)
    list_instances()
