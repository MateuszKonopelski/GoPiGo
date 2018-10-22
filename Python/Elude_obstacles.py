import easygopigo3 as easy
my_gopigo = easy.EasyGoPiGo3()
dist_sensor = my_gopigo.init_distance_sensor()
    
i = 1

while True:
    my_gopigo.forward()
    print('loop: {} '.format(i), dist_sensor.read())
    if dist_sensor.read() <= 10:
        my_gopigo.stop()
        my_gopigo.turn_degrees(45)
        dist_r = dist_sensor.read()
        my_gopigo.turn_degrees(-90)
        dist_l = dist_sensor.read()
        if dist_l < dist_r:
            my_gopigo.turn_degrees(90)
            
    if i == 50:
        my_gopigo.stop()
        break
    i = i+1
print('Ściana')
