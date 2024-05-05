#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives
"""

from fabric.api import env, run, cd
from datetime import datetime
import os

env.hosts = ['35.153.255.15', '100.27.4.210']
# env.user = '<username>'  # Update with actual username
# env.key_filename = '<path to SSH key>'  # Update with actual SSH key path

def do_clean(number=0):
    """Delete out-of-date archives."""
    try:
        number = int(number)
    except ValueError:
        return False

    if number < 0:
        return False

    number += 1  # Include the most recent version
    with cd('/data/web_static/releases'):
        run('ls -1t | tail -n +{} | xargs -I {{}} rm -rf {{}}'.format(number))

    with cd('versions'):
        run('ls -1t | tail -n +{} | xargs -I {{}} rm -rf {{}}'.format(number))

    return True
