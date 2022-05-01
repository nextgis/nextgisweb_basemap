import io
from setuptools import setup, find_packages


with io.open('VERSION', 'r') as fd:
    VERSION = fd.read().rstrip()

requires = (
    'nextgisweb>=4.0.0.dev5',
)

entry_points = {
    'nextgisweb.packages': [
        'nextgisweb_basemap = nextgisweb_basemap:pkginfo',
    ],

    'nextgisweb.amd_packages': [
        'nextgisweb_basemap = nextgisweb_basemap:amd_packages',
    ],

}

setup(
    name='nextgisweb_basemap',
    version=VERSION,
    description='Basemap extension for NextGIS Web',
    author='NextGIS',
    author_email='info@nextgis.com',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8.*, <4",
    install_requires=requires,
    entry_points=entry_points,
)
