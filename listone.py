import boto3

Client = boto3.client('ec2',region_name='us-west-1')

listec2=Client.describe_instances()

##print(listec2['Reservations'])


for output1 in listec2['Reservations']:
    for output2 in output1['Instances']:
        for output3 in output2['Tags']:
            print(output2['InstanceId'],'[',output3['Key'],':',output3['Value'],']')

