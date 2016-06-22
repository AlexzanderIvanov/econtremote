from __future__ import unicode_literals
import yaml

from remoteecont import RemoteEcontXml
from remoteecont.transfer import CurlTransfer


service_url = b'http://demo.econt.com/e-econt/xml_service_tool.php'
parcel_url = b'http://demo.econt.com/e-econt/xml_parcel_import.php'

econt = RemoteEcontXml(service_url, parcel_url,  # Remote API urls
                       'itpartner', 'itpartner',  # Username and password
                       CurlTransfer)

# print(econt.offices('София'))
# print(econt.cities_zones())

with open('result.yml', 'w', encoding="UTF-8") as yaml_file:
    yaml_file.write( yaml.dump(econt.cities({'city_name': '', 'report_type': 'short', 'id_zone': '1'}), default_flow_style=False))


# print(econt.cities({'city_name': '',
#                     'report_type': 'short'}))
