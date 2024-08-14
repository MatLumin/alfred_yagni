import flask;
import os;

app = flask.Flask("alfred yagni");

__dir__ = os.path.split(__file__)[0];

def read_file(path:str)->str:
	with open(path, "r") as f1:
		return f1.read();



@app.route("/main")
def hh_main():
	global_style:str = "<style>"+read_file(f"{__dir__}/static/global_style.css")+"</style>"
	pre_script:str = read_file(f"{__dir__}/static/pre_scripts.js");
	post_scripts:str = read_file(f"{__dir__}/static/post_scripts.js");
	main_html:str = read_file(f"{__dir__}/main.html");
	return global_style + pre_script + main_html + post_scripts;


