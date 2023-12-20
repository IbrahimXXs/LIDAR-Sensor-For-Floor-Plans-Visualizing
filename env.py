# Import the math module
import math

# Import the pygame module
import pygame

# Define a class named _build_environment
class _build_environment:
    # Constructor method that initializes the object with MapDimensions
    def __init__(self, MapDimensions):
        # Initialize the pygame module
        pygame.init()

        # Create an empty list named pointcloud
        self.pointcloud = []

        # Load an external map image named 'map1.png'
        self.externalMap = pygame.image.load('map1.png')

        # Unpack MapDimensions into self.maph and self.mapw
        self.maph, self.mapw = MapDimensions

        # Set the window name for display
        self.MapwindowName = 'RRT path planning'

        # Set the window caption using the window name
        pygame.display.set_caption(self.MapwindowName)

        # Create a display surface with dimensions (self.mapw, self.maph)
        self.map = pygame.display.set_mode((self.mapw, self.maph))

        # Blit the externalMap onto the map surface at the position (0, 0)
        self.map.blit(self.externalMap, (0, 0))

        # Define color constants
        self.black = (0, 0, 0)
        self.grey = (70, 70, 70)
        self.blue = (0, 0, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)

    def AD2pos(self, distance, angle, robotPosition):
        x = distance * math.cos(angle) + robotPosition[0]
        y = -distance * math.sin(angle) + robotPosition[1]
        return (int(x), int(y))

    def data_storage(self, data):
        if data:
            print(len(self.pointcloud))
            for element in data:
                point = self.AD2pos(element[0], element[1], element[2])
                if point not in self.pointcloud:
                    self.pointcloud.append(point)
        else:
            print("No data received from sensor")

    def show_sensor_data(self):
        self.infomap = self.map.copy()
        for point in self.pointcloud:
            self.infomap.set_at((int(point[0]), int(point[1])), (255, 0, 0))

