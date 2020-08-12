# -*- coding: utf-8 -*-
from __future__ import division, absolute_import, print_function, unicode_literals

from nextgisweb.webmap.plugin import WebmapPlugin


@WebmapPlugin.registry.register
class BasemapPlugin(WebmapPlugin):

    @classmethod
    def is_supported(cls, webmap):
        # TODO: Security
        basemaps = [dict(
            url=bm.resource.url,
            qms=bm.resource.qms,
            **bm.to_dict())
            for bm in webmap.basemaps]
        return (
            "ngw-basemap/plugin/BaseMap",
            dict(
                basemaps=basemaps,
            )
        )
