FROM python:alpine3.15
WORKDIR /usr/app
COPY . .
RUN pip install bottle
CMD [ "python", "api.py" ]
