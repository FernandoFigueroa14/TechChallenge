# syntax=docker/dockerfile:1

FROM python:3.11.0a1-bullseye

#Directory for our application
WORKDIR /app

#install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

#Copy our source code
COPY . .

#Run script
CMD [ "python3", "challenge.py"]