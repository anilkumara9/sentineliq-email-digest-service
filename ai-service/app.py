import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Initialize Limiter
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["30 per minute"],
        storage_uri="memory://",
    )

    # Register blueprints
    from routes.digest_routes import digest_bp
    from routes.health_routes import health_bp
    
    app.register_blueprint(digest_bp, url_prefix='/api/v1/ai')
    app.register_blueprint(health_bp, url_prefix='/health')

    @app.route('/')
    def index():
        return {"message": "Email Digest AI Service is running"}, 200

    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
