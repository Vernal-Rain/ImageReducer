#Csci 1913 Project 1
#Elaine Lee
'''Run k-means on an image'''

from k_means import *


if __name__ == "__main__":
    file = input("Enter file name of an image: ")
    k = int(input("Enter number of colors to convert image to: "))
    save_file = input("Enter file name to save image: ")
    image = read_ppm(file)
    means, assignments = k_means(image, k)

    '''Creating new image...'''
    new_image = image.copy()
    for i in range(len(image)):
        for j in range(len(image[0])):
            new_image[i][j] = means[assignments[i][j]]
    save_ppm(save_file, new_image)
