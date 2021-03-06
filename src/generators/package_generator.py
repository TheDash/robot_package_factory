#!/usr/bin/python
# Author: Devon Ash
# Contact: noobaca2@gmail.com
class PackageCredentials:

    package_author = "BuildIt ROS"
    package_maintainer = "BuildIt ROS"
    package_version = "1.0.0"
    package_name = "default"
    is_metapackage = False

    def __init__(self): pass

    def get_package_name(self):
        return self.package_name

    def get_package_maintainer(self):
        return self.package_maintainer

    def is_metapackage(self):
        return self.is_metapackage

    def get_package_version(self):
        return self.package_version

    def get_package_author(self):
        return self.package_author

    def set_package_name(self, name):
        self.package_name = name

    def set_package_maintainer(self, maintainer):
        self.package_maintainer = maintainer

    def set_package_version(self, version):
        self.package_version = version

    def set_package_author(self, author):
        self.package_author = author

    def set_is_metapackage(self, ifis):
        self.is_metapackage = ifis

class PackageGenerator:

    # A list of the dependencies the package will have.
    package_deps = []
    credentials = None

    IS_METAPACKAGE = False

    def __init__(self, credentials):
        print "Generating package %s" % package_name
        self.credentials = credentials

    def generate_cmakelists(self, dependencies):
        print "Generating cmakelists for %s" 
        return

    def generate_packagexml(self, dependencies, credentials):
        return

    def generate_readme(self):
        return
        
