import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib


def get_jsonparsed_data(url):
    """
    from http://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urllib.urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


mat_key = sys.argv[1]
bus_line = sys.argv[2]

url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + mat_key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line
jsonData = get_jsonparsed_data(url)

VMD = jsonData['Siri'][u'ServiceDelivery'][u'VehicleMonitoringDelivery'][0]

bus_num = len(VMD['VehicleActivity'])

def location(bus_num):
    for x in range(bus_num):
        latitude = VMD['VehicleActivity'][x]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        longitude = VMD['VehicleActivity'][x]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print('Bus ' + str(x) + ' is at latitude ' + str(latitude) + ' and longitutde ' + str(longitude))

print('Bus Line: '+ bus_line)
print('Number of Active Buses: '+ str(bus_num))   
print(location(bus_num))