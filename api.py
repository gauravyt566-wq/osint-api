from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "ok", "message": "OSINT API is live!"}

@app.route("/phone")
def phone_lookup():
    number = request.args.get("number")
    if not number:
        return jsonify({"error": "number required"}), 400

    # Dummy response (बाद में database या truecaller जैसी api connect कर लेना)
    data = {
        "number": number,
        "name": "Test User",
        "location": "India",
        "operator": "Jio",
        "facebook": "https://facebook.com/testuser",
        "photo": "https://picsum.photos/200"
    }
    return jsonify(data)

@app.route("/vehicle")
def vehicle_lookup():
    rc = request.args.get("rc")
    if not rc:
        return jsonify({"error": "rc required"}), 400
    return jsonify({
        "rc_number": rc,
        "owner_name": "Rahul Sharma",
        "model_name": "Honda Activa",
        "city": "Delhi",
        "rto": "DL01",
        "insurance_company": "HDFC ERGO",
        "insurance_expiry": "2026-05-14"
    })

@app.route("/insta")
def insta_lookup():
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "username required"}), 400
    return jsonify({
        "username": username,
        "full_name": "Demo User",
        "followers": 1500,
        "following": 250,
        "posts": 23,
        "verified": True,
        "private": False,
        "bio": "This is a demo Instagram bio",
        "profile_pic_url": "https://picsum.photos/300"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
