function displayDialog() {
	var uploadFileDialog = document.getElementById('upload_file_dialog');


    //document.getElementById("class_code").innerHTML=code;
	if (! uploadFileDialog.showModal) {
		dialogPolyfill.registerDialog(uploadFileDialog);
	}
	uploadFileDialog.showModal();

	uploadFileDialog.querySelector('.cancel').addEventListener('click', function() {
		uploadFileDialog.close();
	});

}
var button = document.getElementById('upload');
button.onclick = displayDialog ;
