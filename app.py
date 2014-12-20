from flask import Flask, jsonify, render_template, request
import requests
app = Flask(__name__)
#app.config['DEBUG'] = True #Only include while testing

@app.route('/')
def home_page():
    """The home page."""
    return render_template('home.html')

@app.route('/blog')
def blog_page():
    """The blog page."""
    return render_template('blog.html')

@app.route('/freetibet')
def freetibet_page():
    """Free Tibet page."""
    return render_template('freetibet.html')
@app.route('/cuisine')
def cuisine_page():
    """Tibetan cuisine page."""
    return render_template('cuisine.html')
@app.route('/momocrawl')
def momocrawl_page():
    """Momo crawl page."""
    return render_template('momocrawl.html')
@app.route('/business')
def business_page():
    """Business page."""
    return render_template('business.html')
@app.route('/forum')
def forum_page():
    """Forum page."""
    return render_template('forum.html')
@app.route('/search', methods=["GET", "POST"])
def search():
    if request.method == "POST":
        url = "https://api.github.com/search/repositories?q=" + request.form["user_search"]
        response_dict = requests.get(url).json()
        return render_template("results.html", api_data=response_dict)
    else: #request.method =="GET"
        return render_template("search.html")

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, this page was not found.", 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
