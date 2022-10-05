#!/Users/christophermattar/.pyenv/shims/python

import os
import shutil

if os.path.exists('build/Christopher'):
    shutil.rmtree('build/Christopher')
shutil.copytree('_site', 'build/Christopher')
