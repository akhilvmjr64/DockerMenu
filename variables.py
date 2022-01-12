#!/home/akhil/anaconda3/bin/python
import subprocess
from env import cgiRoute
if(__name__=="__main__"):
    print(f"Location: {cgiRoute}\n")
def style(f):
    # this function returns the styles from the given file
    styles=subprocess.getoutput("cat {0}".format(f))
    print("""
    <style>
        {0}
    </style>
    """.format(styles))
def values():
    f="style.css"
    print("""
    <head>
        <title>Docker Menu</title>
    </head>
    """)
    # following will give the contents of the styles file
    styles=subprocess.getoutput("cat {0}".format(f))
    style(f)
    # below set will store what are the different main menu
    menu_main={}
    # in our case we have 3 main menus local, remote, and AWS
    # below we are giving the names and routes to the sub menus
    menu_main['docker']={
                        "Start docker service":"dockerstart",
                        "Stop docker service":"dockerstop",
                        "List the available images":"listimages",
                        "List the running containers":"listcontainers",
                        "Launch a container":"launchcontainer",
                        "Stop a container":"stopcontainer",
                        "Delete a container":"deletecontainer",
                        "Delete all containers":"deleteallcontainers",
                        "Pull a container image":"pullimage",
                        "Show the logs of the container":"containerlogs",
                        'Copy a file to container':'copytocontainer',
                        'Copy a file from container':'copyfromcontainer'
                        }
    # this function will return styles and the set main menu which we will use further
    return styles,menu_main