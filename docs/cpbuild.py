#!/Users/christophermattar/.pyenv/shims/python

import os
import shutil

if os.path.exists('../BruinBots christopher-jekyll _site/Christopher'):
    shutil.rmtree('../BruinBots christopher-jekyll _site/Christopher')
shutil.copytree('_site', '../BruinBots christopher-jekyll _site/Christopher')
