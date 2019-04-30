function makeSelect(value='') {
	var myDiv = document.getElementById('year');
	var d = new Date();
	var y = d.getFullYear() + 4;
	var array = [];
	//Create array of options to be added
	for (var i = y; i > 1875; i--) {
		array.push(i)
	}
	//Create and append select list
	var selectList = document.createElement("select");
	selectList.setAttribute("name", "year");
	myDiv.appendChild(selectList);

	var option = document.createElement("option");
	option.setAttribute("value", ' -- select -- ');
	option.text = '';
	option.selected = true;
	option.disabled = true;
	selectList.appendChild(option);

	//Create and append the options
	for (var i = 0; i < array.length; i++) {
	    var option = document.createElement("option");
	    option.setAttribute("value", array[i]);
	    option.text = array[i];
	    selectList.appendChild(option);
	}
	selectList.value = value;
}

// function moreFacts() {
//     var container = document.getElementById("container");
//     container.appendChild(document.createTextNode("Fact: "));
//     var input = document.createElement("input");
//     input.type = "text";
//     input.class = "form-control";
//     input.id = "facts";
//     input.name = "facts";
//     container.appendChild(input);

//     var checkbox = document.createElement('input');
// 	checkbox.type = "checkbox";
// 	checkbox.name = "name";
// 	checkbox.class = "form-control";
// 	checkbox.value = "value";
// 	checkbox.id = "id";

// 	var label = document.createElement('label')
// 	label.htmlFor = "id";
// 	label.appendChild(document.createTextNode('Show on display'));

// 	container.appendChild(checkbox);
// 	container.appendChild(label);

//     container.appendChild(document.createElement("br"));
// }

// window.onload = makeSelect;
