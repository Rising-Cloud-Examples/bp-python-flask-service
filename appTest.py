import sys
import json
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

    print(responseData)

    # Write the response to be viewed and/or validated later
    writeResponse(fileName, responseData)

if __name__ == "__main__":
    testRequest(sys.argv[1])