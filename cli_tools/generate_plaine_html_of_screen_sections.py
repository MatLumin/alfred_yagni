from datauri import DataURI;
data:bytes = None;

with open("./static/iran/milad-tower.jpg", "rb") as f1:
	data = f1.read();


made = DataURI.make("image/jpeg", base64=True, data=data);

print(main);