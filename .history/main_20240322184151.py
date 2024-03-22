from extractors.berlin import extract_berlin_jobs
# from filex import save_to_file

from flask import Flask,render_template, request

app = Flask("JobScrapper")

db={}

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    if keyword in db:
        jobs = db[keyword]
    else:
        jobs = extract_berlin_jobs(keyword)
        db[keyword] = jobs
    return render_template('search.html',keyword=keyword, jobs=jobs)

app.run()

