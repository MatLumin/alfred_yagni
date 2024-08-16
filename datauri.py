import base64;
import mimetypes;
import os;
import sys;



def file_to_data_uri(path):
	if os.path.exists(path) == False:
		raise Exception(f"FILE NOT FOUND AT {path}");


	mime, uv = mimetypes.guess_type(path);

	with open(path, "rb") as f1:
		data = f1.read();
		encoded = base64.b64encode(data).decode().splitlines();
		data64 = "".join(encoded);
		return "data:%s;base64,%s" % (mime, data64);




