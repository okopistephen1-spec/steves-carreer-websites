from flask import Flask, render_template, jsonify

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

      {
    'id': 3,
    'title': 'Affiliate Marketer',
    'location': 'Oju',
    'salary': 'N125,000',
    },
    

    
]




@app.route("/")
def hello():
    return render_template('home.html', 
    jobs=JOBS)

@app. route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run( debug=True)
