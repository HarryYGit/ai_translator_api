# Use Python 3.10 as the base image
FROM python:3.10

# Set the working directory in the container to the directory containing manage.py
WORKDIR /trans_ai_api

RUN apt-get update && apt-get install -y \
    libsndfile1 \
    libsox3 \
    libsox-fmt-all \
    && apt-get clean

# Copy the current directory contents into the container at /trans_ai_api/trans_ai_api
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Django app
EXPOSE 8000

CMD ["python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

# Run the Django server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
