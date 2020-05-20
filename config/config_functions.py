################################################################################
#    HPCC SYSTEMS software Copyright (C) 2019 HPCC Systems.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
################################################################################

import os


def getauthfile(authfile='../conf/.radssh_auth'):
    return os.path.abspath(authfile)


def gethosts(hostfile='../conf/hostfile'):
    full_hostfile = os.path.abspath(hostfile)
    with open(full_hostfile) as f:
        list_of_hosts = [s.rstrip() for s in f.readlines()]
    return list_of_hosts


def connections(hosts):
    connection_set = [(x, None) for x in hosts]
    return connection_set

