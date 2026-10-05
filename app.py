from flask import Flask, jsonify
import requests
import pandas as pd 
import os

app = Flask(__name__)

@app.route("/get-data", methods = ["GET"])
def get_data():
    # Target website url
    url = "https://www.huduser.gov/hudapi/public/usps?type=1&query=WA"

    
    token = os.getenv("HUD_API_TOKEN")

    headers = {
        "Authorization": f"Bearer {token}"
    }
    # Fetch the webpage 
    response = requests.get(url, headers=headers)

    # Return an error if the request is unsuccessful
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch website"}), 500

    # Read the data in from the website 
    data = response.json()
    results = data["data"]["results"]

    # Save the website data into a data fram then CSV 
    df = pd.DataFrame(results)
    df.to_csv("hud_crosswalk.csv", index = False)

    return df.to_json(orient = "records")


if __name__ == "__main__":
    app.run(debug = True)