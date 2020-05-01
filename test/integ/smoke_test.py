import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import os


# very simple test checking 200 on localhost:5000
# requires to run docker-compose:
# > docker-compose -f docker-compose.yml up -d
def test_http_5000_code_200():
    host = os.environ['TARGET_HOST']
    port = '5000'
    url = 'http://' + host + ':' + port

    print("Testing with: " + str(host))

    s = requests.Session()
    s.mount(url, HTTPAdapter(max_retries=Retry(total=3, backoff_factor=1)))
    r = s.get(url)
    assert r.status_code == 200

