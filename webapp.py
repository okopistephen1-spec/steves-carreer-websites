from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
    'id': 1,
    'title': 'Frontend developer',
    'location': 'Asa',
    'salary': 'N100,000',
    },

    {
    'id': 2,
    'title': 'Backend developer',
    'location': 'Asa 1',
    'salary': 'N200,000',
    },
    {
    'id': 3,
    'title': 'Expert Hacker',
    'location': 'Asa 3',
    'salary': 'N300,000',
    },
    

    
]




@app.route("/")
def hello():
    return render_template('home.html', 
    jobs=JOBS)


if __name__ == "__main__":
    app.run( debug=True)
