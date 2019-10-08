var result1="";
var result2="";		
var username="";
$(document).ready(function() {
	
	$("#move_right").click(function() {
		var perms_array=result1.split(",");
		for (var i=0;i<(perms_array.length-1);i++){
			if(perms_array[i]!=""){
				var perm_clone = $("#"+perms_array[i]).clone(true);
				$(perm_clone).removeClass('ui-selected');
				$("#"+perms_array[i]).remove();
				$("#sortable2").append(perm_clone);
				
			}
		}
		return;
	});
	
	$("#move_left").click(function() {
		var perms_array=result2.split(",");
		
		for (var i=0;i<(perms_array.length-1);i++){
			if(perms_array[i]!=""){
				var perm_clone = $("#"+perms_array[i]).clone(true);
				$(perm_clone).removeClass('ui-selected');
				$("#"+perms_array[i]).remove();
				$("#sortable1").append(perm_clone);

			}
		}
		return;
	});
	
});

 $(function() {

    $( "#sortable1" ).selectable({
        stop: function() {
            result1 = ""
            $( ".ui-selected", this ).each(function() {
                result1+=this.id+","
            });
        }
    });

    
    $( "#sortable2" ).selectable({
        stop: function() {
            result2 = ""
            $( ".ui-selected", this ).each(function() {
                result2+=this.id+","
            });
        }
    });
    
});

function UpdatePostOrder(url) { 

	var arr1 = [];
	var arr2 = [];
  	$("#sortable2 li").each(function(){
    	arr1.push($(this).attr('id'));
  	});
	
	$("#sortable1 li").each(function(){
    	arr2.push($(this).attr('id'));
  	});
  	
	
	var modulesOk=arr1.join(',');
	var modulesNok=arr2.join(',');
	
	var request = $.ajax({
			url: url,
			type: "POST",
			async: false,
			data: {modulesOk: modulesOk, modulesNok:modulesNok, username: username},
   	});
    			
	request.done(function(msg) {
		
		if (msg["message"]=='403'){
			alert("FORBIDDEN");
        	window.location.href ="/forbidden";
        	return
		}
		if (msg["message"]=='ok'){
			alert("Modules updated");			
		return;
		}
		if(msg["message"]=='error'){
			alert(msg["error_string"]);
			return;
		}		
	});
}