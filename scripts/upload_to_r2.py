import os
import sys

def upload_r2(account_id, access_key, secret_key, bucket_name):
    try:
        import boto3
    except ImportError:
        print("boto3 package required. Installing via pip...")
        os.system("pip install boto3")
        import boto3

    s3 = boto3.client(
        's3',
        endpoint_url=f'https://{account_id}.r2.cloudflarestorage.com',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name='auto'
    )

    base_dir = r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist'
    
    for folder in ['images', 'docs']:
        target = os.path.join(base_dir, folder)
        if os.path.exists(target):
            for root, _, files in os.walk(target):
                for file in files:
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, base_dir).replace('\\', '/')
                    
                    content_type = 'application/octet-stream'
                    if file.endswith('.png'): content_type = 'image/png'
                    elif file.endswith('.jpg') or file.endswith('.jpeg'): content_type = 'image/jpeg'
                    elif file.endswith('.svg'): content_type = 'image/svg+xml'
                    elif file.endswith('.pdf'): content_type = 'application/pdf'
                    
                    print(f"Uploading {rel_path} to R2 bucket '{bucket_name}'...")
                    s3.upload_file(
                        full_path,
                        bucket_name,
                        rel_path,
                        ExtraArgs={'ContentType': content_type}
                    )
    print("All assets successfully uploaded to Cloudflare R2!")

if __name__ == '__main__':
    if len(sys.argv) == 5:
        upload_r2(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Usage: python upload_to_r2.py <ACCOUNT_ID> <ACCESS_KEY> <SECRET_KEY> <BUCKET_NAME>")
