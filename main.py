from app import app

#app.run(debug=1, host="::", port=5000)
def main():
    app.run(debug=False, host="0.0.0.0")


if __name__ == '__main__':
    main()
