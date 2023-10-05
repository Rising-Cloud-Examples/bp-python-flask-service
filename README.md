# bp-python
This is part of the Rising Cloud Boilerplate Repositories. The purpose of
`bp-python-flask-service` and other boilerplate repositories is to quickly get
applications running on Rising Cloud, without having to worry about any of the
basic configuration that is required.

The boilerplate is functional out of the box. If you follow the steps under
the "Using this Boilerplate Repository" without making any changes, you will
have made a fully functioning Rising Cloud Task! If this is your first time
creating a Rising Cloud task of this type, it is recommended to follow those
steps below with no modifications first. After you have seen the build process
and are comfortable with the layour, adjust the code to fit individual needs.

This application demonstrates a working app in base python, with no added
dependencies/libraries/packages. It is intended to use the CLI to create a
task based on this code. If you did not use the CLI, please install it from
[here](https://risingcloud.com/docs/install) and follow the steps shown
[here]() to begin.
TODO: Insert CLI command link above

## Rising Cloud Web Serivice Overview
See [here](https://risingcloud.com/docs/technicals) for useful information
regarding Rising Cloud Web Services. Another useful page for understanding
web services is located [here](https://risingcloud.com/docs/web-service)

## Using this Boilerplate Repository

### Requirements
- Python 3.5+
- Docker (To assist with local building and testing)
- Support for `make` commands (To assist with local building and testing)

### Local Testing and Development

There are two ways to test your application locally. You could just run your
application from `app.py` locally and run tests by also running the
`appTests.py` locally and having them comunicate in your host machine.
request.json in the root folder and run `python3 main.py`. If you are unable
to utilize docker for any reason, this is how you will need to test. However,
it is a much prefered paradigm to test in a docker container. By running
in a container, you ensure that your testing is consistent with deployment. The
provided makefile gives simple bindings necessary to create the image, run the
container, and test requests.

To get the local docker container up and running for testing and development:
TODO: Figure out how to do this first pointautomatically for people. Or at
least to transparently show them how/why this needs to be done.
https://docs.docker.com/config/daemon/ipv6/
1. Customize the docker daemon to allow for ipv6 traffic in your test
container as Rising Cloud workers only support ipv6 traffic. In order to do
this, ...
```json
{
    ...
    "experimental": true,
    "ipv6": true,
    "fixed-cidr-v6": "2001:db8:1::/64",
    "ip6tables": true
}
```
TODO: Finish this thing. Show example for docker desktop (easy) or show the
location of the file for mac, linux, and windows distributions.
1. Run the build make command: `make rc-build-test-image`. This will run a
docker build command that creates your base image and names it
bp-python-flask-service.
1. Start up the test container: `make rc-start-container`. This spins
up the image that was just built and keeps it running in the background. It
will automatically delete any old running containers of the same name for you.
It will also attach a volume to the container so that you can easily test
changes to your code without requiring a docker build every time.
1. Populate any test request files you'd like to be able to test in the
`/rcTests/reqeusts` folder. As long as they are named in the format
`{TEST_NAME}.json`, are proper json, and conform to the below object
specifications, they will work fine!
```json
{
    "url" [required]: The api endpoint to test against
    "params" [optional]: Normal url params which will be formated
        by python's requests package
    "method" [required]: ["GET" || "POST" || "PUT" || "PATCH" || "DELETE"]
    "headers" [optional]: These are passed into the request as headers
    "payload" [optional]: The raw data passed into the request
}
```
1. To run a single request test through: `make rc-test-single f={TEST_NAME}`.
This will load the specified request and then send it to the deployed container.
The response will be located at `./rcTests/responses/{TEST_NAME}` For this
command to work, the file `/rcTests/requests/{TEST_NAME}.json` must exist.
1. To run every test in the `/rcTests/requests/` folder in sequence:
`make rc-test-all`.This will essentially run the `rc-test-single` over
and over for every test file defined.
1. Whenever you're done testing, you can clean up the docker environment with
`rc-kill-container`.

### Building/Deploying
Once you have locally tested your app and verified it's functioning as expected,
you may simply run `risingcloud build` (without the `--local` flag). This will
queue a build of your application on the Rising Cloud build servers. You can
monitor the build progress via the link output from the command, or just
navigate to the "Build Status" page of the application you are building.
https://my.risingcloud.com/task/bp-python-flask-service/build-status

### Using the App
When the application is built, how do you use it? First, you can navigate to
https://my.risingcloud.com/task/bp-python-flask-service/ and ensure the app is deployed
by pressing the "Deploy" button on the top right of the page. After the task has
succesfully been started you can send jobs to your worker from anywhere.
Rising Cloud automatically registers a url for you so you can communicate with
your task. The URL for this task is https://bp-python-flask-service.risingcloud.app.

### Adding Custom Functionality
This repository is boilerplate for a reason. Please add, edit, and customize
code to your liking for whatever your use case may be. Some code comments were
left in the places where most applications are most likely to add or modify
the boilerplate.