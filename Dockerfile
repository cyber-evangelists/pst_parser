# Use an official Ubuntu image as a parent image
FROM ubuntu:20.04

# Set the working directory in the container
WORKDIR /app

# Update the package repository and install Python 3
RUN apt-get update && apt-get install -y python3

# Copy the current directory contents into the container at /app

COPY main.py mbox_parser.py requirements.txt /app/

RUN mkdir /app/target_files

# Install any needed Python packages specified in requirements.txt for your Python application
RUN apt-get install -y python3-pip && pip3 install -r requirements.txt

# Install "readpst" in the container
RUN apt-get install -y pst-utils

# Run the Python script (replace "main.py" with the actual entry point of your Python application)
CMD ["python3", "main.py"]
