import boto3
import json
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def get_secret():
    secret_name = "ASKLAWYER_OPENAI_API_KEY"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except NoCredentialsError:
        print("Credentials not available")
        return None
    except PartialCredentialsError:
        print("Incomplete credentials provided")
        return None

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']

    # Parse and return the secret
    secret_dict = json.loads(secret)
    return secret_dict['OPENAI_API_KEY']