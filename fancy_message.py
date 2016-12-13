#!/usr/bin/env python3.5

########################################################################
#                                                                      #
# Copyright 2016 (c) Araluc Ltd.  All rights reserved.                 #
# For copying and use see:                                             #
#  https://github.com/dlinten/pytools/blob/master/LICENSE              #
#                                                                      #
# Company     : Araluc Ltd.                                            #
# Web site    : araluc.com                                             #
# Email       : info@araluc.com                                        #
# Author      : David Linten                                           #
# Date        : 2016-11-09 12:22:43.653640                             #
#                                                                      #
# Name        : fancy_message                                          #
# Description : Prints our coloured fancy messages to the console      #
#                                                                      #
########################################################################


class Colour:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Message:
    @staticmethod
    def header(message: str, ending='\n'):
        print('{}{}{}'.format(Colour.HEADER, message, Colour.ENDC), end=ending)

    @staticmethod
    def info(message: str, ending='\n'):
        print('{}{}{}'.format(Colour.OKGREEN, message, Colour.ENDC), end=ending)

    @staticmethod
    def warn(message: str, ending='\n'):
        print('{}{}{}'.format(Colour.WARNING, message, Colour.ENDC), end=ending)

    @staticmethod
    def error(message: str, ending='\n'):
        print('{}{}{}'.format(Colour.FAIL, message, Colour.ENDC), end=ending)

    @staticmethod
    def output(message: str, ending='\n'):
        print(message, end=ending)
