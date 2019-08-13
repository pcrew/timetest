#!/usr/bin/env python3

import connexion
import subprocess


def get_timedate():
    retv = subprocess.check_output(['timedatectl', 'status'])
    return retv


def get_timezone():
    retv = subprocess.check_output(['timedatectl', 'list-timezones'])
    return retv


def post_time(time):
    retv = subprocess.run(['timedatectl', 'set-time', time],
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    return retv.stderr


def post_date(date):
    retv = subprocess.run(['timedatectl', 'set-time', date],
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    return retv.stderr


def post_zone(zone):
    retv = subprocess.run(['timedatectl', 'set-timezone', zone],
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    return retv.stderr


def post_ntp(ntp):
    retv = subprocess.run(['timedatectl', 'set-ntp', ntp],
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    return retv.stderr


if __name__ == '__main__':
    app = connexion.App(__name__, port=1771, specification_dir='openapi-3/')
    app.add_api('time.yaml')
    app.run()
