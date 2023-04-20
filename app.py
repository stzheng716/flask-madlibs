from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def index():
    """return prompt of madlids"""


    prompt = silly_story.prompts

    return render_template("questions.html",words=prompt)#naming

@app.get("/results")
def result():
    """return re"""

    story = silly_story.get_result_text(request.args)



    return render_template("results.html",results = story)