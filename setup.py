from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gym_management/__init__.py
from gym_management import __version__ as version

setup(
	name="gym_management",
	version=version,
	description="Gym management software aims to streamline the day-to-day operations of a fitness center by offering features such as membership management, scheduling of classes, billing and payment handling, member check-in, staff management, and reporting.",
	author="Omar Habeeb",
	author_email="omarhabeeb242@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
