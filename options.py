#!/home/akhil/anaconda3/bin/python
import variables 
from form import form
from env import cgiRoute
def nav(inp):
    # function to return the title of the page
    print(f"""
        <nav style="position: relative;">
        <a href="{cgiRoute}" style="position: absolute; left: 10px;">
        <i class="bi bi-house"></i>
        </a>
        <a href="{cgiRoute}/{inp}">{inp.capitalize()}</a>
        </nav>
    """.format(inp.upper()))
def output(platform):
    # based on the platform the selected it will go to a route where sub menu options will be displayed
    menu_main=variables.values()[1]
    nav(platform.upper())
    print("<div class='main_menu'>")
    for i in menu_main[platform.lower()]:
        if(menu_main[platform.lower()][i]!=None):
            print("<h1 class='menu'><a href='{2}menu/{0}'>{1}</a></h1>".format(menu_main[platform.lower()][i],i.capitalize(),platform))
    print("</div>")