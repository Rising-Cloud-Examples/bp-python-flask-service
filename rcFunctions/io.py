import json, typing
from constants import HOST, PORT

def readRequest(fileName: str) -> typing.Tuple[
    str, typing.Dict[str, str], str, typing.Dict[str, str] | None, typing.Any | None
]:
    '''
    readRequest is used during testing to read in example requests from the
    local rcTests folder. Each request should have a few headers defined so the
    test scripts can infer how to process them. Each request.json file in the
    rcTests/requests folder should have 5 attributes.
        "url" [required]: The api endpoint to test against
        "params" [optional]: Normal url params which will be formated
            by python's requests package
        "method" [required]: ["GET" || "POST" || "PUT" || "PATCH" || "DELETE"]
        "headers" [optional]: These are passed into the request as headers
        "payload" [optional]: The raw data passed into the request
    Each of these attributes are returned as a tuple in that order so that they
    maybe be utilized in the testing setup.
    '''

    with open(f"./rcTests/requests/{fileName}.json", "r") as f:
        request = json.load(f)

        # URL and METHOD are required for every request. Ensure they exist
        # and ensure METHOD is of a valid type.
        if "url" not in request:
            raise KeyError(f"no url provided for test requests {fileName}")
        if "method" not in request:
            raise KeyError(f"no method provided for test requests {fileName}")

        url = f'http://[{HOST}]:{PORT}/{request["url"]}'
        method = request["method"]

        validMethods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        if method not in validMethods:
            raise ValueError(f"request method '{method}' not a valid method")
        
        # Extract the params, headers, and payload if they exist. In general,
        # these are not required for all requests,
        # so we will not include checks here for that.
        params, headers, payload = None, None, None
        if "params" in request:
            params = request["params"]
        if "headers" in request:
            headers = request["headers"]
        if "payload" in request:
            payload = request["payload"]

        return url, params, method, headers, payload

def writeResponse(fileName: str, response: typing.Any):
    '''
    writeResponse converts an http response gathered during testing into a json
    object that is stored in the rcTests/responses folder. Additional validation
    scripts may be added if they are necessary for your development process.
    '''

    with open(f"./rcTests/responses/{fileName}.json", "w") as f:
        json.dump(response, f)
