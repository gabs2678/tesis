# Use an official Python runtime as a parent image
FROM python:3.9.6

# Set the working directory in the container
WORKDIR /app/mytesis

# Copy the current directory contents into the container at /app/mytesis
COPY mytesis/ /app/mytesis/

# Install any needed packages specified in requirements.txt
RUN python -m pip freeze > requirements.txt && pip install --no-cache-dir -r requirements.txt
RUN pip install Django==4.2.13

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
