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

import subprocess
import tempfile
import sys


class Svn:
    """
    svn object

    repo_url : repository url that we want to access
    username : username you want the repo to use, system/ssh username is used for access to files
    password : password to go with username for repo use only
    path     : path to object in repo we want to work with
    """

    def __init__(self, repo_url, username='', password='', local=True):
        self.repo_url = repo_url
        self.username = username
        self.password = password
        self.local = local
        if not self.local:
            self.repo_url = repo_url
            self.tmpdir = tempfile.TemporaryDirectory()
            self.checkout(self.repo_url)
        else:
            self.repo_path = repo_url

    def __del__(self):
        self.cleanup()

    def cleanup(self):
        if not self.local:
            self.tmpdir.cleanup()

    def checkout(self, repo_url):
        if self.local:
            raise NameError('Local repositories cannot be checked out')
        checkout_call = ['svn', 'checkout', repo_url]
        if self.username:
            checkout_call.append('--username')
            checkout_call.append(self.username)
        if self.password:
            checkout_call.append('--password')
            checkout_call.append(self.password)
        subprocess.check_call(checkout_call, cwd=self.tmpdir.name)

    def propset(self, propname, propval, path):
        propset_call = ['svn', 'propset', propname, propval, path]
        if self.username:
            propset_call.append('--username')
            propset_call.append(self.username)
        if self.password:
            propset_call.append('--password')
            propset_call.append(self.password)
        if self.local:
            current_cwd = self.repo_path
        else:
            current_cwd = self.tmpdir.name
        subprocess.check_call(propset_call, cwd=current_cwd)

    def proplist(self, path):
        proplist_call = ['svn', 'proplist', '-v', path]
        if self.username:
            proplist_call.append('--username')
            proplist_call.append(self.username)
        if self.password:
            proplist_call.append('--password')
            proplist_call.append(self.password)
        if self.local:
            current_cwd = self.repo_path
        else:
            current_cwd = self.tmpdir.name
        subprocess.check_call(proplist_call, cwd=current_cwd)

    def commit(self, path, msg=''):
        commit_call = ['svn', '--non-interactive', 'commit', path, '--message', msg]
        if self.username:
            commit_call.append('--username')
            commit_call.append(self.username)
        if self.password:
            commit_call.append('--password')
            commit_call.append(self.password)
        if self.local:
            current_cwd = self.repo_path
        else:
            current_cwd = self.tmpdir.name
        subprocess.check_call(commit_call, cwd=current_cwd)

    def update(self):
        update_call = ['svn', '--non-interactive', 'update']
        if self.local:
            update_call.append(self.repo_path)
            current_cwd = self.repo_path
        else:
            current_cwd = self.tmpdir.name
            sp = subprocess.check_output(['ls'], cwd=self.tmpdir.name).decode(sys.stdout.encoding).strip()
            update_call.append(sp)
        if self.username:
            update_call.append('--username')
            update_call.append(self.username)
        if self.password:
            update_call.append('--password')
            update_call.append(self.password)
        subprocess.check_call(update_call, cwd=current_cwd)
