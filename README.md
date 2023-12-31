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
request.json in the root folder and run `python3 app.py`. If you are unable
to utilize docker for any reason, this is how you will need to test. However,
it is a much prefered paradigm to test in a docker container. By running
in a container, you ensure that your testing is consistent with deployment. The
provided makefile gives simple bindings necessary to create the image, run the
container, and test requests.

To get the local docker container up and running for testing and development:
1. Run the local build command: `risingcloud build --local`. This will run a
docker build command that creates your base image and names it
bp-python-flask-service.
1. Start up the test container: `risingcloud run -s`. This spins up the image
that was just built and keeps it running in the background. It will
automatically delete any old running containers of the same name for
you. It will also attach a volume to the container so that you can easily test
changes to your code without requiring a docker build every time.
1. Open up the `requestCollection.json` file in either Insomnia or Postman.
Modify the collection as you please, but this should give a good starting point
on how you can interact with your application locally and when it is deployed.
In Postman, the `{{host}}` and `{{auth}}` variables are set in the collection
variables. In Insomnia, they will be imported under the Environment Overrides.
1. Send requests via Postman or Insomnia to your local test container to
verify it is working as intended.
1. Whenever you're done testing, you can clean up the docker environment with
`risingcloud kill-local`.

For all the above commands, you can expedite testing and remove the prompt
"`No task URL provided. Use "bp-python-flask-service" as your task URL? [y/n]`"
by providing the command with the taskURL in question on the end of the command.
- ex. 1: `risingcloud build --local` -> `risingcloud build --local bp-python-flask-service`
- ex. 2: `risingcloud run -s` -> `risingcloud run -s bp-python-flask-service`
- ex. 3: `risingcloud kill-local` -> `risingcloud kill-local bp-python-flask-service`

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

### Securing your App
You can navigate to this page
https://my.risingcloud.com/task/bp-python-flask-service/security and check
"Require app users use an API key to send jobs to this task." to require a key
to be included when commnunicating with your app. The key should be included
as "X-RisingCloud-Auth" in the headers.

### Adding Custom Functionality
This repository is boilerplate for a reason. Please add, edit, and customize
code to your liking for whatever your use case may be. Some code comments were
left in the places where most applications are most likely to add or modify
the boilerplate.