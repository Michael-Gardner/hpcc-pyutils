#    HPCC SYSTEMS software Copyright (C) 2020 HPCC Systems.
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

import time
import os
import glob
import logging


class Cleanup:
    """
    cleanup object

    """

    def __init__(self, directory, days=30, suffix="log"):
        searchpath = "%s/**/*%s" % (directory, suffix)
        files = glob.glob(searchpath, recursive=True)
        self.oldfiles = []
        # convert days to seconds for later time conversions
        current_time = time.time()
        past_time = current_time - ( days * 86400 )
        for f in files:
            if os.stat(f).st_mtime < past_time:
                self.oldfiles.append(f)

    def delete(self):
        for f in self.oldfiles:
            if os.path.isfile(f):
                logging.info("deleting: %s", f)
                os.remove(f)

    def list(self):
        for f in self.oldfiles:
            logging.info("oldfiles: %s", f)
            print("%s", f)

if __name__ == '__main__':
    logging.basicConfig(filename='cleanup.log',level=logging.INFO)

    mycleanup = Cleanup('/var/log/HPCCSystems')
    mycleanup.list()
