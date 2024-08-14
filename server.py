import flask;


app = flask.Flask("alfred yagni");


def read_file(path:str)->str:
	with open(path, "r") as f1:
		return f1.read();



@app.route("/main")
def hh_main():
	global_style:str = "<style>"+read_file("./static/global_style.css")+"</style>"
	pre_script:str = read_file("./static/pre_scripts.js");
	post_scripts:str = read_file("./static/post_scripts.js");
	main_html:str = read_file("./main.html");
	return global_style + pre_script + main_html + post_scripts;


