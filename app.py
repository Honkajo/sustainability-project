from flask import Flask, render_template, request, jsonify
from codecarbon import EmissionsTracker

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if file is included in the request
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']

    # Check if a file is selected
    if file.filename == '':
        return jsonify({"error": "No selected file"})

    # Ensure the uploaded file is a Python file (this can be customized later)
    if not file.filename.endswith('.py'):
        return jsonify({"error": "Invalid file type. Only Python files are allowed for now."})

    # Read the file content directly from memory
    code = file.read().decode('utf-8')  # Read the file content as a string

    # Track emissions while executing the code
    tracker = EmissionsTracker(output_method=None) #Disables file output
    tracker.start()

    # Execute the uploaded Python code safely
    try:
        exec(code)  # Execute the uploaded Python code (still risky, proceed with caution)
    except Exception as e:
        return jsonify({"error": f"Error executing the file: {str(e)}"})

    tracker.stop()

    # Return the emission data
    emissions = tracker.final_emissions_data
    return jsonify({
        "message": "File processed successfully",
        "emissions": emissions
    })

if __name__ == '__main__':
    app.run(debug=True)

