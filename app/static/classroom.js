function displayDialog() {
	var joinClassDialog = document.getElementById('join_class_dialog');


    //document.getElementById("class_code").innerHTML=code;
	if (! joinClassDialog.showModal) {
		dialogPolyfill.registerDialog(joinClassDialog);
	}
	joinClassDialog.showModal();

	joinClassDialog.querySelector('.cancel').addEventListener('click', function() {
		joinClassDialog.close();
	});

}
var fab = document.getElementById('join_class_fab');
fab.onclick = displayDialog ;

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function displayMenu() {
    document.getElementById("fabDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('#add_class_fab')) {

    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
