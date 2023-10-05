import os, sys
import requests

from rcFunctions import readRequest, writeResponse

def testRequest(fileName: str):
    '''
    testRequest tests an indiviual request file in rcTests/requests. It will
    write the output from the service in the rcTests/responses folder.
    '''

    url, params, method, headers, payload = readRequest(fileName)

    # Make a call to the requested url with the appropriate method defined.
    # Populate function parameters according to the request. Python's requests
    # package will correctly interpret the None values
    response = requests.request(
        method,
        url,
        params=params,
        headers=headers,
        json=payload
    )

    responseData = response.text
    try: responseData = response.json()
    except: pass

    # Write the response to be viewed and/or validated later
    writeResponse(fileName, responseData)

if __name__ == "__main__":

    # If only param is passed in, we assume we are running over every test file.
    if len(sys.argv) == 1:
        for fileName in os.listdir("./rcTests/requests"):

            # The only files which are valid to run are .json files. And in
            # order to run testRequest(), we just need the name without the
            # file extension
            splitFile = fileName.split(".")
            if len(splitFile) != 2:
                raise Warning(f"File rcTests/requests/{fileName} has no extension")
            if "json" != splitFile[1]: continue
            name = splitFile[0]

            # If here, we have a valid test so we will run it
            testRequest(name)
    
    # Otherwise, we test the one file passed in and move on.
    else:
        testRequest(sys.argv[1])