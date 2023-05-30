# xAPI is rhe API for collaboration endpoint software -> Cmds, configs, status, events

# URL = "https://<ip-address>/status.xml	# "GET" -> the complete status of the device

# URL = "https://<ip-address>/configuration.xml	# "GET" -> the configuration of the device

# URL = "https://<ip-address>/command.xml	# "GET" -> the complete set of cmds supported by the device

# URL = "https://<ip-address>/valuespace.xml	# "GET" -> value spaces used inthe system settings, status info, and CMDs

# URL = "https://<ip-address>/put.xml	# "PUT" -> Configure any setting on the device

# URL = "https://<ip-address>/xmlapi/session/begin.xml	# "GET" -> Start a session, get session cookie


# Get session cookie below:

import requests

URL = input('Enter the xAPI url: ')

HEADERS = {'Authorization', "Basic LJJGVJYHBMJN"}

RESPONSE = requests.request("POST", URL, headers=HEADERS)

print (RESPONSE.headers["Set-Cookie"])



# Get the current device status below:

import requests

URL = input('Enter the xAPI url: ')

HEADERS = {'Cookie', "SessionId=LJJGVJYHBMJN"}

RESPONSE = requests.request("GET", URL, headers=HEADERS)

print (RESPONSE.text)


# Setting device attributes below:

import requests

URL = input('Enter the xAPI url: ')

PAYLOAD = (
    '<Command>' + 
    '   <Camera>' +
    '       <PositionSet command="True">' +
    '       <CameraId>1</CameraId>' + 
    '       <Pan>150</PAN>' +
    '       <Tilt>150</Tilt>' + 
    '       </PositionSet>' +
    '   </Camera>' +
    '</Command>'
)

HEADERS = {'Content-Type': "application/xml", 'Cookie': "SessionId=JHBKJGCKJYVHHKJNK"}

RESPONSE = requests.request("POST", URL, data=PAYLOAD, headers=HEADERS)

print (RESPONSE.text)


# Registering an Event Notification Webhook below:


import requests

URL = input('Enter the xAPI url: ')

PAYLOAD = (
    '<Command>' + 
    '   <HttpFeedback>' +
    '       <Register command="True">' +
    '           <FeebackSlot>1</FeedbackSlot>' + 
    '           <ServerUrl>' + URL + '</ServerUrl>' +
    '           <Format>JSON</Format>' + 
    '           <Expression item="1">/Configuration</Expression>' + 
    '           <Expression item="2">/Event/CallDisconnect</Expression>' + 
    '           <Expression item="3">/Status/Call</Expression>' + 
    '       </Register>' + 
    '   </HttpFeedback>' +
    '</Command>' +
    '</Command>'
)

HEADERS = {'Content-Type': "application/xml", 'Cookie': "SessionId=JHBKJGCKJYVHHKJNK"}

RESPONSE = requests.request("POST", URL, data=PAYLOAD, headers=HEADERS)

print (RESPONSE.text)


# Set people presence detector status

import requests

URL = input('Enter the xAPI "PUT" url: ')

PAYLOAD = (
    '<Configuration>' + 
    '   <RoomAnalytics>' +
    '       <PeoplePresenceDetector>On</PeoplePresenceDetector>' +
    '   </RoomAnalytics>' + 
    '</Configuration>'
)

HEADERS = {'Content-Type': "application/xml", 'Cookie': "SessionId=JHBKJGCKJYVHHKJNK"}

RESPONSE = requests.request("POST", URL, data=PAYLOAD, headers=HEADERS)

print (RESPONSE.text)
