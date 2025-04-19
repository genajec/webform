from flask import Flask, render_template, request, jsonify
import os
import logging
from dotenv import load_dotenv
from pathlib import Path

# Загружаем переменные окружения из .env файла
env_path = Path('.') / '.env'
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
    logging.info("Переменные окружения загружены из .env")

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__, static_folder='static', static_url_path='/static')
app.template_folder = 'templates'

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/terms")
def terms():
    return render_template('terms.html')
    
@app.route("/privacy")
def privacy():
    return render_template('privacy.html')
    
@app.route("/refund")
def refund():
    return render_template('refund.html')

@app.route("/api/status")
def api_status():
    return jsonify({
        "status": "running", 
        "message": "FaceForm AI website is active"
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

# For running directly with Python (without Gunicorn)
if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=5000)