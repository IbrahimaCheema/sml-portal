import os
import sys

def load_env():
    env_file = os.path.expanduser('~/.env')
    if not os.path.exists(env_file):
        env_file = '.env'
    if os.path.exists(env_file):
        with open(env_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, val = line.split('=', 1)
                    os.environ[key.strip()] = val.strip()

def upload_r2():
    load_env()
    
    account_id = os.getenv('R2_ACCOUNT_ID')
    access_key = os.getenv('R2_ACCESS_KEY_ID')
    secret_key = os.getenv('R2_SECRET_ACCESS_KEY')
    bucket_name = os.getenv('R2_BUCKET_NAME', 'sml-uploads')

    if not account_id or not access_key or not secret_key:
        print("ERROR: Missing R2_ACCOUNT_ID, R2_ACCESS_KEY_ID, or R2_SECRET_ACCESS_KEY in environment or ~/.env")
        sys.exit(1)

    try:
        import boto3
    except ImportError:
        print("Installing boto3...")
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
    
    total_uploaded = 0
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
                    total_uploaded += 1
    print(f"SUCCESS: {total_uploaded} media assets uploaded to Cloudflare R2 bucket '{bucket_name}'!")

if __name__ == '__main__':
    upload_r2()
