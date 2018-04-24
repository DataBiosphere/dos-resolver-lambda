from chalice import Chalice
import requests

app = Chalice(app_name='dos-resolver')
app.debug = True

@app.route('/')
def index():
    return {'hello': 'world'}

base_path = '/ga4gh/dos/v1'

server_list = [
    "https://5ybh0f5iai.execute-api.us-west-2.amazonaws.com/api/ga4gh/dos/v1",
    "https://spbnq0bc10.execute-api.us-west-2.amazonaws.com/api/ga4gh/dos/v1",
    "https://gmyakqsfp8.execute-api.us-west-2.amazonaws.com/api/ga4gh/dos/v1",
    "https://mkc9oddwq0.execute-api.us-west-2.amazonaws.com/api/ga4gh/dos/v1"
]


@app.route("{}/dataobjects/{}".format(base_path, "{data_object_id}"),
           methods=['GET'], cors=True)
def get_data_object(data_object_id):
    """
    Attempts a GetDataObject request against each of the listed
    servers and returns the first result.
    :param data_object_id:
    :return:
    """
    data_objects = []
    found_server = None
    for server in server_list:
        response = requests.get("{}/dataobjects/{}".format(server, data_object_id))
        if response.status_code == 200:
            data_objects.append(response.json()['data_object'])
            found_server = server
            break


    # Modify the Data Object to include provenance about the
    # server we got metadata from.

    dos_url = "{}/dataobjects/{}".format(
        found_server, data_object_id)

    data_object = data_objects[0]
    data_object['urls'].append({'url': dos_url})

    return {'data_object': data_object}
