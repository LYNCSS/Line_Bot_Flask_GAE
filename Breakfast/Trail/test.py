# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 09:16:14 2019

@author: user
"""
class NotFlask():
    def route(self, route_str):
        def decorator(f):
            print("inside_Decorator")
            f()
            print("PostDecorator")
 
        return decorator
 
app = NotFlask()
 
@app.route("/")
def hello():
    print("Hello world")
    

if __name__ == "__main__":
    print(type(hello))