import re
from flask import Flask, render_template, json, request
import os
import keras
from keras.applications import inception_v3 as inc_net
from keras.preprocessing import image
from keras.applications.imagenet_utils import decode_predictions
from skimage.io import imread
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings(action='ignore') 

 
app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def transform_img_fn(path_list):
    out = []
    for img_path in path_list:
        img = image.load_img(img_path, target_size=(299, 299))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = inc_net.preprocess_input(x)
        out.append(x)
    return np.vstack(out)
 
@app.route("/parse", methods=['POST'])
def home():
    
    url = request.data.decode('utf-8')
    
    images = transform_img_fn([os.path.join('image_sample/', url)])

    inet_model = inc_net.InceptionV3()
    plt.imshow(images[0] / 2 + 0.5)
    
    preds = inet_model.predict(images)

    explain = ""
    for x in decode_predictions(preds)[0]:
        explain = explain + x[1] + ' : ' + str(x[2]) + '    '


    import base
    import image

    explainer = image.ImageExplainer()
    print(images[0].astype('double').shape)
    explanation = explainer.explain_instance(images[0].astype('double'), inet_model.predict, top_labels=50, hide_color=0, num_samples=100)


    from skimage.segmentation import mark_boundaries

    temp, mask = explanation.get_image_and_mask(explanation.top_labels[0], positive_only=True, num_features=5, hide_rest=False)
    plt.imshow(mark_boundaries(temp / 2 + 0.5, mask))

    for filename in os.listdir('static/result/'):
        print(filename)
        if (filename == 'result.png'):  # not to remove other images
            os.remove('static/result/' + filename)


    plt.imsave('static/result/result.png', mark_boundaries(temp / 2 + 0.5, mask))

    return json.dumps(explain)


@app.route("/main")
def main():
    return render_template('main.html')


if __name__ == "__main__":
    app.run()
    










