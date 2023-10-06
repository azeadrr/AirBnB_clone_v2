#!/usr/bin/python3
"""Fabric script that distributes"""
from fabric.contrib import files
from fabric.api import env, put, run
import os

env.hosts = ['54.234.81.198', '100.25.193.190']


def do_deploy(archive_path):
    """Deploy archive!"""
    if not os.path.exists(archive_path):
        return False

    dt_path = '/data/web_static/releases/'
    tmp = archive_path.split('.')[0]
    nm = tmp.split('/')[1]
    dst = dt_path + nm

    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(dst))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(nm, dst))
        run('rm -f /tmp/{}.tgz'.format(nm))
        run('mv {}/web_static/* {}/'.format(dst, dst))
        run('rm -rf {}/web_static'.format(dst))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(dst))
        return True
    except Exception:
        return False
