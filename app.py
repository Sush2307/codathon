from flask import Flask, render_template, request, jsonify

app=Flask(__name__,template_folder='template')

# In-memory data stores
volunteers = []
ngos = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    data = request.json
    volunteers.append(data)
    return jsonify({"message": "Volunteer registered successfully!", "volunteers": volunteers})


@app.route("/list_ngos", methods=["GET"])
def list_ngos():
    return jsonify({"ngos": ngos})


@app.route("/post_ngo", methods=["POST"])
def post_ngo():
    data = request.json
    ngos.append(data)
    return jsonify({"message": "NGO opportunity posted successfully!", "ngos": ngos})


@app.route("/match_volunteers", methods=["GET"])
def match_volunteers():
    matches = []
    for ngo in ngos:
        suitable_volunteers = [
            v for v in volunteers if ngo["required_skill"] in v["skills"]
        ]
        matches.append({"ngo": ngo, "volunteers": suitable_volunteers})
    return jsonify({"matches": matches})


if __name__ == "__main__":
    app.run(debug=True)