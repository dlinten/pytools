#!/usr/bin/env python3

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
# Date        : 2016-12-05 16:20:27.475138                             #
#                                                                      #
# Name        : async_runner.py                                        #
# Description : Library to run commands in an asynchronous way.        #
#                                                                      #
########################################################################

import sys
import subprocess
import re

ARG_PATTERN = re.compile(r'(?:[^\s,"]|"(?:\\.|[^"])*")+')


class Execute:
    """Class for running commands on a system
    """

    @staticmethod
    def execute_async(cmd: str) -> str:
        """Executes a command asynchronously without returning command state on completion

        :param cmd: Command to run
        :returns str: Iterator to lines returned from stdout
        :raises CalledProcessError
        """
        args = list()
        for val in ARG_PATTERN.finditer(cmd):
            args.append(val.group().replace("\"", "").replace("\'", ""))

        popen = subprocess.Popen(args,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT,
                                 universal_newlines=True)
        lines = iter(popen.stdout.readline, "")

        for line in lines:
            yield line

        popen.stdout.close()

        return_code = popen.wait()

        if return_code != 0:
            raise subprocess.CalledProcessError(return_code, cmd.split(' '))

    @staticmethod
    def execute_with_info_async(cmd: str) -> str:
        """Executes a command asynchronously with returning command state on completion

        :param cmd: Command to run
        :returns str: Iterator to lines returned from stdout
        :raises CalledProcessError
        """
        try:
            for line in Execute.execute_async(cmd):
                yield line
        except KeyboardInterrupt:
            yield "Stopped!"
            sys.exit(0)
        except subprocess.CalledProcessError as err:
            yield "Failed!"
