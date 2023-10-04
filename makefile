#############################
# Application Make Commands #
#############################

####################
# RC Make Commands #
####################

# Binding to docker for building the image. Built this way for consistency
# between "risingcloud" and "web" mode applications.
rc-build-test-image:
	docker build --tag bp-python-flask-service . 

# Spin up the test-container. Stop and delete an old one if it exists. We attach
# a volume mapping the development directory to the container app to aid with
# quick dev. Many langauges and frameworks for APIs support hot reloads that can
# keep the container deployment up to date without requiring a rebuild.
rc-start-container:
	make rc-kill-container
	docker run -d --name bp-python-flask-service --volume ${PWD}:/app bp-python-flask-service

# Stops and removes the existing bp-python-flask-service container
rc-kill-container:
	docker stop bp-python-flask-service || true
	docker rm bp-python-flask-service || true

# Tests a single request. This assumes the test container is already up and
# running and the request file is passed in as $(f). The resulting data will
# be saved in ./rcTests/responses/$(f).
# Example usage: `make rc-test-single f={TEST_NAME}`
# Don't include the full path to the test. The command will automatically
# look for it in the ./rcTests/requests folder and add the .json extension.
rc-test-single:
	docker exec bp-python-flask-service python3 appTest.py $(f)

# Iterates through every test file in ./rcTests/requests and writes the output
# of every test file to ./rcTests/responses under the same name.
rc-test-all:
	docker exec bp-python-flask-service python3 appTest.py
