from setuptools import setup

name = 'time_tracker'
install_requires = [
    'click==5.1',
    'PyGithub==1.26.0',
]

if __name__ == '__main__':
    setup(
        name=name,
        install_requires=install_requires,
    )
