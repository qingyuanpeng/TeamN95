import urllib.request
import json

def getDistance(origin, destination):
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    apiKey = 'AIzaSyDZ3NzuWjs0Q-MB8xB7h4EzaSOFlQvIThQ'
    origin = origin.replace(' ','+')
    destination = destination.replace(' ','+')
    navRequest = 'origin={}&destination={}&key={}'.format(origin,destination,apiKey)
    request = endpoint + navRequest
    response = urllib.request.urlopen(request).read()
    directions = json.loads(response)
    routes = directions['routes']
    if len(routes)<0:
        return "no valid route"
    legs = routes[0]['legs']
    distStr = legs[0]['distance']['text']
    return convertDist(distStr)

#convert string distance to double
def convertDist(distString):
    #replace all commas
    distString = distString.replace(",", "")
    #find index of space before unit
    index = distString.find(" ", 0, len(distString))
    
    return float(distString[:index])


def getCoord(addr):
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    apiKey = 'AIzaSyDZ3NzuWjs0Q-MB8xB7h4EzaSOFlQvIThQ'
    addr = addr.replace(' ','+')
    navRequest = 'origin={}&destination={}&key={}'.format(addr,addr,apiKey)
    request = endpoint + navRequest
    response = urllib.request.urlopen(request).read()
    directions = json.loads(response)
    routes = directions['routes']
    if len(routes)<0:
        return "no valid route"
    legs = routes[0]['legs']
    return [legs[0]['start_location']['lat'],legs[0]['start_location']['lng']]

def test3():
    origin = "3411 Chestnut St, PA"
    destination = "3401 Grays Ferry Ave, PA"
    destination2 = "New York"
    print(getDistance(origin, destination2))
    print(getCoord(origin))

#test3()



def getDistancePrompt():
    endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
    apiKey = 'AIzaSyDZ3NzuWjs0Q-MB8xB7h4EzaSOFlQvIThQ'
    origin = input("Where are you right now: ").replace(' ','+')
    destination = input("Where do you want to go: ").replace(' ','+')
    navRequest = 'origin={}&destination={}&key={}'.format(origin,destination,apiKey)
    request = endpoint + navRequest
    response = urllib.request.urlopen(request).read()
    directions = json.loads(response)
    routes = directions['routes']
    if len(routes)<0:
        return "no valid route"
    legs = routes[0]['legs']
    distStr = legs[0]['distance']['text']
    print(distStr)

getDistancePrompt()