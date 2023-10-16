
# FastAPI Example App

This is a simple API app built with FastAPI framework. It provides some dummy data for testing and learning purposes.

## Dependencies

To run this app, you need to have Python 3.7+ installed¹[1]. You also need to install the following packages:

- fastapi: the web framework for building APIs²[2].
- uvicorn: the ASGI server that loads and serves the app³[3].
- fuzzywuzzy: the library for fuzzy matching of categories.
- python-Levenshtein: the library for improving the performance of fuzzywuzzy.

You can install all of these with:

```bash
pip install fastapi uvicorn fuzzywuzzy python-Levenshtein
```

## Usage

To run the app, use the command:

```bash
uvicorn main:app --reload⁴[4]
```

This will start the server on http://127.0.0.1:8000⁵[5]⁶[6].

You can access the interactive API documentation at http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc.

The app has two endpoints:

- `/category/all`: returns all the data in the JSON file.
- `/{category}`: returns the data for a specific category, or the closest match if the category is not found.

The data is stored in a JSON file named `categoryQuotes.json`. It contains some quotes categorized by topics such as love, life, humor, etc.

You can modify the JSON file to add or remove categories and quotes as you wish.

## Disclaimer

This app is not intended to be used in production. It is only a basic example for learning and experimenting with FastAPI. Use it at your own risk.
