#!/usr/bin/python3
"""Fabric script that distributes
an archive to your web servers"""

from fabric.contrib import files
from fabric.api import env, put, run
import os

env.hosts = ['54.144.128.184', '100.25.159.254']


def do_deploy(archive_path):
    """deployment function"""
    if not os.path.exists(archive_path):
        return False

    data_path = '/data/web_static/releases/'
    tmp = archive_path.split('.')[0]
    name = tmp.split('/')[1]
    dest = data_path + name

    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(dest))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(name, dest))
        run('rm -f /tmp/{}.tgz'.format(name))
        run('mv {}/web_static/* {}/'.format(dest, dest))
        run('rm -rf {}/web_static'.format(dest))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(dest))
        return True
    except Exception:
        return False
