# use python as base image
FROM python:3.5-slim

# use working dir as /app
WORKDIR /app

# copy all contents of current dir to /app
ADD . /app

# install required packages
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# open port 5500
EXPOSE 5500

# set environment variable
ENV NAME OpentoAll

# run python program
CMD ["python","app.py"]