# For simple flask apps, a small base image like python:alpine is prefered as
# it is less resource intensive. This can be modified accordingly if your app
# has more rigorous runtime requirements.
FROM python:alpine

# Because we begin from an image that already has python installed, we just
# need to copy in the requirements and run the pip install command
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python -m pip install -r requirements.txt

# Copy over all the code to the image and expose the appropriate port
COPY . /app
EXPOSE 8080

CMD ["python", "app.py"]