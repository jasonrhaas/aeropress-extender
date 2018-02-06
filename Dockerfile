FROM python:3-slim-jessie

# Track build number (for automated build systems)
ARG BUILD_NUMBER=0
ENV BUILD_NUMBER $BUILD_NUMBER

# Set up code directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy over requirements
COPY requirements.txt .

# Install python dependencies
RUN pip install -r requirements.txt

WORKDIR /code