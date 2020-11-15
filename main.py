from swagger_client.api.default_api import DefaultApi

default_api = DefaultApi()

response = default_api.find_by_patent_type_get("grant", "7654321")

print('Response: {}'.format(response))