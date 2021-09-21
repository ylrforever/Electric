#Electric API

Flask API to get electricity usage data

Request
Path:	GET /api/{user_key}/limits
Description:	successful operation
Headers:	Status Code: 200
Content-Type: application/json

Example:
/api/dfsdf3kdfsl31f1h/limits

401: User key is not valid



Request
Path:	GET /api/{user_key}/data/{resolution}/{start}/{count}
Description:	successful operation
Headers:	Status Code: 200
Content-Type: application/json

Example:
/api/dfsdf3kdfsl31f1h/data/days/2020-10-01/8

401: User key is not valid
414: start date is not valid, format should be xxxx-xx-xx.
415: resolution is not valid, only days and months are valid.
416: count need to be an integer.



Installation
1. When you install Flask, please notice that openssl may need to be upgrade to the newest version.
2. If you don't have FLASK_ENV=development, you may need to reload everytime you change the files.
3. Python 3.5 or newer version is required.

