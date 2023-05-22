import os
from flask import Flask, flash, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from photo_resrorer import predict_image

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSION = {'txt', 'pdf', 'png', 'jpg', 'gif', 'jpeg'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16*1000*1000  # Max allowed image size 16 MB


@app.route("/")
def home():
    return render_template("index.html")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            full_filename = "." + \
                url_for("static", filename="/images"+filename)
            print(full_filename)
            file.save(full_filename)

            predicted_img_url = predict_image(
                full_filename, request.form['selectedFeature'])
            return render_template("index.html", filename=filename, restored_img_url=predicted_img_url)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('download_file', name=filename))


if __name__ == "__main__":
    app.run(debug=True)
