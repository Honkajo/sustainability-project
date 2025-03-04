from flask import Flask, render_template, request, jsonify
from codecarbon import EmissionsTracker

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"})

    if not file.filename.endswith('.py'):
        return jsonify({"error": "Invalid file type. Only Python files are allowed for now."})

    code = file.read().decode('utf-8')

    tracker = EmissionsTracker(save_to_file=False)  # Disable CSV output
    tracker.start()

    try:
        exec_scope = {}  # Capture variables from executed code
        exec(code, exec_scope)
    except Exception as e:
        return jsonify({"error": f"Error executing the file: {str(e)}"})

    tracker.stop()

    emissions = tracker.final_emissions_data  # Correct way to access emissions data
    return jsonify({
        "message": "File processed successfully",
        "emissions": emissions
    })

if __name__ == '__main__':
    app.run(debug=True)
