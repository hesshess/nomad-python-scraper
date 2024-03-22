# from extractors.berlin import extract_berlin_jobs
# from filex import save_to_file

from flask import Flask,render_template, request

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    return render_template('search.html',keyword=keyword)

app.run()

