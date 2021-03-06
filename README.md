# swagger-client
API specification for PatentDB 2.0

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/ehallmark/patentdb2_client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ehallmark/patentdb2_client.git`)

Then import the package:
```python
import swagger_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
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
```

## Documentation for API Endpoints

All URIs are relative to *https://ai.gttgrp.com/v1/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**find_by_patent_type_get**](docs/DefaultApi.md#find_by_patent_type_get) | **GET** /find_by_{patent_type} | Returns patent information for a given patent grant, application, or publication.

## Documentation For Models

 - [InlineResponse200](docs/InlineResponse200.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author
