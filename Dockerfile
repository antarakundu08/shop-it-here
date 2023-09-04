FROM python:3.8-slim-buster
WORKDIR app
COPY . .
RUN pip install flask
RUN pip install Flask-SQLAlchemy
RUN pip install flask-login
EXPOSE 5000
CMD ["python","main.py"]
