import requests

BASE_URL = ' http://127.0.0.1:5000'

class ApiInstance:
  @classmethod
  def getExample1(cls, cb: callable) -> None:
    """
    # getExample1( cb )
    cb: a callback function which takes in a text argument

    Makes a request for example1 html from the flask server
    """
    response = requests.get(f'{BASE_URL}/example1')
    if response.ok:
      print(f'Respose: {response.text}')
      cb(response.text)

  @classmethod
  def getHome(cls, cb: callable) -> None:
    """
    # getExample1( cb )
    cb: a callback function which takes in a text argument

    Makes a request for home html from the flask server
    """
    response = requests.get(f'{BASE_URL}/home')
    if response.ok:
      cb(response.text)

  @classmethod
  def postSearch(cls, searchQuery: str) -> str:
    """
    # postSearch ( serachQuery )
    searchQuery: A search query to search the world wide web.

    The search is done through a query to the flask server.
    """
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
      while not (pollResponse and pollResponse.ok):
        pollResponse = requests.get(f'{BASE_URL}/search/{searchId}')
      return pollResponse.text
    else:
      raise ApiUnavailableError

class ApiUnavailableError(Exception):
  def __str__(self):
    return 'API unavailable'

