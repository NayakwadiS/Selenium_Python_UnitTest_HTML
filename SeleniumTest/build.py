from pybuilder.core import use_plugin, init

# These are the plugins we want to use in our project.
# Projects provide tasks which are blocks of logic executed by PyBuilder.

use_plugin("python.core")
# the python unittest plugin allows running python's standard library unittests
use_plugin("python.unittest")
# this plugin allows installing project dependencies with pip
use_plugin("python.install_dependencies")
use_plugin("python.PyCharm")


# The project name
name = "SeleniumTest"
default_task = "publish"


# This is an initializer, a block of logic that runs before the project is built.
@init
def set_properties(project):
    # Nothing happens here yet, but notice the `project` argument which is automatically injected.
    project.build_depends_on('TestRunner.py')
    project.version = "0.1.14"
    project.set_property('unittest_module_glob', '*_unittest')
