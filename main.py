from flask import Flask, request, jsonify
from risk_engine import assess_risk
from filters import is_message_allowed
import requests
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

def get_location(ip):
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        data = response.json()
        return data.get("country_name", "Unknown")
    except:
        return "Unknown"

@app.route("/chat", methods=["POST"])
def chat():
    user_ip = request.remote_addr
    user_message = request.json.get("message", "")

    country = get_location(user_ip)
    risk = assess_risk(country)

    logging.info(f"[{user_ip}] from {country} | Risk: {risk}")

    if risk == "high":
        return jsonify({"message": "Access restricted due to legal limitations."}), 403

    if not is_message_allowed(user_message, country):
        return jsonify({"message": "Message contains restricted content in your jurisdiction."}), 400

    response = f"Echo: {user_message}"
    return jsonify({"message": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)