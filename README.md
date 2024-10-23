# Trans AI API

This project is a Django-based API with machine learning capabilities using **Transformers** and **PyTorch**. The application includes authentication, CORS support, and JWT for secure API access.

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
git clone https://github.com/your_username/trans_ai_api.git
cd trans_ai_api

## Run in local

To install the necessary dependencies, you can run:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

The api will be accessible at [http://localhost:8000]

## Run in docker
docker-compose build
docker-compose -f docker-compose.yml up








