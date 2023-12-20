from LIDAR import env,sensors
import pygame
environment = env._build_environment((600, 1200))
environment.originalMap = environment.map.copy()
laser = sensors.LaserSensor(200, (0.5, 0.01), environment.originalMap)
environment.map.fill((0, 0, 0))
environment.infomap = environment.map.copy()
running = True

while running:
    sensor_on = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_focused():
        sensor_on = True
    elif not pygame.mouse.get_focused():
        sensor_on = False

    if sensor_on:
        position = pygame.mouse.get_pos()
        laser.position = position
        sensor_data = laser.sense_obstacles()
        environment.data_storage(sensor_data)
        environment.show_sensor_data()

    environment.map.blit(environment.infomap, (0, 0))
    pygame.display.update()



