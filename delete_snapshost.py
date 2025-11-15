# Delete unused snapshot whose volume is not attached to EC2.

import boto3
from botocore.exceptions import ClientError
ec2   = boto3.client('ec2')

snapshot_response=ec2.describe_snapshots(
    Filters=[
        {
            'Name': 'tag:env',
            'Values': ['dev']
        },
    ]

)
if (len(snapshot_response['Snapshots']))==0:
    print('No snapshots found')
    exit
for snapshots in snapshot_response['Snapshots']:
    snapshot_id=snapshots['SnapshotId']
    volume_id=snapshots['VolumeId']
    if not volume_id:
        ec2.delete_snapshot(
            SnapshotId=snapshot_id,
        )
        print(f'Deleted {snapshot_id} with no volume attached')
        continue
    else:
        try:
            volume_response=ec2.describe_volumes(
                VolumeIds=[
                    volume_id,
                ],
            )
            if not volume_response['Volumes'][0]['Attachments']:
                ec2.delete_snapshot(
                    SnapshotId=snapshot_id,
                )
                print(f"Deleting snapshot {snapshot_id}")

        except ClientError as e:
            if 'InvalidVolume.NotFound' in str(e):
                print(f"Volume {volume_id} not found. Deleting snapshot {snapshot_id}...")
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted snapshot {snapshot_id}")
            else:
                print(f"Error processing snapshot {snapshot_id}: {e}")
            



