# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 21:28:50 2021

@author: JY
"""
from flask import Flask
from flask import render_template, send_file

import os
import pandas as pd


app = Flask(__name__,
                 static_folder='static',
                 template_folder='templates')

DB = pd.read_csv("artworks_db.csv", index_col=0)


@app.route('/', methods=['GET', 'POST'])
def img_list():
    return render_template('list.html')


@app.route('/id/<int:report_id>', methods=['GET', 'POST'])
def get_img_by_id(report_id):
    if report_id in DB.index:
        return send_file(DB.img_path[report_id])
    else:
        return send_file(os.path.join("img","ctar.png"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=12572, debug=True)