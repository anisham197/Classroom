var fab = document.getElementById('join_class_fab');
fab.onclick = function() {
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
