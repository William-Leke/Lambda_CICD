import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hey from github actions vscode cicd pipeline')
    }