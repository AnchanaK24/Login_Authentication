
from init import init_app

app=init_app()


@app.route('/')
def welcome():
    return "Welcome"

if __name__ ==  '__main__':
    app.run(debug=True)