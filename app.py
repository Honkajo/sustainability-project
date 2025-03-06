from flask import Flask, render_template, redirect, request, jsonify
from codecarbon import EmissionsTracker
import subprocess
import os
import time
import threading
import sys
import psutil

app = Flask(__name__)
CSV_PATH = os.path.abspath("./emissions.csv")
carbonboard_process = None

def run_carbonboard():
    """Start carbonboard with enhanced diagnostics"""
    global carbonboard_process
    
    try:
        # Check emissions.csv exists
        if not os.path.exists(CSV_PATH):
            raise FileNotFoundError(f"Emissions file missing: {CSV_PATH}")
        
        # Use the same Python executable and environment
        env = os.environ.copy()
        python_path = sys.executable
        
        carbonboard_process = subprocess.Popen(
            [
                python_path,
                "-m", "codecarbon.viz.carbonboard",
                "--filepath", CSV_PATH,
                "--port", "3334",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            env=env,
            bufsize=1,
            universal_newlines=True
        )

        # Wait for server startup with timeout
        for _ in range(15):  # 15 * 0.2s = 3s total wait
            if carbonboard_process.poll() is not None:
                raise RuntimeError("Carbonboard failed to start")
            try:
                # Check if port is active
                conns = psutil.net_connections()
                if any(conn.laddr.port == 3334 for conn in conns):
                    print("Carbonboard successfully bound to port 3334")
                    break
            except:
                pass
            time.sleep(0.2)
        else:
            raise TimeoutError("Carbonboard didn't start within 3 seconds")
            
    except Exception as e:
        print(f"Critical startup error: {str(e)}")
        if carbonboard_process:
            carbonboard_process.kill()
        raise

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    global carbonboard_process

    # Delete existing emissions.csv file
    if os.path.exists(CSV_PATH):
        os.remove(CSV_PATH)
        
    # Get uploaded file    
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"})

    if not file.filename.endswith('.py'):
        return jsonify({"error": "Invalid file type. Only Python files are allowed for now."})

    # Track emissions
    tracker = EmissionsTracker(
        save_to_file=True,
        output_file=CSV_PATH,
        measure_power_secs=5,
        log_level="INFO",
        allow_multiple_runs=True,
    )

    try:
        tracker.start()
        exec(file.read().decode('utf-8'), {})
    except Exception as e:
        return jsonify({"error": f"Error executing the file: {str(e)}"})
    finally:
        tracker.stop()

    # Verify CSV creation
    if not os.path.exists(CSV_PATH):
        return "Failed to create emissions data"
    time.sleep(3)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({"redirect": "/launch"})
    else:
        return redirect("/launch")
    return redirect("/launch")

@app.route('/launch')
def launch_dashboard():
    try:
        # Check existing process
        if carbonboard_process and carbonboard_process.poll() is None:
            print("Reusing existing carbonboard instance")
        else:
            print("Starting carbonboard")
            thread = threading.Thread(target=run_carbonboard)
            thread.start()
            thread.join(timeout=5)  # Wait for startup completion
            
        return redirect("http://127.0.0.1:3334")
        
    except Exception as e:
        return e

if __name__ == '__main__':
    app.run(port=5000, debug=False, use_reloader=False)