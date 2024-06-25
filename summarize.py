import requests

headers = {
    'accept': 'application/json',
}

def summarize(text):
    params = {
        'text': text
    }
    response = requests.post('https://stestoni91-docker-space.hf.space/', params=params, headers=headers)
    return response.json()['summary']