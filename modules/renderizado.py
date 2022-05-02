from flask import render_template,request
from .mock_data import seccion

class CustomRouter:
    # index
    def render_index(self):
        return render_template('altern.html', sec= seccion)
