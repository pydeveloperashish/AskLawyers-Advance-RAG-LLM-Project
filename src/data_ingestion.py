import os
import boto3

# Initialize S3 client
s3_client = boto3.client('s3')

# Define your S3 bucket
bucket_name = 'asklawyers-bucket-s3'

# Function to upload a file to S3
def upload_pdf_to_s3(bucket, local_path, s3_key):
    try:
        s3_client.upload_file(local_path, bucket, s3_key)
        print(f'Successfully uploaded {local_path} to S3 bucket: {bucket}/{s3_key}')
    except Exception as e:
        print(f'Error uploading file to S3: {e}')

# Function to upload all PDF files from a directory to S3
def upload_pdfs_from_directory(directory, bucket_name):
    try:
        for filename in os.listdir(directory):
            if filename.endswith('.pdf'):
                local_path = os.path.join(directory, filename)
                s3_key = f'pdf_files/{filename}'  # Customize the S3 key as needed
                upload_pdf_to_s3(bucket_name, local_path, s3_key)
    except Exception as e:
        print(f'Error uploading PDFs from directory: {e}')

# Example usage
input_dir = r'dataset\Indian Penal Code Book (2)_chunks'

upload_pdfs_from_directory(input_dir, bucket_name)
