# dos-resolver-lambda

This microservice provides a minimalistic implementation of the Data Object
Service to provide access resources in multiple DOS implementations.

It works by routing requests to a list of registered servers and returning
the Data Object that matches the request.


## Usage

To use this service, simply make a `GetDataObject` request as you would
against any other Data Object Service.

`curl https://0eofs5xr08.execute-api.us-west-2.amazonaws.com/api/ga4gh/dos/v1/dataobjects/a7ad1195-0ca2-4af1-9bdb-0c90515e5155`

The request will be made against a number of DOS instances to provide
a response, from the Team Calcium development DSS.

A similar request can be made against an identifier that is made available
by the NCI GDC:

`curl https://0eofs5xr08.execute-api.us-west-2.amazonaws.com/api/ga4gh/dos/v1/dataobjects/23fa7b4b-9d68-429b-aece-658b11124bb3`

In this case, the request was routed to another lambda, which translated
the request from NCI GDC into the DOS schemas.

For more, check out the [example-usage notebook](example-usage.ipynb)!

## Development

This is Open Source software, please offer a PR or feature request in the issues!

* Make server list configurable
* Data Bundles
* More documentation


