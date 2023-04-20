from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

story_instance = None

@app.get("/")
def index():
    """return prompt of madlibs"""

    prompts = excited_story.prompts

    return render_template("questions.html",prompts=prompts)

@app.get("/results")
def result():
    """return story"""

    story = excited_story.get_result_text(request.args)

    return render_template("results.html",results = story)