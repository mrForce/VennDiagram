import numpy as np
import itertools
from scipy.optimize import minimize
import math
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def __add__(self, other_point):
        return Point2D(self.x + other_point.x, self.y + other_point.y)
    def __radd__(self, other_point):
        return Point2D(self.x + other_point.x, self.y + other_point.y)
    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    def __mul__(self, other):
        return Point2D(self.x*other, self.y*other)
    def __rmul__(self, other):
        return Point2D(self.x*other, self.y*other)
    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        
"""
a = Point2D(1, 2)
b = Point2D(3, 4)
print(a + b)
print(a - b)
print(a*3)
exit()
"""
class Circle:
    def __init__(self, radius, center_point):
        self.radius = radius
        self.center_point = center_point

    def get_radius(self):
        return self.radius
    def get_center_point(self):
        return self.center_point
    def contains_point(self, point):
        dist = self.center_point.distance(point)
        if dist <= self.get_radius():
            return True
        else:
            return False
    @staticmethod
    def intersection_area(circles):
        #give it a list of at least two circles
        #returns False if they do not overlap
        contained_intersecting_points = []
        for circle_one, circle_two in itertools.product(circles, circles):
            if circle_one != circle_two:
                intersection_points = circle_intersection_points(circle_one, circle_two)
                
                if len(intersection_points) < 2:
                    return False
                else:
                    point_one = intersection_points[0]
                    point_two = intersection_points[1]
                    if all([circle.contains_point(point_one) or circle == circle_one or circle == circle_two for circle in circles]):
                        contained_intersecting_points.append(point_one)
                    if all([circle.contains_point(point_two) or circle == circle_one or circle == circle_two for circle in circles]):
                        contained_intersecting_points.append(point_two)
        """
        Then, sort the points in contained_intersection_points by their angle with the centroid of the polygon formed by them. 
        """

def circle_intersection_points(circle_one, circle_two):
    #returns a list: empty if the circles don't overlap (or one is contained in the other), one if two circles touch at a single point, and two if there are two intersection points
    center_distance =   circle_one.get_center_point().distance(circle_two.get_center_point())
    if center_distance > circle_one.get_radius() + circle_two.get_radius() or center_distance < abs(circle_one.get_radius() - circle_two.get_radius()) or (center_distance < 1e-10 and abs(circle_one.radius - circle_two.radius) < 1e-10):
        return []
    #I'm awful at geometry, so I found this solution for getting the intersection points online: https://stackoverflow.com/questions/3349125/circle-circle-intersection-points#
    a = (circle_one.get_radius()**2 - circle_two.get_radius()**2 + center_distance**2)*1.0/(2*center_distance)
    h = circle_one.get_radius()**2 - a**2
    point_two = circle_one.get_center_point() + 1.0*a*(circle_two.get_center_point() - circle_one.get_center_point)/center_distance
    if h == 0:
        return [point_two]
    else:
        center_one = circle_one.get_center_point()
        center_two = circle_two.get_center_point()
        x_three_add = h*(center_two.y - center_one.y)/center_distance
        y_three_add = h*(center_two.x - center_one.x)/center_distance
        return [Point2D(point_two.x + x_three_add, point_two.y - y_three_add), Point2D(point_two.x - x_three_add, point_two.y + y_three_add)]



