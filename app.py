import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
# import os
# import imp
# import ctypes
# import thread
# import win32api

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Sales should be $ {}'.format(output))


@app.route('/results', methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


# if __name__ == "__main__":
    # basepath = imp.find_module('numpy')[1]
    # ctypes.CDLL(os.path.join(basepath, 'core', 'libmmd.dll'))
    # ctypes.CDLL(os.path.join(basepath, 'core', 'libifcoremd.dll'))

    # # Now set our handler for CTRL_C_EVENT. Other control event 
    # # types will chain to the next handler.
    # def handler(dwCtrlType, hook_sigint=thread.interrupt_main):
    #     if dwCtrlType == 0: # CTRL_C_EVENT
    #         hook_sigint()
    #         return 1 # don't chain to the next handler
    #     return 0 # chain to the next handler

    # win32api.SetConsoleCtrlHandler(handler, 1)
app.run(host='0.0.0.0',port=5007, debug=True)

   