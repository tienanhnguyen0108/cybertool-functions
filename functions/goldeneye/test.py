
from app import lambda_handler

id_token = 'eyJraWQiOiJCbjk4ZEF3ajNUVG1scUNkc21XY1wvakoxVU01eDJWaHFiMGk5c0dzSmJyUT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIyNDA0YTQ0YS04Mjc2LTRjMjctYTNlMy1mMTdkZDlkZDViMzYiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmFwLXNvdXRoZWFzdC0xLmFtYXpvbmF3cy5jb21cL2FwLXNvdXRoZWFzdC0xXzA5OW5oamlsbiIsInBob25lX251bWJlcl92ZXJpZmllZCI6ZmFsc2UsImNvZ25pdG86dXNlcm5hbWUiOiIyNDA0YTQ0YS04Mjc2LTRjMjctYTNlMy1mMTdkZDlkZDViMzYiLCJhdWQiOiIzczM3cWNhYjRiZGlicGw3dXM4NXA4bnNyNyIsImV2ZW50X2lkIjoiZjExZWFkZmUtZmI4Mi0xMWU4LTgxNjQtNGRkOWRlNGNkYTRmIiwidG9rZW5fdXNlIjoiaWQiLCJhdXRoX3RpbWUiOjE1NDQzNDAwNDQsIm5hbWUiOiJDaHJpc3RpYW4gV2VuIiwicGhvbmVfbnVtYmVyIjoiKzg0ODM5Njg0NDM0IiwiZXhwIjoxNTQ0MzcxMjg0LCJpYXQiOjE1NDQzNjc2ODQsImVtYWlsIjoiY2hyaXN0aWFud2VuMThAZ21haWwuY29tIn0.YK-KuUPkbDN68VKlVyJ9m668-lHX-Ggs9FuYuqX7WOQ2YQhwG4Hk4JfsnSdnkAG5c875EJSu2SNuiXHMfMlmzRvmvAeRF7N0YXIpaKkpNbEylp83JsiRC7eSzu2t2lAoAr6R4ReJkUee6AQ56kYr8-b-9d9h3WEK6wy3ACNY38wAPX2n3B5BbnD7w1skWUA-qwY9kKYF9Zsv36LOexjQ9xvhBDQNJdq-44AJOkKDiLLzuC-UHixWBv0r-ks3gEmaPzKOMHmxORnx25HMkdBD9htUzYACmMLO9fel6nJAZSxoG6ViuJKWh-HgMj7SsNvkwwq4sCZ-7dGxBoN2vTPVlQ'

event = {
  "queryStringParameters": {
    "target": "c3chuvanan.edu.vn",
    "duration": 60,
    "id_token": id_token,
    "strength": 50
  }
}

lambda_handler(event, {})
