from flask import request, Flask;
import os;
from typing import *;
import image_collection;


app = Flask("alfred yagni");

__dir__ = os.path.split(__file__)[0];

def read_file(path:str)->str:
	with open(path, "r") as f1:
		return f1.read();



#dont touch this ! =======================================================
@app.route("/main")
def hh_main():
	imports:str = read_file(f"{__dir__}/static/imports.html");
	global_style:str = "<style>"+read_file(f"{__dir__}/static/global_style.css")+"</style>"
	pre_script:str = "<script>"+read_file(f"{__dir__}/static/pre_scripts.js")+"</script>";
	post_scripts:str = "<script>"+read_file(f"{__dir__}/static/post_scripts.js")+"</script>";
	main_html:str = read_file(f"{__dir__}/main.html");
	return imports + global_style + pre_script + main_html + post_scripts;
#=========================================================================
def make_eout(is_ok:bool, err_msg:str, data:Any)->Dict[str,Any]:
	return {
		"is_ok":is_ok,
		"err_msg":err_msg,
		"data":data
	};



@app.route("/get_image_collection_data")
def hh_get_image_collection_data():
	given_uti = request.args.get("uti", None);
	if given_uti == None:
		return make_eout(False, "no uti was given", {});

	if given_uti not in image_collection.ALL_IMAGE_COLLECTIONS:
		return make_eout(False, "given uti was not found", {"given_uti":given_uti});


	data = image_collection.ALL_IMAGE_COLLECTIONS[given_uti].generate_dict();
	return make_eout(True, None, data);


