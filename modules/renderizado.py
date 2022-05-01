from flask import render_template,request
from .mock_data import clase_info, seccion

class CustomRouter:
    # index
    def render_index(self):
        return render_template('index.html', sec= seccion)
