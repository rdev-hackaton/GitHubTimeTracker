from setuptools import setup, find_packages

name = 'ghtt'
install_requires = [
    'click==5.1',
    'PyGithub==1.26.0',
]
console_scripts = [
    'ghtt = time_tracker.frontends.cli.tracker:print_time_tracking_info',
]

if __name__ == '__main__':
    setup(
        name=name,
        install_requires=install_requires,
        version='0.0.1',
        packages=find_packages(exclude=['hooks', 'tests']),
        include_package_data=True,
        package_data={
            'time_tracker': ['*.json']
        },
        entry_points={
            'console_scripts': console_scripts
        }
    )
