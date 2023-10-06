#!/usr/bin/python3
"""Fabric script that generates a .tgz
archive from contents of the web_static"""

from datetime import datetime
from fabric.api import local
from os import path
def do_pack():
    """function to generate the archive"""
    try:
        local("mkdir -p versions")
        neq = local("tar -cvzf versions/web_static_{}.tgz web_static"
                    .format(datetime.now().strftime("%Y%m%d%H%M%s")),
                    capture=True)
        return neq
    except Exception:
        return None
