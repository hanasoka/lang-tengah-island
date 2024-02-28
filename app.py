from flask import Flask, render_template, jsonify 

app = Flask(__name__)

TOURS = [
  {
    "id": 1,
    "title": "Lang Tengah Day Trip",
    "description": """
Experience the wonders of Lang Tengah Island on a thrilling day excursion, offering breathtaking views and unforgettable moments.""",
    "price": "MYR 250.00",
    "image":"/static/turtle.jpg",
    "alt": "Lang Tengah Island"
  },
  {
    "id": 2,
    "title": "Lang Tengah 3D2N",
    "description": """
Immerse yourself in the natural beauty of Lang Tengah Island during a comprehensive 
3-day, 2-night adventure, creating memories that last a lifetime.""",
    "price": "MYR 700.00 - MYR 2500.00",
    "image":"/static/turtle.jpg",
    "alt": "Pulau Lang Tengah"
  },
  {
    "id": 3,
    "title": "Lang Tengah Camping",
    "description": """
Embark on an adventurous camping journey on Lang Tengah Island, uncovering its 
hidden gems and embracing the essence of outdoor living.""",
    "price": "MYR 500.00",
    "image":"/static/turtle.jpg",
    "alt": "Lang Tengah Campsite"
  },
  {
    "id": 4,
    "title": "Private Group Trip",
    "description": """
Customize your perfect day trip for family, friends, or colleagues, ensuring a 
tailored and unforgettable experience.""",
    "price": "MYR 5,000.00",
    "image":"/static/turtle.jpg",
    "alt": "Han at Traisea"
  },
  {
    "id": 5,
    "title": "Redang Island 3 Days 2 Nights",
    "description": """
Discover the enchanting beauty of Redang Island during a memorable 3-day, 
2-night getaway, offering a range of experiences for all.""",
    "price": "MYR 700.00 - MYR 5,000.00",
    "image":"/static/turtle.jpg",
    "alt": "Redang Island"
  },
  {
    "id": 6,
    "title": "Bidong Island Day Trip",
    "description": """
Explore the captivating sights of Pulau Bidong, also known as the Little Saigon 
of Malaysia, on an enriching day trip filled with cultural immersion and scenic views.""",
    "price": "MYR 200.00",
    "image":"/static/banner.jpg",
    "alt": "Bidong Island"
  }
]



@app.route("/")
def hello_world():
    return render_template("home.html", tours=TOURS, name="Lang Tengah Island")

@app.route("/api/tours")
def list_tour():
    return jsonify(TOURS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)  