# Star Wars Planet Browser

A flask app which retrieves and displays the Star Wars API (SWAPI) planet data.
I made this app to learn how to use APIs and pytest.

(View Page)[https://lisas7.github.io/SWPlanets/]

### swapi.py 
BasicApi class: retrieves the data from SWAPI and caches it. 
I've tried to make this as reusable as possible for other APIs. I added caching as the requests were taking a few seconds to return data.

Planet class: takes the dictionary returned by the BasicApi class and uses the data to create a Planet object.


What I learned:
* Setting up linting in VSCode with Flake8 and changing settings
* Using requests to get data from an API
* Caching the response
* Creating tests and fixtures with pytest

Resources:
(SWAPI Planets Documentation)[https://swapi.dev/documentation#planets]
(How to use APIs)[https://realpython.com/api-integration-in-python/]
(Caching)[https://realpython.com/caching-external-api-requests/]