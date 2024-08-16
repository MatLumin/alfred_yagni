
from __future__ import annotations;
from typing import *;
from datauri import file_to_data_uri;


ALL_IMAGE_COLLECTIONS:Dict[str:ImageCollection] = dict();
__dir__ = os.path.split(__file__)[0];

class ImageCollection:
	def __init__(self, uti, images:List[Image]):
		self.uti = uti
		self.images = images;
		ALL_IMAGE_COLLECTIONS[uti] = self;


	def generate_dict(self):
		images = [];
		for i1 in self.images:
			images.append(i1.generate_dict());
		return {
		"uti":self.uti,
		"images":images
		}




class Image:
	def __init__(self, uti, title, path):
		self.uti = uti;
		self.title = title;
		self.path = __dir__+"/"+path;

	def generate_path(self, path):
		return "./static/" + self.path;


	def generate_data_uri(self):
		return file_to_data_uri(self.path);


	def generate_dict(self)->Dict[str,Any]:
		return {
			"uti":self.uti,
			"title":self.title,
			"path":self.path,
			"data":self.generate_data_uri(),
		}





#definitions===========================================
arazi:ImageCollection = ImageCollection(
	"arazi",
	[
	Image(
		"gonbad_mina",
		"گنبد مینا",
		r"static\image_collections\arazi\gonbad mina.jpg",
		),
	Image(
		"milad_tower",
		"پل ظبعیت ",
		r"static\image_collections\arazi\Pol Tabiat .jpg",
		),
	Image(
		"book_garden",
		"باغ کتاب",
		r"static\image_collections\arazi\TEHRAN-BOOK-GARDEN.jpg",
		),
	]
	);








iran:ImageCollection = ImageCollection(
	"iran",
	[
	Image(
		"33_pol",
		"سی و سه پل",
		r"static\image_collections\Iran\33 pol .jpg",
		),
	Image(
		"azadi_tower",
		"برج ازادی",
		r"static\image_collections\Iran\Azadi-Tower.jpg",
		),
	Image(
		"book_garden",
		"برج میلاد",
		r"static\image_collections\Iran\milad-tower.jpg",
		),
	Image(
		"takht_jamshid",
		"تخت جمشید",
		r"static\image_collections\Iran\takhtjamshid.jpg",
		),
	]
	);





foreign:ImageCollection = ImageCollection(
	"foreign",
	[
	Image(
		"eifel_tower",
		"ایفل",
		r"static\image_collections\World\eafel tower .jpg",
		),
	Image(
		"khalifa",
		"برج خلیفه",
		r"static\image_collections\World\khalifa tower.jpeg",
		),
	Image(
		"rome_arena",
		"کلوسعوم",
		r"static\image_collections\World\rome.jpg",
		),
	]
	)