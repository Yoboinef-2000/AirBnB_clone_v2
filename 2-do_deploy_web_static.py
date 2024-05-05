#!/usr/bin/python3
"""
This Fabric script distributes an archive to web servers
"""

from fabric.api import run, put, env
import os

env.hosts = ['35.153.255.15', '100.27.4.210']
# env.user = '<username>'  # Update with actual username
# env.key_filename = '<path to SSH key>'  # Update with actual SSH key path


def do_deploy(archive_path):
    """
    Distributes the archive to web servers.
    :param archive_path: Path to the archive file
    :return: True if successful, False otherwise
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # put(archive_path, '/tmp/')

        # filename = os.path.basename(archive_path)
        # folder_name = filename.split('.')[0]
        # run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
        # run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
        #     .format(filename, folder_name))

        # run('rm /tmp/{}'.format(filename))

        # run('rm /data/web_static/current')

        # run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
        #     .format(folder_name))
        # return True
        filename = archive_path.split("/")[-1]
        foldername = filename.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, foldername))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filename, path, foldername))
        run('rm /tmp/{}'.format(filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, foldername))
        run('rm -rf {}{}/web_static'.format(path, foldername))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, foldername))
        return True
    except:
        return False
