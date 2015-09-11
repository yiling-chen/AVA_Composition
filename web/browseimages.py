import os, os.path
import random
import string
import numpy as np
import cherrypy

class BrowseImage(object):
    def __init__(self):
        # header and footer html
        self.header = """
            <!doctype html>
            <head>
            <title>Browse image</title>
            </head>
            <body>
            <div align="center">
              <form align="center" method="get" action="generate">
                <label>How many random images to show?:</label>
                <input type="text" value="100" name="length" />
                <button type="submit">Show me the images!</button>
              </form>
            </div>
            <div align="center">
            """

        self.footer = """
            </body>
            </html>
            """

        self.imageIDs = np.loadtxt('../AVA.txt', dtype=int)[:,1]

    @cherrypy.expose
    def index(self):
        html = self.header
        html += self.footer
        return html

    @cherrypy.expose
    def generate(self, length=100):
        html = self.header
        for i in range(int(length)):
            html += "<img src=/static/"
            html += str(self.imageIDs[i])
            html += ".jpg width='200'/>"
        html += "</div>"
        html += self.footer
        return html

if __name__ == '__main__':
    conf = {
        '/': {
             'tools.sessions.on': True,
             'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
         '/static': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': '../images'
        }
    }
    cherrypy.quickstart(BrowseImage(), '/', conf)
