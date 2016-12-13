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
# Date        : 2016-12-05 16:20:27.475138                             #
#                                                                      #
# Name        : git_tools.py                                           #
# Description : Library with various git commands.                     #
#                                                                      #
########################################################################

import re
from subprocess import CalledProcessError
from pytools.async_runner import Execute

git_short_ref = re.compile('^[0-9a-f]{7}$')


class InvalidGitRepoException(Exception):
    def __init__(self, message, errors):
        super(InvalidGitRepoException, self).__init__(message)
        self.errors = errors


def local_commit_ref(repo_path: str) -> str:
    """Gets the local commit ref HEAD for a given repository file location

    :param repo_path: Repository path location
    :return str: Ref HEAD value in short notation
    :raises CalledProcessError: If there is an invalid repository path
    """
    try:
        for line in Execute.execute_async('git --git-dir={repo_path}/.git rev-parse --short --verify HEAD'.
                                          format(repo_path=repo_path)):
            if git_short_ref.match(line):
                return line.strip('\n')
            else:
                raise CalledProcessError(returncode=128, cmd=line)
    except CalledProcessError as ex:
        raise InvalidGitRepoException('Invalid GIT repo at {path}'.format(path=repo_path), ex)


def is_path_a_repo(repo_path: str) -> bool:
    """Checks if a given path is a GIT Repository
    :param repo_path: Repository path location
    :return bool: True or False
    """
    try:
        return local_commit_ref(repo_path) is not None
    except InvalidGitRepoException:
        return False

