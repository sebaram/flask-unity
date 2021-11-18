# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 21:28:50 2021

@author: JY
"""
from flask import Flask
from flask import jsonify, render_template, send_file, redirect

import os
import pandas as pd

from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__,
                 static_folder='static',
                 template_folder='templates')

DB = pd.read_csv("artworks_db.csv", index_col=0)


@app.route('/', methods=['GET', 'POST'])
def img_list():
    return render_template('list.html')

@app.route('/info/id/<int:report_id>', methods=['GET', 'POST'])
def get_info_by_id(report_id):
    try:
        return DB.loc[report_id].to_json(orient = 'records', force_ascii=False)
    except Exception as err:
        print(repr(err))
        return jsonify(error=repr(err))
    
@app.route('/img/id/<int:report_id>', methods=['GET', 'POST'])
def get_img_by_id(report_id):
    try:
        img_path = DB.img_path[report_id]
        if img_path[:4] == "http":
            return redirect(img_path)
        else:
            return send_file(img_path)
    except Exception as err:
        print(repr(err))
        return send_file(create_text_to_image(repr(err)))

def create_text_to_image(str_):
    img = Image.new('RGB', (500,500), color = (73, 109, 137))
 
    fnt = ImageFont.truetype(os.path.join('static','arial.ttf'), 30)
    d = ImageDraw.Draw(img)
    d.text((10,10), str_, font=fnt, fill=(255, 255, 0))
     
    tmp_path = os.path.join("img","error.png")
    img.save(tmp_path)
    
    return tmp_path
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=12572, debug=True)