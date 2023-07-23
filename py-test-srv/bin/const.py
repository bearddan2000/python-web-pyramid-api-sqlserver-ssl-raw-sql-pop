URL = 'http://py-srv:6543'

GET_ALL_URL = URL + '/pop'

GET_BY_FILTER_URL = URL + '/pop/3'

STATIC = {  
    "results": [
    {
      "color": "brown",
      "id": 1,
      "name": "RC Cola"
    },
    {
      "color": "clear",
      "id": 2,
      "name": "Sprite"
    },
    {
      "color": "brown",
      "id": 3,
      "name": "Verners"
    },
    {
      "color": "green",
      "id": 4,
      "name": "Mt. Lightening"
    }
  ]
}

DELETE_URL = URL + '/pop/1'

INSERT_URL = URL + '/pop/pink/lemonade'

SMOKE_URL = URL + '/'

SMOKE = {"hello": "world"}

UPDATE_URL = URL + '/pop/2/clear/crystal'
