from flask import Flask, request, jsonify, render_template
from ai_model import run_ai_model

app = Flask(__name__)

@app.route('/api/process-csv', methods=['POST'])
def process_csv():
    try:
        # Retrieve the uploaded CSV file
        uploaded_file = request.files['csv-file']

        # Save the uploaded CSV file to a temporary location
        temp_file_path = 'temp.csv'
        uploaded_file.save(temp_file_path)

        # Call the AI model function to process the CSV data
        run_ai_model(temp_file_path)  # Call the AI model function with the CSV file path

        # You can return a response or result here as needed
        return jsonify({'message': 'CSV file processed successfully'})

    except Exception as e:
        error_message = str(e)
        return jsonify({'error': error_message}), 400

@app.route('/')
def index():
    return render_template('my_template.html')  # Render the HTML template

if __name__ == '__main__':
    app.run(debug=True)
