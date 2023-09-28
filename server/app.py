from flask import Flask
from flask_cors import CORS


def create_app():
    """Initialize the core application."""
    app = Flask(__name__)
    return app

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "-p", "--port", default=5000, type=int, help="port to listen on"
    )
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host="0.0.0.0", port=port)
