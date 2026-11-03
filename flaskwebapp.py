from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return"<h2>Welcom to app"


#create a new route
@app.route('/studentID/<int:id>')
def studentID(id):
    return (f"My panther id is {id}.</h2>")


@app.route('/search')
def search():
    keyword =  request.args.get('keyword', default = None)
    limit = request.args.get('limit', default= 5, type = int)
    return(f"<h2> Search results for {keyword}, limit {limit}.</h2>")


@app.route('/api/data')
def data():
    some_data = {
        "status": "success",
        "course": "CIS3590",
        "students": 35,
        "topics": ["Streamlit", "flask"]

    }
    return jsonify(some_data)




if __name__ == '__main__':

    app.run(debug = True,
             port =5050)
