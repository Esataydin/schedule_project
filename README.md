## Implementing JWT Authentication

This project uses JSON Web Tokens (JWT) for authentication. Below are the steps to implement JWT authentication in your Django REST API.

### Step 1: Install Dependencies

Make sure you have the `djangorestframework-simplejwt` package installed. If it's not included in your `requirements.txt`, you can install it via pip:

```bash
pip install djangorestframework-simplejwt
```

### Step 2: Update settings.py
Add the following configuration to your `schedule_app/settings.py` file to enable JWT authentication:

```python
# schedule_app/settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

### Step 3: Create Token Views
In your `schedule_app/urls.py`, add paths to obtain and refresh tokens:
```python
# urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

### Step 4: Obtain JWT Tokens
To authenticate a user and obtain a JWT token, send a POST request to the /api/token/ endpoint with your username and password:
#### Request
```http
POST /api/token/
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}
```

#### Response
If the credentials are correct, you will receive a response containing the access and refresh tokens:
```json
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```

### Step 5: Refresh JWT Tokens
To refresh the access token, send a POST request to the /api/token/refresh/ endpoint with the refresh token:
#### Request
```http
POST /api/token/refresh/
Content-Type: application/json

{
  "refresh": "your_refresh_token"
}
```

#### Response
If the refresh token is valid, you will receive a new access token:
```json
{
  "access": "new_access_token"
}
```

### Step 6: Use JWT for Authentication
To access protected endpoints, include the access token in the Authorization header of your requests:
```http
Authorization: Bearer your_access_token
```

#### Example
Here’s an example of a request to create a weekly schedule with JWT authentication:
```http
POST /api/weekly_schedule/
Authorization: Bearer your_access_token
Content-Type: application/json

{
  "schedule": {
    "monday": [
      {
        "start": "00:00",
        "stop": "01:00",
        "ids": [1]
      }
    ]
  }
}
```

#### Notes
* Ensure that the user model used for authentication has the necessary fields (username and password).
* You can customize the token claims by creating a custom token serializer if needed.

With these steps, you should have a fully functional JWT authentication system in your Django REST API.