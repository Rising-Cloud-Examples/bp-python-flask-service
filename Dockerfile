# For simple flask apps, a small base image like python:alpine is prefered as
# it is less resource intensive. This can be modified accordingly if your app
# has more rigorous runtime requirements. The only compatibility requirement
# for your image to run on Rising Cloud is that the base image is linux based.
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