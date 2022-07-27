from ast import arg
from stuff.brain import *
from flask import request, make_response, jsonify, redirect, render_template, flash, get_flashed_messages
from stuff import app, db
from stuff.models import Bin

@app.route('/')
def stuff():
	return render_template("home.html")

@app.route('/404')
def error():
	return render_template("404.html")

@app.route('/done', methods=["GET", "POST"])
def done():
	content = request.form.get("content")
	author = request.form.get("author")
	password = request.form.get("password")
	content_info = creation_engine(author, password, content)
	return render_template("done.html", content_info=content_info, tinyurl=tinyurl(f'https://noobshare.herokuapp.com/stuff/{content_info["hash"]}'))

@app.route('/msg/<hash>', methods=["POST"])
def msg_check(hash):
	content_info = get_og(hash)
	if content_info == "No Such Stuff":
		return redirect('/404')
	else:
		password = request.form.get("password_check")
		if password == content_info.password:
			return render_template("msg.html", content_info=content_info, tinyurl=tinyurl(f'https://noobshare.herokuapp.com/stuff/{content_info.hash}'))
		else:
			return redirect(f'/stuff/{hash}')


@app.route('/stuff/<hash>', methods=["GET", "POST"])
def stuff_123(hash):
	password = get_og(hash)
	if password == "No Such Stuff":
		return redirect('/404')
	else:
		return render_template("password.html", hash=hash, ran_quote=ran_quote())

@app.route('/about')
def about():
    code_content = "# POST API for NoobShare\n\nimport requests\nrequest_url = 'https://noobshare.herokuapp.com/api'\ndata = {'author': 'author_name', 'content': 'content', 'password': 'password'}\n# returns {'author': 'author_name', 'content': 'content', 'password': 'password' , 'hash': 'tw28dekl', 'time':  '16:32:46 2022-01-27'}\n\n# GET API\n\nrequest_url = 'https://noobshare.herokuapp.com/get/(hash)/(password)'\n# returns {'author': 'author_name', 'content': 'content', 'password': 'password' , 'hash': 'tw28dekl', 'time':  '16:32:46 2022-01-27'}"
    return render_template("about.html", ran_fact=ran_fact(), code_content=code_content)

@app.route('/license')
def license():
	return render_template("license.html")

@app.route('/github')
def github():
	return redirect("https://github.com/newtoallofthis123/noobshare")

@app.route('/api', methods=["GET", "POST"])
def api():
	if request.method == "POST":
		author = request.values.get("author")
		content = request.values.get("content")
		password = request.values.get("password")
		content_info = jsonify(creation_engine(author, password, content))
		return content_info
	else:
		return redirect("/about#api")

@app.route('/get/<hash>/<password>', methods=["GET", "POST"])
def get(hash, password):
	query = hash
	content = get_og(query)
	if content == "No Such Stuff":
		return f'Sorry No SharedStuff with hash: {query}'
	else:
		if password == content.password:
			content_dict = {
			"author": content.author,
			"hash": content.hash,
			"content": content.content,
			"time": content.time
			}
			return jsonify(content_dict)
		else:
			return f'Sorry Wrong Password: {password} for hash: {query}'