from flask import Flask, request, jsonify

app = Flask(__name__)

# 🔹 Dummy function (safe response)
def safe_response(data):
    return {k: (v if v else "N/A") for k, v in data.items()}

# 🔹 Number Info
@app.route("/number")
def number():
    number = request.args.get("q")
    return jsonify(safe_response({
        "number": number,
        "caller_name": "Rahul Sharma",
        "location": "Delhi, India",
        "operator": "Jio",
        "facebook": "https://facebook.com/rahul.sharma",
        "photo": "https://example.com/photo.jpg"
    }))

# 🔹 Aadhaar Info
@app.route("/aadhaar")
def aadhaar():
    aadhaar = request.args.get("q")
    return jsonify(safe_response({
        "aadhaar": aadhaar,
        "name": "Gaurav Kumar",
        "dob": "1998-05-17",
        "gender": "Male",
        "state": "Uttar Pradesh",
        "district": "Lucknow"
    }))

# 🔹 Vehicle RC Info
@app.route("/rc")
def rc():
    rc_number = request.args.get("q")
    return jsonify(safe_response({
        "rc_number": rc_number,
        "owner_name": "Amit Verma",
        "father_name": "Rajesh Verma",
        "model_name": "Honda Activa",
        "maker_model": "Activa 6G",
        "vehicle_class": "Scooter",
        "fuel_type": "Petrol",
        "fuel_norms": "BS6",
        "registration_date": "2021-02-12",
        "insurance_company": "HDFC Ergo",
        "insurance_expiry": "2026-02-12",
        "fitness_upto": "2031-02-12",
        "puc_upto": "2025-08-01",
        "tax_upto": "2031-02-12",
        "rto": "UP32",
        "city": "Lucknow",
        "address": "Gomti Nagar, Lucknow",
        "phone": "+91-9876543210"
    }))

# 🔹 Email Info
@app.route("/email")
def email():
    email = request.args.get("q")
    return jsonify(safe_response({
        "email": email,
        "status": "valid",
        "domain": email.split("@")[-1],
        "breached": True,
        "last_seen": "2023-07-10"
    }))

# 🔹 Password Lookup
@app.route("/password")
def password():
    pwd = request.args.get("q")
    return jsonify(safe_response({
        "password": pwd,
        "leaked": True,
        "times_seen": 4521,
        "sources": ["Collection#1", "RockYou.txt"]
    }))

# 🔹 IP Info
@app.route("/ip")
def ip():
    ip_addr = request.args.get("q")
    return jsonify(safe_response({
        "ip": ip_addr,
        "city": "Mumbai",
        "region": "Maharashtra",
        "country": "IN",
        "isp": "Airtel",
        "asn": "AS45609"
    }))

# 🔹 Telegram ID
@app.route("/telegram")
def telegram():
    tg = request.args.get("q")
    return jsonify(safe_response({
        "telegram": tg,
        "name": "TG User",
        "bio": "Tech enthusiast",
        "groups": 53,
        "last_seen": "Recently"
    }))

# 🔹 Facebook Info
@app.route("/facebook")
def facebook():
    fb = request.args.get("q")
    return jsonify(safe_response({
        "facebook": fb,
        "name": "Arjun Singh",
        "friends": 2034,
        "profile_link": f"https://facebook.com/{fb}"
    }))

# 🔹 Instagram Info
@app.route("/instagram")
def instagram():
    insta = request.args.get("q")
    return jsonify(safe_response({
        "username": insta,
        "full_name": "Priya Sharma",
        "followers": 15200,
        "following": 301,
        "posts": 120,
        "verified": True,
        "private": False,
        "bio": "Travel | Food | Fashion"
    }))

# 🔹 VK Info
@app.route("/vk")
def vk():
    vk_id = request.args.get("q")
    return jsonify(safe_response({
        "vk": vk_id,
        "name": "Russian User",
        "city": "Moscow",
        "friends": 534
    }))

# 🔹 Domain Info
@app.route("/domain")
def domain():
    site = request.args.get("q")
    return jsonify(safe_response({
        "domain": site,
        "registrar": "GoDaddy",
        "creation_date": "2017-05-20",
        "expiry_date": "2027-05-20",
        "nameservers": ["ns1.example.com", "ns2.example.com"]
    }))

# 🔹 Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
