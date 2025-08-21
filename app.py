from flask import Flask, render_template, request, jsonify
import json, random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shoot', methods=['POST'])
def shoot():
    reaction = random.uniform(0.1, 0.6)
    with open('config.json') as f:
        config = json.load(f)
    result = "headshot" if reaction < config["reaction_threshold"] else "miss"
    return jsonify({
        "reaction": round(reaction, 3),
        "result": result,
        "message": f"{result.upper()}! Reaction Time: {round(reaction, 3)}s"
    })

@app.route('/leaderboard', methods=['POST'])
def leaderboard():
    data = request.json
    with open('leaderboard.json', 'r+') as f:
        scores = json.load(f)
        scores.append(data)
        f.seek(0)
        json.dump(scores, f, indent=2)
    return jsonify({"status": "saved"})

if __name__ == '__main__':
    app.run(debug=True)
