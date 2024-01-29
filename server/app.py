#!/usr/bin/env python3

# Standard library imports

# Local imports
from app_setup import app, db, ma, api

# Route imports

# Add resources


@app.route("/")
def index():
    return "<h1>Project Server</h1>"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
