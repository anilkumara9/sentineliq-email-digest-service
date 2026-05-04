from flask import Blueprint, request, jsonify
from datetime import datetime
import os
from services.groq_service import groq_service
from services.redis_cache import redis_cache

digest_bp = Blueprint('digest', __name__)

def load_prompt(filename, **kwargs):
    path = os.path.join('prompts', filename)
    with open(path, 'r') as f:
        prompt = f.read()
    for key, value in kwargs.items():
        prompt = prompt.replace(f'{{{{{key}}}}}', str(value))
    return prompt

@digest_bp.route('/describe', methods=['POST'])
def describe_email():
    data = request.json
    email_body = data.get('email_body')
    
    if not email_body:
        return jsonify({"error": "email_body is required"}), 400
    
    prompt = load_prompt('describe_prompt.txt', email_body=email_body)
    
    # Check cache
    cached = redis_cache.get(prompt)
    if cached:
        cached['from_cache'] = True
        return jsonify(cached), 200

    result = groq_service.call_groq(prompt)
    
    if result:
        result['generated_at'] = datetime.utcnow().isoformat()
        redis_cache.set(prompt, result)
        return jsonify(result), 200
    else:
        return jsonify({"error": "Failed to generate description", "is_fallback": True}), 500

@digest_bp.route('/recommend', methods=['POST'])
def recommend_actions():
    data = request.json
    description = data.get('description')
    sentiment = data.get('sentiment', 'neutral')
    
    if not description:
        return jsonify({"error": "description is required"}), 400
    
    prompt = load_prompt('recommend_prompt.txt', description=description, sentiment=sentiment)
    
    # Check cache
    cached = redis_cache.get(prompt)
    if cached:
        return jsonify(cached), 200

    result = groq_service.call_groq(prompt)
    
    if result:
        # Assuming the AI returns a JSON object with a list under 'recommendations' 
        # or just the list itself. The prompt asks for a JSON array.
        recommendations = result.get('recommendations', result) if isinstance(result, dict) else result
        
        redis_cache.set(prompt, recommendations)
        return jsonify(recommendations), 200
    else:
        return jsonify({"error": "Failed to generate recommendations", "is_fallback": True}), 500

@digest_bp.route('/generate-report', methods=['POST'])
def generate_report():
    data = request.json
    summaries = data.get('summaries')
    
    if not summaries:
        return jsonify({"error": "summaries is required"}), 400
    
    prompt = load_prompt('report_prompt.txt', summaries=summaries)
    
    # Check cache
    cached = redis_cache.get(prompt)
    if cached:
        return jsonify(cached), 200

    result = groq_service.call_groq(prompt)
    
    if result:
        redis_cache.set(prompt, result)
        return jsonify(result), 200
    else:
        return jsonify({"error": "Failed to generate report", "is_fallback": True}), 500
