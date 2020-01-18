import requests

BASE_URL = ' http://127.0.0.1:5000'

class ApiInstance:
  @classmethod
  def getExample1(cls, cb):
    respose = requests.get(f'{BASE_URL}/example1')
    if respose.ok:
      cb(respose.text)

  @classmethod
  def getHome(cls, cb):
    response = requests.get(f'{BASE_URL}/home')
    if response.ok:
      cb(response.text)

  @classmethod
  def postSearch(cls, searchQuery):
    # TODO sanatize the Query
    header = {
      'Accepts': 'application/json',
      'Content Type': 'application/json'
    }
    data = {
      'query': searchQuery
    }
    response = requests.post(f'{BASE_URL}/search', data=data, headers=header)
    searchId = response.text
    if response.ok:
      pollResponse = None
      while not (pollResponse and pollResponse.ok and pollResponse):
        pollResponse = requests.get(f'{BASE_URL}/search/{searchId}')
      return pollResponse.text
    else:
      raise ApiUnavailableError

class ApiUnavailableError(Exception):
  def __str__(self):
    return 'API unavailable'

