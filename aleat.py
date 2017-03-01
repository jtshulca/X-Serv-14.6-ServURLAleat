#!/usr/bin/python3

import webapp
import random

class aleat(webapp.webApp):
    """Generator random URLs with classes"""

    def process(self, parsedRequest):
        newURL = str(random.randint(0, 1000000000000))	#cogemos un numero de cero a otro muy grande
        return ("200 OK", "<html><body><a href= '"+ newURL +"'>Dame otra</a></body></html>")

if __name__ == "__main__":
    port = 1234
    testWebApp = aleat("localhost", port)
    
