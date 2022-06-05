from csv import reader
from os import walk
import pygame
import logging
import pip
import pkg_resources
from termcolor import colored

# modules_to_install = [n"googletrans==4.0.0rc1", "csv", "os",
# 		"pygame", "logging", "pip", "pkg_resources", "termcolor", "sqlalchemy", "geocoder",
# 		"pytmx", "sys", "random", "json"]
modules_to_install = ["googletrans",
		"pygame", "logging", "pip", "termcolor", "sqlalchemy", "geocoder",
		"pytmx", "random"]


def import_csv_layout(path):
    """imports the csv-file's values of the map layers

    :param path: path to the csv file
    :type path: String
    :return: List of all the csv- file's values
    :rtype: String[]
    """

    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
    return terrain_map


def import_folder(path):
    """imports the content of a folder, especially made for images for pygame sprites

    :param path: path to the folder
    :type path: String
    :return: Surface list of all the sprites
    :rtype: pygame.image[]
    """
    surface_list = []   
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    # logging.debug("Created Surface- List: " + str(surface_list))
    return surface_list



def install(package):
    """installs the python package given in the parameter

    :param package: python package name
    :type package: String
    """
    print(hasattr(pip, 'main'))
    if hasattr(pip, 'main'):
        pip.main(['install', package])
        print('Installed ' + str(package))
    else:
        pip._internal.main(['install', package])


def test_modules_installed(package_list):
    """Tests if the python package is installed, when not, asks if it should be installed

    :param package_list: List of all python packages that should be tested
    :type package_list: String[]
    """
    print(colored('Testing if all neccessaryy packages are installed...', 'blue'))
    for package in package_list:
        try:
            dist = pkg_resources.get_distribution(package)
            print(colored('You have {} (v. {}) installed'
                .format(dist.key, dist.version), 'green'))
        except pkg_resources.DistributionNotFound:
            print(colored('{} is NOT installed'.format(package), 'red'))
            inp = input("Do you want to install {} (Y/n)? ".format(package))
            if inp == 'Y' or inp == 'y':
                print("Installing {}...".format(package))
                install(package)

    print("\n\n")
