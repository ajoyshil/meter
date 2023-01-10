# meter
Coding challenge 

# This repository is Django framework codebase.

# Clone this project and run below command to start local server

  1. pip install -r requirements.txt
  2. python manage.py makemigrations
  3. python manage.py migrate 
  4. python manage.py runserver
  
 

# API
  1. /meters
  2. /meters/<int:pk>
  
  
# Sample Response 

# http://127.0.0.1:8000/meters

[
    {
        "url": "http://127.0.0.1:8000/meters/1",
        "label": "meter 1"
    },
    {
        "url": "http://127.0.0.1:8000/meters/2",
        "label": "meter 2"
    },
    {
        "url": "http://127.0.0.1:8000/meters/3",
        "label": "William Green"
    },
 ]
 
 
# http://127.0.0.1:8000/meters/58
 
 [
    {
        "id": 31,
        "value": 9393848,
        "timestamp": "2023-01-10T05:48:31.379181Z"
    }
]
