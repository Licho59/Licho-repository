#! python3
# 'traffic_lights.py' - program to switch traffic lights at the crossroads
# assertion in line 17 finds the risk of collision because both direction are open for cars

# variables below mean 2 separate crossroads of different streets
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
            
for i in range(3):
    switchLights(market_2nd)
    print(market_2nd)
