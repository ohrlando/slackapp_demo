from app import create_app
app = create_app()


if __name__ == "__main__":
    app.start(port=5001, path='/slack/events')
