from fastapi import FastAPI
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

app = FastAPI()

# Load the JSON file at startup
with open('categoryQuotes.json') as f:
    data = json.load(f)

@app.get("/category/{category}")
async def read_category(category: str):
    # Check if the category exists in the JSON data
    if category in data:
        return {category: data[category]}
    else:
        # If the category does not exist, find the closest match
        closest_match, score = process.extractOne(category, data.keys())
        
        # You can set a threshold for score
        if score > 80:
            return {closest_match: data[closest_match]}
        else:
            return {"error": "Category not found"}

@app.get("/data/all")
async def read_all():
    return data
    