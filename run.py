from website import create_app

app = create_app()

# This will run the application in debug mode by default, we may want to change
# that before going online
if __name__ == '__main__':
    app.run(debug=True)
