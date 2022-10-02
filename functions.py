from pyowm import OWM

def weather(city):
    owm = OWM('dbf1c716cecbf43263218e4e0505968c') 
    # owm = OWM('a15943b9de17ee15503fca01e6762916')
       
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    t = w.temperature('celsius')['temp']
    w = w.wind()['speed'] 
    # p = w.pressure['press']
    # cl = w.clouds
    # dt = w.detailed_status

    return (f'В городе {city} сейчас {round(t)} C, cкорость ветра: {w} м/с.')