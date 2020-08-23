#Csci 1913 Project 1
#Elaine Lee
'''K-means functions'''

from image_utils import *


def initial_means(k):
    '''Returns a k length list of random colors'''
    return [random_color() for i in range(k)]


def distance(c1, c2):
    '''Distance between two colors'''
    return ((c1[0]-c2[0])**2+(c1[1]-c2[1])**2+(c1[2]-c2[2])**2)**0.5


def assign(image, means):
    '''Returns assignment list'''
    assignments = [[-1 for j in range(len(image[0]))] for i in range(len(image))]
    for i in range(len(image)):
        for j in range(len(image[0])):
            mini = 256
            dist = 0
            for k in range(len(means)):
                dist = distance(image[i][j], means[k])
                if dist < mini:
                    mini = dist
                    assignments[i][j] = k
    return assignments


def update_means(image, assignments, means, k):
    '''Updates means list to be the average of the colors assigned to each color'''
    colors = [[] for i in range(k)]
    for i in range(len(image)):
        for j in range(len(image[0])):
            colors[assignments[i][j]].append(image[i][j])
    for c in colors:
        r, g, b = 0, 0, 0
        num = len(c)
        for color in c:
            r += color[0]
            g += color[1]
            b += color[2]
        means[colors.index(c)] = (r//num, g//num, b//num) if num != 0 else random_color()
    return


def k_means(image, k):
    '''Full k means function: returns means list and assignments to reduce image to k colors'''
    means = initial_means(k)
    assignments1 = assign(image, means)
    update_means(image, assignments1, means, k)
    assignments2 = assign(image, means)
    while assignments1 != assignments2:
        assignments1, assignments2 = assignments2, assignments1
        update_means(image, assignments1, means, k)
        assignments2 = assign(image, means)
    return means, assignments2














