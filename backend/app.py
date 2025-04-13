from flask import Flask, request, jsonify
from match_score import compute_match

app = Flask(__name__)

@app.route('/match', methods=['POST'])
def match():
    try:
        data = request.get_json(force=True)
        resume = data.get('resume', '')
        jd = data.get('job_description', '')
        score, keywords = compute_match(resume, jd)
        return jsonify({"score": score, "matched_keywords": keywords})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
