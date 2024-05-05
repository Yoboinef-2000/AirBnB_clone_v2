#!/usr/bin/python3
"""
This is a Fabric Script generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the
function do_pack
"""

from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """Compress the web_static folder into a .tgz archive."""
    timeStamp = datetime.now().strftime("%Y%m%d%H%M%S")
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    theTGZarchive = "web_static_" + timeStamp + ".tgz"
    result = local("tar -cvzf versions/{} web_static".format(theTGZarchive))
    if result.return_code == 0:
        return os.path.abspath("versions/{}".format(theTGZarchive))
    else:
        return None
