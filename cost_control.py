import boto3
import sys
from datetime import date
import pandas as pd

cleanupdate = date(2021, 12, 31)
from hurry.filesize import size

import threading
import time


def dry_run(bucket, prefix):
    s3 = boto3.client('s3')
    paginator = s3.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket, Prefix=prefix)

    before = []
    object_dates = []
    object_names = []
    sizes = []
    deleted = []
    objects_to_delete = []

    bytes = 0
    stopper = 0
    i = 0
    for page in pages:
        for o in page['Contents']:
            if o["LastModified"].date() < cleanupdate:
                stopper = stopper + 1
                i = i + 1
                bytes += int(o['Size'])
                before.append(cleanupdate)
                object_dates.append(o["LastModified"].date())
                object_names.append(BUCKET_NAME + "/" + o["Key"])
                sizes.append(size(int(o['Size'])))

                objects_to_delete.append({'Key': o["Key"]})
                # print(objects_to_delete)
                # resp = s3.delete_object(Bucket=bucket, Key=o["Key"])
                # print(resp)
                # print(objects_to_delete[0:10])

                if len(objects_to_delete) > 999:
                    s3_new = boto3.resource('s3')
                    #
                    my_bucket = s3_new.Bucket(bucket)
                    # print(objects_to_delete)
                    response = my_bucket.delete_objects(
                        Delete={
                            'Objects': (objects_to_delete)
                        }
                    )
                    print(response['Deleted'])
                    print(len(objects_to_delete))
                    print(len(response))


                    #
                    # print("{before}, {date}, {object}, {size}, {totalled}".format(before=cleanupdate,
                    #                                                               date=o["LastModified"].date(),
                    #                                                               object=BUCKET_NAME + "/" + o["Key"],
                    #                                                               size=o['Size'], totalled=size(bytes)))

                    objects_to_delete = []
                    data = pd.DataFrame({'before': before,
                                         'date': object_dates,
                                         'name': object_names,
                                         'size': sizes,
                                         })

                    data.sort_values(by=['date', 'size'], ascending=False)
                    data.to_csv(bucket + "." + prefix, encoding='utf-8', index=False)

            # print(response)

    # print(response)

    print(f"for prefix: {prefix} total cleanup {size(bytes)}, files before: {cleanupdate}")
    return f"for prefix: {prefix} total cleanup {size(bytes)}, files before: {cleanupdate}"


if __name__ == '__main__':
    BUCKET_NAME = sys.argv[1]
    prefix_list = sys.argv[2:]
    print(BUCKET_NAME)
    print(prefix_list)
    stats = []

    for prefix in prefix_list:
        stats.append(dry_run(BUCKET_NAME, prefix))
    print(stats)
