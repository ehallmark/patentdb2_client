# swagger_client.DefaultApi

All URIs are relative to *https://ai.gttgrp.com/v1/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_by_patent_type_get**](DefaultApi.md#find_by_patent_type_get) | **GET** /find_by_{patent_type} | Returns patent information for a given patent grant, application, or publication.

# **find_by_patent_type_get**
> InlineResponse200 find_by_patent_type_get(patent_type, number, include_description=include_description, include_claims=include_claims)

Returns patent information for a given patent grant, application, or publication.

Eg. GET /find_by_grant?number=7654321 or GET /find_by_publication?number=20080156487

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
patent_type = 'patent_type_example' # str | 
number = 'number_example' # str | 
include_description = true # bool |  (optional) (default to true)
include_claims = true # bool |  (optional) (default to true)

try:
    # Returns patent information for a given patent grant, application, or publication.
    api_response = api_instance.find_by_patent_type_get(patent_type, number, include_description=include_description, include_claims=include_claims)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->find_by_patent_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patent_type** | **str**|  | 
 **number** | **str**|  | 
 **include_description** | **bool**|  | [optional] [default to true]
 **include_claims** | **bool**|  | [optional] [default to true]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

