from setuptools import setup, find_packages

__pkg_name__ = 'frame2seq'

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

print(requirements)

setup(name=__pkg_name__,
      version='0.0.5',
      packages=find_packages(),
      install_requires=requirements,
      zip_safe = False,
      entry_points = {
        'console_scripts': [
            '{0} = {0}:main'.format(__pkg_name__)
        ]
      },
    )