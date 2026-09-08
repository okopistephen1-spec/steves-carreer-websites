from flask import Flask, render_template, jsonify, request

app = Flask(__name__)



JOBS = [
    {
        "id": 1,
        "title": "Python Developer",
        "location": "Lagos",
        "salary": "₦500,000"
    },

    {
        "id": 2,
        "title": "Frontend Developer",
        "location": "Remote",
        "salary": "₦400,000"
    },

    {
        "id": 3,
        "title": "Backend Developer",
        "location": "Abuja",
        "salary": "₦600,000"
    }
]



@app.route("/")
def home():

    return render_template(
        "home.html",
        jobs=JOBS
    )


@app.route("/jobs")
def list_jobs():

    return jsonify(JOBS)


@app.route("/apply/<int:job_id>", methods=["GET", "POST"])
def apply(job_id):

    selected_job = None

    for job in JOBS:

        if job["id"] == job_id:
            selected_job = job
            break

    if selected_job is None:
        return "Job not found", 404

    return render_template(
        "apply.html",
        job=selected_job
    )


if __name__ == "__main__":
    app.run(debug=True)
