import boto3
# import sys
import click

session = boto3.Session(profile_name = 'test')
ec2 = session.resource('ec2')

def filer_instances(project):
    instances = []
    if project:
        filters = [{'Name':'tag:Project', 'Values':[project]}]
        instances = ec2.instances.filter(Filters = filters)
    else:
        instances = ec2.instances.all()
    return instances

@click.group()
def instances():
    """Commands for instances"""

@instances.command('list')
@click.option('--project', default = None,
    help = "Only for project")

def list_instances(project):
    "List EC2 instances"
    instances = filer_instances(project)
    for item in instances:
        tags = { t['Key']: t['Value'] for t in item.tags or []}
        print(', '.join((
            item.id,
            item.instance_type,
            item.placement['AvailabilityZone'],
            tags.get('Project', '<no project>')
            )))
    return

@instances.command('stop')
@click.option('--project', default = None,
    help = "Only for project")
def stop_instances(project):
    "Stop EC2 instances"
    instances = filer_instances(project)
    for item in instances:
        print("Stopping {0} ...".format(item.id))
        item.stop()
    return

@instances.command('start')
@click.option('--project', default = None,
    help = "Only for project")
def start_instances(project):
    "Start EC2 instances"
    instances = filer_instances(project)
    for item in instances:
        print("Starting {0} ...".format(item.id))
        item.start()
    return

if __name__ == '__main__':
#    print(sys.argv)
    instances()
