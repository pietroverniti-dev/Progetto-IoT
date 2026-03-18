from flask import Flask, jsonify, render_template
from pymongo import MongoClient

# ------------------------------
# CONFIG
# ------------------------------
MONGO_URL = "mongodb://127.0.0.1:27017"
DB_NAME = "radarDB"
COLLECTION_NAME = "fasce"

# ------------------------------
# MONGO
# ------------------------------
mongo = MongoClient(MONGO_URL)
db = mongo[DB_NAME]
collection = db[COLLECTION_NAME]

# ------------------------------
# FLASK
# ------------------------------
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/dati")
def api_dati():
    dati = list(collection.find().sort("timestamp", -1).limit(200))
    for d in dati:
        d["_id"] = str(d["_id"])
    return jsonify(dati[::-1])

@app.route("/api/live")
def api_live():
    """Ultimo documento in DB: distanza e fascia più recenti."""
    ultimo = collection.find_one(sort=[("timestamp", -1)])
    if ultimo is None:
        return jsonify({"distanza": None, "fascia": None})
    return jsonify({
        "distanza": ultimo["distanza"],
        "fascia": ultimo["fascia"]
    })

# ------------------------------
# MAIN
# ------------------------------
if __name__ == "__main__":
    print("Server web attivo su http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)