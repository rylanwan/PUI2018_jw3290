import json
import sys
import csv


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

url_bus = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + mat_key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line
jsonData = get_jsonparsed_data(url_bus)


VMD = jsonData['Siri'][u'ServiceDelivery'][u'VehicleMonitoringDelivery'][0]

bus_num = len(VMD['VehicleActivity'])

file = open(sys.argv[3], 'w')
file.write('Latitude, Longtitude, Stop Name, Stop Status\n')

for x in range(bus_num):
        latitude = VMD['VehicleActivity'][x]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        longitude = VMD['VehicleActivity'][x]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        try:
            stop_name = VMD['VehicleActivity'][x]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        except: 
            stop_name = "N/A"
        try:
            stop_status = VMD['VehicleActivity'][x]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
        except:
            stop_status = ('N/A')
        file.write('%s, %s, %s, %s\n'%(latitude, longitude, stop_name, stop_status))