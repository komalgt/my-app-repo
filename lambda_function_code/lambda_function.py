import json

def lambda_handler(event, context):
    """
    Basic AWS Lambda function.
    Args:
        event (dict): Event data passed to the function.
        context (LambdaContext): Runtime information.

    Returns:
        dict: Response data.
    """
    print("Received event:", json.dumps(event))

    # Example: return HTTP 200 with the event payload
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello from Lambda!',
            'input': event
        })
    }
