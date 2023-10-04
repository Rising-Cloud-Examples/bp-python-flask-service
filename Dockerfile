# For simple flask apps, a small base image like python:alpine is prefered as
# it is less resource intensive. This can be modified accordingly if your app
# has more rigorous runtime requirements. Keep in mind, if this is modified,
# there is a good chance you will need to modify the testing commands in the
# makefile and the appTest.py file based on the new image's compatibility.
FROM python:alpine

# Because we begin from an image that already has python installed, we just
# need to copy in the requirements and run the pip install command
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python -m pip install -r requirements.txt

# Copy over all the code to the image and expose the appropriate port. If the
# port your service is serving on is not exposed, Rising Cloud (and you) will
# not be able to communicate with it.
COPY . /app
EXPOSE 8080

CMD ["python", "app.py"]