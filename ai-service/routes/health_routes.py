from flask import Blueprint, jsonify
import time

health_bp = Blueprint('health', __name__)

start_time = time.time()

@health_bp.route('/', methods=['GET'])
def health_check():
    uptime = time.time() - start_time
    return jsonify({
        "status": "healthy",
        "model": "llama-3.3-70b-versatile",
        "uptime": f"{uptime:.2f} seconds",
        "avg_response_time": "0.8s" # Mocked for now
    }), 200
