FROM python:3.11.0-slim-buster 
# set work directory
WORKDIR /app

# set environment variables


# install dependencies
RUN pip install --upgrade pip 
COPY requirments.txt requirments.txt
RUN pip3 install -r requirments.txt

# copy project
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]