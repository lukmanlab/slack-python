import urllib3
import json

WEBHOOK_URL = 'https://hooks.slack.com/services/ABCDEFGHIJ/ABCDEFGHIJ/xxxxxxxxxxxxxxxxxxxx'

def postSlack(message):
    encoded_data = json.dumps(message).encode('utf-8')
    http = urllib3.PoolManager()
    response = http.request('POST',
        WEBHOOK_URL, body=encoded_data,
        headers={'Content-Type': 'application/json'}
    )
    status_code = response.status
    if status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s'
            % (status_code)
        )

data = {'text': 'Testing!'}

postSlack(data)