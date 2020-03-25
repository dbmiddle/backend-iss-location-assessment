#!/usr/bin/env python

__author__ = 'dbmiddle'

import requests
import time
import turtle


def main():
    # part_A:
    res1 = requests.get('http://api.open-notify.org/astros.json')
    res_obj = res1.json()
    astros = res_obj['people']
    for obj in astros:
        print('{} is currently in space and onboard the {} spacecraft'.format(
            obj['name'], obj['craft']))
    print("There are {} total astronauts in space".format(len(astros)))

    # part_B:
    res2 = requests.get('http://api.open-notify.org/iss-now.json')
    res_obj = res2.json()
    print('On {}, the ISS was positioned at lat: {} lon: {}'.format(
        time.ctime(res_obj['timestamp']), res_obj['iss_position']['latitude'],
        res_obj['iss_position']['longitude']))

    # part_C:
    lat = res_obj['iss_position']['latitude']
    lon = res_obj['iss_position']['longitude']
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.register_shape('iss.gif')
    screen.bgpic('map.gif')
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.penup()
    iss.goto(float(lat), float(lon))

    # part_D:
    lat_indy = 39.7684
    lon_indy = -86.1581
    url = 'http://api.open-notify.org/iss-pass.json?lat=' + \
        str(lat_indy) + '&lon=' + str(lon_indy)
    res3 = requests.get(url)
    res_obj2 = res3.json()

    location = turtle.Turtle()
    location.penup()
    location.color('yellow')
    location.goto(float(lon_indy), float(lat_indy))
    location.dot(5)
    location.hideturtle()

    over_indy = res_obj2['response'][1]['risetime']
    location.write('Next time ISS over Indy will be: {}'.format(
        time.ctime(over_indy)))
    turtle.done()


if __name__ == '__main__':
    main()
