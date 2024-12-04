# Trans AI API

This project is a Django-based API with machine learning capabilities using **Transformers** and **PyTorch**. The application includes authentication, CORS support, and JWT for secure API access.

# Prerequisites

- Python 3.10 or higher
- Docker and Docker Compose
- Virtual environment (optional, but recommended)

# Environment Variables

Ensure to set the following environment variables in your `.env` file (if applicable):
- `SECRET_KEY`: Django secret key for cryptographic signing.
- `DEBUG`: Set to `True` for development; `False` for production.

## Testing the API

You can test the API using tools like Postman or directly via `curl`. Below are examples of how to make requests using `curl`.


# Dependencies
### As shown in requirements.txt
- Django==4.2
- djangorestframework==3.14.0
- transformers==4.31.0
- torch==2.0.1
- django-cors-headers==4.4.0
- djangorestframework-simplejwt==5.3.1
- langdetect==1.0.9

# Getting Started
1. Clone the repository
```bash
git clone https://github.com/your_username/trans_ai_api.git
cd trans_ai_api
```

## Run in local

To install the necessary dependencies, you can run:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The api will be accessible at [http://localhost:8000]

## Run in docker
```bash
docker login
docker-compose build
docker-compose -f docker-compose.yml up
```

# API Endpoints

### The following endpoints are available in the API:

- **Translate**
  - **Endpoint:** `/api/translate/`
  - **Method:** `POST`
  - **Description:** Detect Language of user input. Detect System Language of user. Translates the user input text into detected language or user choosen target language or default target lang 'eng-Latn'. Requires Access Token in header, Auth type Bearer Token. Requires source_text and target_lang. 

- **User Registration**
  - **Endpoint:** `/api/auth/register/`
  - **Method:** `POST`
  - **Description:** Registers a new user, generate refresh token and access token. Requires user details username and password in the request body.

- **Obtain Token**
  - **Endpoint:** `/api/auth/obtaintoken/`
  - **Method:** `POST`
  - **Description:** Obtains access token and refresh token to registered user. Requires username and password.

- **Token Refresh**
  - **Endpoint:** `/api/token/refresh/`
  - **Method:** `POST`
  - **Description:** Refreshes the JWT token using a valid refresh token. Requires refresh token.

## Usage

1. **Translating Text:**
   To translate text, send a `POST` request to `/api/translate/` with the necessary payload.
   
2. **Mutil Language Audio Detect:**
   To detect audio, send a `POST` request and auiod file to `/api/translate/` with the necessary payload.

3. **Registering a User:**
   Send a `POST` request to `/api/auth/register/` with the user's information (username, password) to register and get refresh token and access token.

4. **Obtaining a Token:**
   Authenticate a user by sending a `POST` request to `/api/auth/obtaintoken/` with the username and password. This will return a JWT token.

5. **Refreshing the Token:**
   Use a valid refresh token to get a new JWT by sending a `POST` request to `/api/token/refresh/`.

## Example Requests

#### Register user
```json
{
    "username": "testname9",
    "password": "Testname@123"
}
```

```bash
curl -X POST http://localhost:8000/api/auth/register/ \
-H "Content-Type: application/json" \
-d '{"username": "testname9", "password": "Testname@123"}'
```

output:
```json
{
    "user": {
        "username": "testname9"
    },
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyOTY0OTI0MSwiaWF0IjoxNzI5NTYyODQxLCJqdGkiOiJiYjQ4ZmQyOGU4MTE0Yzk3OTVmNjk1MGY4MGFiOGY1YSIsInVzZXJfaWQiOjEzfQ.aeI0TirkIkepYWAdgm02qafZGYDz8hC0hokb08nybdI",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyMTU0ODQxLCJpYXQiOjE3Mjk1NjI4NDEsImp0aSI6IjkxZmZhOWE1MzZhMDRjYzQ5MjIyMmJmMjY2MDFhOTBkIiwidXNlcl9pZCI6MTN9.K0hQuuSKAMptsGJlCj6Tug5tnknyCF8u6EfGCrVnizI",
    "message": "User registered successfully"
}
```

#### Obtain token
```json
{
    "username" : "testname9",
    "password" : "Testname@123"
}
```

```bash
curl -X POST http://localhost:8000/api/auth/obtaintoken/ \
-H "Content-Type: application/json" \
-d '{"username": "testname9", "password": "Testname@123"}'
```

output:
```json
{
    "user": {
        "username": "testname9"
    },
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyOTY1MjA0MCwiaWF0IjoxNzI5NTY1NjQwLCJqdGkiOiIwZjcwMDExYTEzMjI0MDUwOGNmZjIwNTE4YmNkY2FkMCIsInVzZXJfaWQiOjEzfQ.eIGQyCHlc3D5LHw_jHa5wH5ZUqA8nkEKRIRiwfUTI5E",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5NTY1OTQwLCJpYXQiOjE3Mjk1NjU2NDAsImp0aSI6ImY4NzExNGY1YWUwZjRhZGRhMGMzNTdlYmM3N2UxNGY2IiwidXNlcl9pZCI6MTN9.J8jOOnERIwHABNop42sDVmnGlgcavGDU44nKu_XRVXs",
    "message": "Token generated successfully"
}
```


#### Translate Text
```json
{
    "source_text": "El rápido zorro marrón salta sobre el perro perezoso",
    "target_lang": "ace_Arab"
}
```

```bash
curl -X POST http://localhost:8000/api/translate/ \
-H "Authorization: Bearer <your_token>" \
-H "Content-Type: application/json" \
-d '{"text": "Hello, world!", "target_language": "fr"}'
```
output:
```json
{
    "source_text": "El rápido zorro marrón salta sobre el perro perezoso",
    "source_lang": "es",
    "target_lang": "eng_Latn",
    "trans_text": "The fast brown fox jumps over the slothful dog."
}
```

#### License
This project is licensed under the MIT License - see the LICENSE file for details.
