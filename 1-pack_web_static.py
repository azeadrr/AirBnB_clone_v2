#!/usr/bin/python3
"""Fabric script that generates a .tgz
archive from contents of the web_static"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """Compress before sending"""
    try:
        local("mkdir -p versions")
        res = local("tar -cvzf versions/web_static_{}.tgz web_static".format(datetime.now().strftime("%Y%m%d%H%M%s")),capture=True)
        return res
    except Exception:
        return None
