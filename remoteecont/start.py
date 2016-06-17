from __future__ import unicode_literals

from remoteecont import RemoteEcontXml
from remoteecont.transfer import CurlTransfer

service_url = b'http://demo.econt.com/e-econt/xml_service_tool.php'
parcel_url = b'http://demo.econt.com/e-econt/xml_parcel_import.php'

econt = RemoteEcontXml(service_url, parcel_url,  # Remote API urls
                       'itpartner', 'itpartner', # Username and password
                       CurlTransfer)

print(econt.offices('София'))
print(econt.cities_regions())