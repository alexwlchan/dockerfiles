#!/usr/bin/env python3
# -*- encoding: utf-8

import logging
import os
import subprocess

import daiquiri
import requests

daiquiri.setup(level=logging.INFO)
logger = daiquiri.getLogger()

tasks = subprocess.check_output(['make', 'list']).decode('ascii').split()
publish_tasks = [t for t in tasks if t.endswith('-publish')]

logger.info('*** Logging in to Docker Hub')
subprocess.check_call([
    'docker', 'login',
    '--username', os.environ['DOCKER_USERNAME'],
    '--password', os.environ['DOCKER_PASSWORD']
])

# For each publish task, get the most recent version from Docker Hub
for p in publish_tasks:
    name = p.rsplit('-', 1)[0]
    logger.info('*** Starting checks for %s', name)
    resp = requests.get(
        f'https://registry.hub.docker.com/v2/repositories/greengloves/{name}/tags/'
    )
    resp.raise_for_status()

    subprocess.check_call(['make', f'{name}-build'])

    if os.environ.get('TRAVIS_EVENT_TYPE') == 'pull_request':
        logger.info('This is a Travis PR, skipping publish steps')
    else:
        versioned_images = [
            img
            for img in resp.json()['results']
            if img['name'] != 'latest'
        ]
        try:
            latest_image = max(versioned_images, key=lambda img: img['last_updated'])
            latest_version = latest_image['name'].strip()
        except ValueError:
            latest_version = '<none>'
        logger.info('Docker Hub  = %s', latest_version)

        local_version = subprocess.check_output(['make', f'{name}-version']).decode('ascii').strip()
        logger.info('Local build = %s', local_version)

        if latest_version == local_version:
            logger.info('Versions match, nothing to do!')
        else:
            logger.warning('Versions differ, rebuilding!')
            subprocess.check_call(['make', f'{name}-publish'])

    logger.info('*** Finished checks for %s', name)
