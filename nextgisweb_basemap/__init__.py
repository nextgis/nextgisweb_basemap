# -*- coding: utf-8 -*-
from __future__ import division, absolute_import, print_function, unicode_literals

from nextgisweb.component import Component, require
from nextgisweb.lib.config import Option

from .model import Base
from .util import COMP_ID


class BasemapComponent(Component):
    identity = COMP_ID
    metadata = Base.metadata

    def initialize(self):
        from . import plugin

    @require('resource', 'webmap')
    def setup_pyramid(self, config):
        from . import view

    def client_settings(self, request):
        return dict(
            qms_geoservices_url=self.options['qms_geoservices_url'],
            qms_icons_url=self.options['qms_icons_url'])

    option_annotations = (
        Option('qms_geoservices_url', default='https://qms.nextgis.com/api/v1/geoservices/',
               doc="Geo Services QMS API URL"),
        Option('qms_icons_url', default='https://qms.nextgis.com/api/v1/icons/',
               doc="Icons QMS API URL"),
    )


def pkginfo():
    return dict(components=dict(
        basemap='nextgisweb_basemap'))


def amd_packages():
    return (
        ('ngw-basemap', 'nextgisweb_basemap:amd/ngw-basemap'),
    )
