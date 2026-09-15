from flask import Flask, jsonify
import requests
import pandas as pd 

app = Flask(__name__)

@app.route("/get-data", methods = ["GET"])
def get_data():
    #target website url
    url = "https://www.huduser.gov/hudapi/public/usps?type=1&query=WA"

    
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI2IiwianRpIjoiNjMzN2Q2M2NiNmU0MmVlZjc5M2Y2YjBjNmZiYTRkYjgwZjhjMzU3ZDUzNTU1MTc1ZDkxOTNkNzc4OGM1ZDljNDVhMjE1OGY3OGRiYTBlNTUiLCJpYXQiOjE3ODk1MDUyNjguODU5MzgzLCJuYmYiOjE3ODk1MDUyNjguODU5Mzg2LCJleHAiOjIxMDUxMjQ0NjguODU0NDM1LCJzdWIiOiIxNDA5NzkiLCJzY29wZXMiOltdfQ.ciVELqG9DEiUAYtEjsCTPzk-RymFe0hCF0-_ht5B-wlgu1SXLYmINXx5bG2gNH9pIa2s5Bxnw429I4GRDydM1A"

    headers = {
        "Authorization": f"Bearer {token}"
    }
    # fetch the webpage 
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return jsonify ({"error": "Falied to fetch website"}), 500

    data = response.json()

    results = data["data"]["results"]


    df = pd.DataFrame(results)

    return df.to_json(orient = "records")


if __name__ == "__main__":
    app.run(debug = True)