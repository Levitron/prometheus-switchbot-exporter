from setuptools import setup

setup(
   name='prometheus_switchbot_exporter',
   version='0.1',
   description='An Prometheus exporter for Switchbots Meters',
   author='',
   author_email='',
   packages=['prometheus_switchbot_exporter'],  #same as name
   install_requires=['wheel', 'bluepy', 'click', 'prometheus-client'], #external packages as dependencies
)
