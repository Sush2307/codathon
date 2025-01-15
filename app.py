from flask import Flask, render_template, request, jsonify

app=Flask(__name__,template_folder='template')

# In-memory data stores
volunteers = []
ngos = []


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET"])
def register_page():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():
    data = request.form  # Use request.form for form data
    user_type = data.get("userType")

    if user_type == "volunteer":
        volunteer = {
            "name": data.get("name"),
            "email": data.get("email"),
            "skills": data.get("skills"),
            "availability": data.get("availability")
        }
        volunteers.append(volunteer)
        return jsonify({"message": "Volunteer registered successfully!", "volunteers": volunteers})
    elif user_type == "ngo":
        ngo = {
            "name": data.get("name"),
            "email": data.get("email"),
            "requirement": data.get("ngoRequirement")
        }
        ngos.append(ngo)
        return jsonify({"message": "NGO registered successfully!", "ngos": ngos})
    else:
        return jsonify({"error": "Invalid user type"}), 400

if __name__ == "__main__":
    app.run(debug=True)