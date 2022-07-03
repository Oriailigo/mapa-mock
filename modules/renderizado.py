from flask import render_template,request
from .mock_data import seccion
import js2py
  
eval_res, tempfile = js2py.run_file("./static/js/js.js")
are=tempfile.wish("GeeksforGeeks")

class CustomRouter:
    # index
    def render_index(self):
        # return render_template('altern.html', sec= seccion)
        return render_template('index_back.html',sec=seccion, area=are)
    def render_altern(self,id):
        return render_template('altern.html', sec=seccion, area=id)

