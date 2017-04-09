var fab = document.getElementById('add_class_fab');
fab.onclick = function() {
	var createClassDialog = document.getElementById('create_class_dialog');

    //document.getElementById("class_code").innerHTML=code;
	if (! createClassDialog.showModal) {
		dialogPolyfill.registerDialog(createClassDialog);
	}
	createClassDialog.showModal();

	createClassDialog.querySelector('.cancel').addEventListener('click', function() {
		createClassDialog.close();
	});

}
