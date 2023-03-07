from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,50,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
  }
]

def load_jobs_from_db():
  with engine.connect() as conn:
   result = conn.execute(text("select * from jobs"))

   jobs = []
   for row in result.all():
     # get the column names
     keys = result.keys()
     # create a dictionary for the row
     row_dict = dict(zip(keys, row))
     # append the dictionary to the list
     jobs.append(row_dict)
   return jobs 

@app.route("/")
def hello_company():
  #jobs = load_jobs_from_db()
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':