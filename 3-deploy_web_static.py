#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers
"""

from fabric.api import env
from fabric.operations import local, put, run
from datetime import datetime
import os

env.hosts = ['35.153.255.15', '100.27.4.210']
# env.user = '<username>'  # Update with actual username
# env.key_filename = '<path to SSH key>'  # Update with actual SSH key path


def do_pack():
    """Compress the web_static folder into a .tgz archive."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    the_tgz_archive = "web_static_" + timestamp + ".tgz"
    result = local("tar -cvzf versions/{} web_static".format(the_tgz_archive))
    if result.return_code == 0:
        return os.path.abspath("versions/{}".format(the_tgz_archive))
    else:
        return None


def do_deploy(archive_path):
    """
    Distributes the archive to web servers.
    :param archive_path: Path to the archive file
    :return: True if successful, False otherwise
    """
    if not os.path.exists(archive_path):
        return False

    try:
        filename = os.path.basename(archive_path)
        folder_name = filename.split('.')[0]
        path = "/data/web_static/releases/"

        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, folder_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filename, path, folder_name))
        run('rm /tmp/{}'.format(filename))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, folder_name))

        return True
    except Exception as e:
        print(e)
        return False


def deploy():
    """Create and distribute an archive to web servers."""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


# #!/usr/bin/python3

# """
# This Fabric script (based on the file 2-do_deploy_web_static.py)
# creates and distributes an archive to web servers, using the
# function deploy
# """

# from datetime import datetime
# from fabric.api import local, run, put, env
# import os

# env.hosts = ['35.153.255.15', '100.27.4.210']
# # env.user = '<username>'  # Update with actual username
# # env.key_filename = '<path to SSH key>'  # Update with actual SSH key path

# def do_pack():
#     """Compress the web_static folder into a .tgz archive."""
#     timeStamp = datetime.now().strftime("%Y%m%d%H%M%S")
#     if not os.path.isdir("versions"):
#         os.mkdir("versions")
#     theTGZarchive = "web_static_" + timeStamp + ".tgz"
#     result = local("tar -cvzf versions/{} web_static".format(theTGZarchive))
#     if result.return_code == 0:
#         return os.path.abspath("versions/{}".format(theTGZarchive))
#     else:
#         return None

# def do_deploy(archive_path):
#     """
#     Distributes the archive to web servers.
#     :param archive_path: Path to the archive file
#     :return: True if successful, False otherwise
#     """
#     if not os.path.exists(archive_path):
#         return False

#     try:
#         # put(archive_path, '/tmp/')

#         # filename = os.path.basename(archive_path)
#         # folder_name = filename.split('.')[0]
#         # run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))
#         # run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
#         #     .format(filename, folder_name))

#         # run('rm /tmp/{}'.format(filename))

#         # run('rm /data/web_static/current')

#         # run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
#         #     .format(folder_name))
#         # return True
#         filename = archive_path.split("/")[-1]
#         foldername = filename.split(".")[0]
#         path = "/data/web_static/releases/"
#         put(archive_path, '/tmp/')
#         run('mkdir -p {}{}/'.format(path, foldername))
#         run('tar -xzf /tmp/{} -C {}{}/'.format(filename, path, foldername))
#         run('rm /tmp/{}'.format(filename))
#         run('mv {0}{1}/web_static/* {0}{1}/'.format(path, foldername))
#         run('rm -rf {}{}/web_static'.format(path, foldername))
#         run('rm -rf /data/web_static/current')
#         run('ln -s {}{}/ /data/web_static/current'.format(path, foldername))
#         return True
#     except Exception as e:
#         return False

# def deploy():
#     """The deployer."""
#     archive_path = do_pack()
#     if archive_path is None:
#         return False
#     return do_deploy(archive_path)
