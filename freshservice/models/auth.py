import os, requests, json
from requests import Session
from freshservice.models.exceptions import FreshserviceResourceNotFound, FreshserviceBadRequest

class Auth:

    def __init__(self):

        # * Get the API key and domain
        api_key = os.environ['FRESHSERVICE_API_KEY']
        domain = os.environ['FRESHSERVICE_DOMAIN']

        # * Create a requests session
        self.session = Session()
        # * Create a url prefix
        self.url_prefix = f"https://{domain}/api/v2/"

        # * Authenticate the session
        self.session.auth = (api_key, '')

        # * Add the headers to the sessions
        self.session.headers.update(
            {
                'Content-Type': 'application/json',
                'Connection': 'close'
            }
        )
    
    def getx(self, url) -> dict:

        # * Make the API call
        response = self.session.get(self.url_prefix + url)

        # * Parse to response checker and return the outcome
        return self.__response_checker(response=response)

    def putx(self, url, data) -> dict:

        # * Make the API call
        response = self.session.put(self.url_prefix + url, data=json.dumps(data))

        # * Parse to response checker and return the outcome
        return self.__response_checker(response=response)

    def postx(self, url, data) -> dict:

        # * Make the API call
        response = self.session.post(self.url_prefix + url, data=json.dumps(data))

        # * Parse to response checker and return the outcome
        return self.__response_checker(response=response)

    def deletex(self, url) -> dict:

        # * Make the API call
        response = self.session.delete(self.url_prefix + url)

        # * Parse to response checker and return the outcome
        return self.__response_checker(response=response)

    def __response_checker(self, response: requests.models.Response) -> dict:

        # * Verify if the request was successful
        # TODO(Improve error handler)
        if response.status_code >= 200 and response.status_code <= 299:
            return response.json()
        elif response.status_code == 404:
            raise FreshserviceResourceNotFound(None)
        else:
            raise FreshserviceBadRequest(response.text)