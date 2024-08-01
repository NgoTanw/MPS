function openNav(){
	document.getElementById("menu_panel").style.display = "block";
	document.getElementById("menu_btn").style.display = "none";
	document.getElementById("close_btn").style.display = "block";
}
function closeNav(){
	document.getElementById("menu_panel").style.display = "none";
	document.getElementById("menu_btn").style.display = "block";
}


var x = document.getElementById("user")
var y = document.getElementById("vendor")
var z = document.getElementById("btn")

function vendor(){
	x.style.left = "-720px";
	y.style.left = "50px";
	z.style.left = "150px";
}

function user(){
	x.style.left = "50px";
	y.style.left = "770px";
	z.style.left = "0px";
}

function usertab(){
	document.getElementById("usertab").style.background = "linear-gradient(to top, #1e90ff, #1effff)";
	document.getElementById("keytab").style.background = "radial-gradient(white, lightgrey)";
}

function keytab(){
	document.getElementById("usertab").style.background = "radial-gradient(white, lightgrey)";
	document.getElementById("keytab").style.background = "linear-gradient(to top, #1e90ff, #1effff)";
}

$('.mydatatable').DataTable();

function copyPvtKey(r) {
	/* Get the text field */
	var copyText = document.getElementById("pvtkey").row[r];

	/* Select the text field */
	copyText.select();
	copyText.setSelectionRange(0, 99999); /*For mobile devices*/

	/* Copy the text inside the text field */
	document.execCommand("copy");

	/* Alert the copied text */
	alert("Private Key Copied");
}

function copyBinKey() {
	/* Get the text field */
	var copyText = document.getElementById("binary");

	/* Select the text field */
	copyText.select();
	copyText.setSelectionRange(0, 99999); /*For mobile devices*/

	/* Copy the text inside the text field */
	document.execCommand("copy");

	/* Alert the copied text */
	alert("Binary Key Copied");
}