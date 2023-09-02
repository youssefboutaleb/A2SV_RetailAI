from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import pandas as pd
from predict_storage import predict_storage  # Replace with your predictive model function

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')

        file = request.files['file']

        # If the user does not select a file, the browser also
        # submits an empty file without a filename
        if file.filename == '':
            return render_template('index.html', error='No selected file')

        if file:
            # Save the uploaded file to the UPLOAD_FOLDER
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Call the prediction function with the file path
            result = predict_storage(file_path)

            # Render a template with the result
            return render_template('result.html', predictions=result)  # Changed 'result' to 'predictions'

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
