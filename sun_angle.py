def sun_angle(time):
    hours = int(time[:2]) + int(time[3:]) / 60
    if hours < 6 or hours > 18:
        return "I don't see the sun!"
    return (hours - 6) * 1.5 * 10

sun_angle("07:00") # 15
sun_angle("01:23") # "I don't see the sun!"
sun_angle("12:15") # 93.75