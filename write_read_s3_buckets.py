import boto
import boto.s3.connection
from boto.s3.key import Key

# Set variables (keys, bucket, etc.)
access_key = ''
secret_key = ''
bucket = '' # bucket name e.g. cyber-siem
key_name = '' # key name associated with bucket e.g. iocs
local_path_up = '' # local path of file to upload e.g. /Users/jesse/iocs_up.tar.gz
local_path_dl = '' # local path to store file to e.g. /Users/jesse/iocs_down.tar.gz

# S3 connect 
conn = boto.connect_s3(aws_access_key_id = access_key, aws_secret_access_key = secret_key)

# Set bucket/key to work with
bucket = conn.get_bucket(bucket)
k = Key(bucket)
k.key = key_name

# Write file to S3 bucket/key - uncomment to write to bucket/key
#k.set_contents_from_filename(local_path_up)

# Download file from S3 bucket/key - uncomment to read from bucket/key
#k.get_contents_to_filename(local_path_dl)



