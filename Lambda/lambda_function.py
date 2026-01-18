import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('goodnight from our github actions vscode cicd pipeline!')
    }