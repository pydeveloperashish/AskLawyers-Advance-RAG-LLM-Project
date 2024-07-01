import boto3

def search_kendra(query_text):
    # Initialize the Kendra client
    client = boto3.client('kendra', region_name='us-east-1')

    try:
        # Send query to Kendra
        response = client.query(
            IndexId='99a9ffbd-4e42-40a4-883a-35c2f6e40301',
            QueryText=query_text
        )

        # Extract and return relevant context from the response
        if 'ResultItems' in response:
            for result in response['ResultItems']:
                if 'DocumentExcerpt' in result:
                    print(result['DocumentExcerpt']['Text'])

    except Exception as e:
        print(f"Error querying Kendra: {e}")

# Example usage:
search_kendra("What is Indian Panel Code?")
