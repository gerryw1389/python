#!/usr/bin/python3

################################################################
# Name: Backup Plex
# Copyright: Gerry Williams (https://automationadmin.com)
# License: MIT License (https://opensource.org/licenses/mit)
# Script Modified from: n/a
# Last Update: 2020-05-24 
# Description: Backups my Plex Media Server database to /mnt/vids/linux/plex/backup using rsync
################################################################

import logging
import logging.handlers
import sys
from datetime import datetime
import re
import shutil
import subprocess

# require Python interpreter > v.3.5
assert sys.version_info >= (3, 5)


def main():

    # set user functions
    date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    log = "/home/gerry/scripts/logs/plexbackup_" + date + ".log"

    # build rsync command
    options = "-zavh --exclude='Cache' --exclude='Crash Reports' --exclude='Logs' --exclude='Plug-in Support'"
    source = '/var/lib/plexmediaserver/Library/Application\ Support/Plex\ Media\ Server/'
    destination = '/mnt/vids/linux/plex/backup'
    seq = "rsync" + ' ' + options + ' ' + source + ' ' + destination

    logger = logging.getLogger("")
    logger.setLevel(logging.DEBUG)
    handler = logging.handlers.RotatingFileHandler(
        log, maxBytes=(1048576*5), backupCount=7
    )
    formatter = logging.Formatter(
        "%(asctime)s => %(levelname)s : %(message)s", datefmt='%Y-%m-%d %I:%M:%S %p')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

    if sys.platform == 'win32':
        logging.error("This script is incompatible with the Windows native"
                      "environment.\nIt should be run under a Unix-like"
                      "environment such as Linux or Cygwin.\n.")
        exit(1)

    # exit with error if rsync not found
    if not shutil.which('rsync'):
        logging.error("rsync executable not found in PATH\n")
        exit(1)

    logging.info('==========================')
    logging.info('Starting function...')
    logging.info('Logfile fullname: %s', log)

    logging.info('Stopping Plex Media Server')
    logging.info('--------------------------')
    stop = 'systemctl stop plexmediaserver.service'
    logging.info('Running: %s', stop)
    stop_process = subprocess.run(stop, shell=True, stdout=subprocess.PIPE)
    logging.info(stop_process)

    logging.info('Starting Backup')
    logging.info('--------------------------')
    logging.info('Running: %s', seq)
    #seq_process = subprocess.run(seq, shell=True, stdout=subprocess.PIPE)
    # logging.info(seq_process)

    logging.info('Starting Plex Media Server')
    logging.info('--------------------------')
    start = 'systemctl start plexmediaserver.service'
    logging.info('Running: %s', start)
    start_process = subprocess.run(start, shell=True, stdout=subprocess.PIPE)
    logging.info(start_process)

    logging.info('Backup Complete')
    logging.info('==========================')


if __name__ == "__main__":
    main()
