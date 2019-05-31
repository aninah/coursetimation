$(document).ready(function(){ 
	$("#class_submit").click(submit_classes);
});

function submit_classes() {
  $.post("/receive_classes", {class_str: $("#class_input")[0].value}, function(req, res) {
  	for (let i = 0; i < req.concentrations.length;i++) {
  		console.log(req.concentrations[i]);
  	}
  })
}