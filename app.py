from flask import Flask, render_template, jsonify 

app = Flask(__name__)

TOURS = [
  {
    "id": 1,
    "title": "Day Trip",
    "description": "Thrilling Lang Tengah Island day trip: explore wonders in a day.",
    "price": "MYR 250.00",
    "image":"/static/turtle.jpg",
    "alt": "Lang Tengah Island"
  },
  {
    "id": 2,
    "title": "Boat Transfer",
    "description": "Return public speedboat transfer for easy Lang Tengah access.",
    "price": "MYR 160.00",
    "image":"/static/turtle.jpg",
    "alt": "Pulau Lang Tengah"
  },
  {
    "id": 3,
    "title": "Boat Charter",
    "description": "Lang Tengah Island private boat charter for exclusive transfers.",
    "price": "MYR 600.00",
    "image":"/static/turtle.jpg",
    "alt": "Lang Tengah Campsite"
  },
  {
    "id": 4,
    "title": "Private Day Trip",
    "description": "Tailored Lang Tengah day trip for family, friends, or colleagues.",
    "price": "MYR 5,000.00",
    "image":"/static/turtle.jpg",
    "alt": "Han at Traisea"
  },

]



@app.route("/")
def hello_world():
    return render_template("home.html", tours=TOURS, name="Lang Tengah Island")

@app.route("/api/tours")
def list_tour():
    return jsonify(TOURS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)  