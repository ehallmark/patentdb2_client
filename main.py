from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient())
patent_type = 'grant' # str |
number = '7654321' # str |
include_description = True # bool |  (optional) (default to true)
include_claims = True # bool |  (optional) (default to true)

try:
    # Returns patent information for a given patent grant, application, or publication.
    api_response = api_instance.find_by_patent_type_get(patent_type, number, include_description=include_description, include_claims=include_claims)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->find_by_patent_type_get: %s\n" % e)
