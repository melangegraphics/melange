"""
melangeadmin commandline
"""

import cmdln
import os
import shutil
import sys

def startproject(projectname, template):
    if os.path.isdir(projectname):
        print("directory already exists, not overwritting.")
        return False

    template_path=os.path.join(os.path.dirname(__file__), "templates", template)
    if not os.path.isdir(template_path):
        print("cannot find template '%s'" % template)
    
    print("creating project %s using template %s" % (projectname, template))
    shutil.copytree(template_path, projectname)
    

class Admin(cmdln.Cmdln):
    name="melange"
    
    @cmdln.option("-t", "--template",                     # (1)
                    help="which project template to use?")
    def do_startproject(self, subcmd, opts, projectname=None):
        """${cmd_name}: create new melange project

        ${cmd_usage}                            # (1)
        ${cmd_option_list}
        """
        if not projectname:
            print('projectname not specified')
        else:
            startproject(projectname, opts.template or "default")

    @cmdln.option("-c", "--client",                     # (1)
                    help="which client to use?")
    def do_run(self, subcmd, opts, projectdir="."):
        """${cmd_name}: create new melange project

        ${cmd_usage}                            # (1)
        ${cmd_option_list}
        """
        from melange import client
        client.run(opts.client)
        #if not os.path.isfile(os.path.join(projectdir, "melange.cfg")):
        #    print("melange.cfg not found")
        #    pass

def main():
    try:
        admin = Admin()
    except Exception as e:
        print('oops')
        pass
    sys.exit(admin.main())

