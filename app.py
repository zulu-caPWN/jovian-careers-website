from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {'id':1,
  'title': 'Data Analyst',
  'location': 'Bengluru, India',
  'salary': 'Rs. 11,00,000'
  },
  {'id':2,
  'title': 'Data Dogger',
  'location': 'Bengal, Tiger',
  'salary': 'Rs. 10,00,000'
  },
  {'id':3,
  'title': 'Data Diggler',
  'location': 'Remote USA',
  'salary': '1'
  },
  {'id':4,
  'title': 'Data Docker',
  'location': 'San Franciso, CA',
  'salary': '$120,000'
  },
]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS,
                          company_name="Jovan")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)