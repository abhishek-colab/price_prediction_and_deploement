#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 02:29:26 2020

@author: abhisheksingh
"""

from flask import Flask, request, jsonify
import util


app = Flask(__name__)


@app.route('/predict_price',methods=['POST'])
def predict_mobile_price():
    brand = request.form['brand']
    bands_3G = bool(request.form['bands_3G'])
    '''
    bands_4G = bool(request.form['bands_4G'])
    GPRS = bool(request.form['GPRS'])
    EDGE = bool(request.form['EDGE'])
    status = request.form['brand']
    weight_g = float(request.form['weight_g'])
    display_type = float(request.form['display_type'])
    display_size = float(request.form['display_size'])
    OS = request.form['OS']
    CPU = request.form['CPU']
    Chipset = request.form['Chipset']
    GPU = bool(request.form['GPU'])
    memory_card = float(request.form['memory_card'])
    internal_memory = float(request.form['internal_memory'])
    RAM = float(request.form['RAM'])
    primary_camera = float(request.form['primary_camera'])
    secondary_camera = float(request.form['secondary_camera'])
    loud_speaker = bool(request.form['loud_speaker'])
    audio_jack = bool(request.form['audio_jack'])
    WLAN = bool(request.form['WLAN'])
    GPS = bool(request.form['GPS'])
    have_fingerprint = bool(request.form['have_fingerprint'])
    bluetooth= int(request.form['bluetooth'])
    battery = float(request.form['battery'])
    display_res = float(request.form['display_res'])
    screen_to_body_ratio = float(request.form['screen_to_body_ratio'])
    width = float(request.form['width'])
    diag_len = float(request.form['diag_len'])   
    release_date = float(request.form['release_date'])
    '''
    response = jsonify({
        'estimated_price': util.predict_mobile_price(brand=brand, bands_3G=bands_3G )
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
    

if __name__ == '__main__':
    print("Starting Flask Server...")
    app.run()