# Import the Flask class, Render_template for escaping all the html code, 
from flask import Flask, render_template, request, jsonify
from main import get_ai_response
from response import get_response

# Create an instance of the class Flask
app = Flask(__name__)

# Tell which URL should trigger the app
@app.get("/")
def index_get():
    return render_template("index.html")

@app.post("/predict")
def predict():
    data = request.get_json()  # Correctly call get_json as a method
    text = data.get("message")  # Access the 'message' key in the JSON data
    response = get_response(text)
    message = {"answer": response}
    
    # Return the response as a JSON object
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
