from importlib import import_module
from warnings import warn

from nextgisweb.imptool import deprecate


def pkginfo():
    return dict(components=dict(basemap='nextgisweb_basemap.basemap'))


def __getattr__(name):
    ver = '1.7.0.dev1'
    cmp = 'basemap'
    pkg = f'nextgisweb_{cmp}'
    new = f'{pkg}.{cmp}'
    m = import_module(new)
    if hasattr(m, name):
        warn(
            f"Since {ver} {cmp} component has been moved to {new}. "
            f"Update import to {new}.{name}.", stacklevel=2)
        return getattr(m, name)

    raise AttributeError


deprecate(
    'nextgisweb_basemap.view', 'nextgisweb_basemap.basemap.view',
    since='1.7.0.dev1', remove='1.8.0.dev0')
