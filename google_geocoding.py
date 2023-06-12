# install 
# pip install -U googlemaps

import googlemaps
import json 

#구글 api key 를 입력하세요. 
api_key = "[구글지도api키]"
gps_info = (37.54794204380073, 127.07460710236217)
lang = "ko"

gmaps = googlemaps.Client(api_key)
reverse_geocode_result = gmaps.reverse_geocode(gps_info, language=lang)
string = json.dumps(reverse_geocode_result)
result = json.loads(string)
#print(result) 
item = result[0]


address_components = item['address_components']
long_names = []
short_names = [] 
for address_component in address_components:
    long_name = address_component["long_name"]
    short_name = address_component["short_name"]
    long_names.append(long_name)
    short_names.append(short_name)

print(' '.join(long_names))
print(' '.join(short_names))

 

