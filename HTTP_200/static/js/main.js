$(document).ready(function () {

	$("#search_full").click(function(){
		$("#full_text_search").submit();
	})


	$("body").css({
		'overflow-y':'hidden'
	})
	$(".loader-container").fadeIn();
	$(window).load(function  () {
		$(".loader-container").delay(1000).fadeOut();
		setTimeout(function(){
			$("body").css({
				'overflow-y':'scroll'
			})
		},1000)
		
	})


	$(".left-nav-inner ul li").click(function () {
		$(this).addClass("active").siblings().removeClass("active");
		$(this).find("span").addClass("active_number");
		$(this).siblings().find("span").removeClass("active_number");
	})


	$(window).scroll(function () {

		if ($(window).scrollTop() > 35) {

			if ($(window).outerWidth() >= 780) {
				$(".sub-header").css({
					'position': 'fixed',
					'width': 'calc(100% - 220px)',
					'z-index': '1',
					'top': '0px'
				})
				$(".relevant-content-head ").css({
					'position': 'fixed',
					'width': 'calc(100% - 220px)',
					'z-index': '1',
					'top': '60px',
					'box-shadow': '1px 1px 2px #9d9d9d'
				})
				$(".relevant-content").css({
					'margin-top': '100px'
				})
			} else {
				$(".sub-header").css({
					'position': 'fixed',
					'width': '100%',
					'z-index': '1',
					'top': '0px'
				})
				$(".relevant-content-head ").css({
					'position': 'fixed',
					'width': '100%',
					'z-index': '1',
					'top': '60px',
					'box-shadow': '1px 1px 2px #9d9d9d'
				})
				$(".relevant-content").css({
					'margin-top': '100px'
				})
			}
		} else {
			$(".sub-header").css({
				'position': 'relative',
				'width': '100%'

			})
			$(".relevant-content-head ").css({
				'position': 'relative',
				'width': '100%',
				'top': '0px',
				'box-shadow': '0px 0px 0px #9d9d9d'
			})
			$(".relevant-content").css({
				'margin-top': '0px'
			})
		}

		
	})


	var i = 0;

	$(".relevant-content ul li:nth-child(2n)").addClass('white');
	$(".relevant-content ul li:nth-child(2n+1)").addClass('grey');

	$(".imp i").mouseenter(function () {
		$(this).css({
			'color': '#252525'
		})
	})
	$(".imp i").mouseleave(function () {
		$(this).css({
			'color': '#9d9d9d'
		})
	})
	$(".imp i").click(function () {
		if ($(this).parent().hasClass("active_star")) {
			var id = $(this).attr('id');
			console.log(id.slice(9));
			removeBookmark(id.slice(9));
			$(this).parent().removeClass("active_star");

		} else {
			var id = $(this).attr('id');
			addBookmark(id.slice(9));
			console.log(id.slice(9));
			$(this).parent().addClass("active_star");

		}

	})

	// info-display page======

	$(".relevant-info").hide();


	$(".sec,.preview,.modal-index").click(function () {
		var login_status = $('#login_status').val();
		console.log(login_status);

		if(login_status=='0'){
			location.href = "/notices/"
		}

		else {

			location.hash = "details";

			$(".relevant-info").hide().fadeIn();
			var index = $(".relevant-content ul li").index(this);
			var id = $(this).attr('id');
			console.log('the id is '+id);
			var description = $("#notice_description_"+id).text();
			console.log("This:"+description);
			var title = $("#notice_title_"+id).text();
			var modified = $("#notice_modified_"+id).text();
			var faculty = $("#notice_faculty_"+id).text();
			var file_attached = $("#notice_file_attached_"+id).val();
			if (typeof file_attached == "undefined") {
				$("#notice_download_attachment").hide();
			}
			else {
				$("#notice_download_attachment").show();
				$("a#download_attachment").prop("href", file_attached);
			}
			$("#notice_description").html(description);
			$("#notice_title").html(title);
			$("#notice_posted_by").html("Posted By "+faculty+" "+modified);

			$("body").css({
				'overflow': 'hidden'
			})
		}
	})



	


	$(".relevant-info .cross").click(function () {
		$(".relevant-info").fadeOut("fast");
		$("body").css({
			'overflow-y': 'scroll'
		})
	})


	// checking click event on list====

	$(".relevant-content ul li").click(function () {
		$(this).addClass("click-list").siblings().removeClass("click-list");

	})

	// mobile navigation
	$(".dot-menu-links").hide();

	var sidenav_width=$(".dot-menu-links").outerWidth()+50;
	$(".dot-menu-links").css({
		'right':-sidenav_width
	})


	$(".overlay-dark,.overlay-dark-mob").hide();
	if($(window).width()<=950){

		$(".search2").click(function(){

			$(".left-nav").css({
				'margin-left':'-250px',
				'z-index':'2'
			})

			$(".overlay-dark,.overlay-dark-mob").fadeOut();
			$(".dot-menu-links").css({
				'right':-$(".dot-menu-links").outerWidth()-50
			});

			$(".dot-menu-links").hide();

			$(".search-container").fadeIn();
			$("body").css({

				"overflow-y":"hidden "
			})

		})

		$(".mobile-menu,.index-bars").click(function(){
			$(".left-nav").css({
				'margin-left':'0px',
				'z-index':'2'
			})
			$(".overlay-dark").fadeIn();
			$("body").css({
				'overflow':'hidden'
			})
		})
		$(".mob-side-link").click(function(){

			$(".overlay-dark-mob").fadeIn();
			$(".dot-menu-links").show();
			setTimeout(function(){
				$(".dot-menu-links").css({
					'right':'0'
				});
			},1);
			$("body").css({
				'overflow':'hidden'
			})



		})

	// cross-mobile

	$(".cross-mobile,.overlay-dark,.overlay-dark-mob,.move-in,.dot-menu-links ul li").click(function(){
		$(".left-nav").css({
			'margin-left':'-250px',
			'z-index':'2'
		})
		$("body").css({
			'overflow-y':'scroll'
		})
		$(".overlay-dark,.overlay-dark-mob").fadeOut();
		$(".dot-menu-links").css({
			'right':-$(".dot-menu-links").outerWidth()-50
		});

		$(".dot-menu-links").hide();
	})

}





	// responsive list in mobile
	var win_width=$(window).width();

	if(win_width<=640){
		
		
		$(".relevant-content ul li .post_head").removeClass("sm-col-8").addClass("sm-col-12");
	}
	if(win_width<=940){
		$(".heading-small").removeClass("sm-col-4").addClass("sm-col-8");
		$(".head-links-resize").removeClass("sm-col-8").addClass("sm-col-4");
	}



// landing page scripting=================

// $(".login-container").fadeOut();


$(".login-click").click(function(){

	$(".login-container").fadeIn();
	$("body").css({
		"overflow":"hidden"
	})

})


$(".cross,.login-overlay").click(function(){

	$(".search-container").fadeOut();
	$("body").css({
		"overflow-y":"scroll"
	})

})


$(".search-container").hide();
$(".search2").click(function(){

	
	$(".search-container").fadeIn();
	$("body").css({

		"overflow-y":"hidden "
	})
	
})


var i,j;
for(i=1;i<=31;i++){
	$("#date-id").append("<option>"+i+"</option>");
	$("#date-id2").append("<option>"+i+"</option>");
}
for(j=1;j<=12;j++){
	$("#month-id").append("<option>"+j+"</option>");
	$("#month-id2").append("<option>"+j+"</option>");
}


setInterval(function(){
	if($("#year option:selected").text()=="Year" ) { 

		
		$("#year").css({
			'color':'#9d9d9d'
		})
	}
	else  { 
		$("#year").css({
			'color':'#000'
		})

	}
	if($("#year2 option:selected").text()=="Year" ) { 

		
		$("#year2").css({
			'color':'#9d9d9d'
		})
	}
	else  { 
		$("#year2").css({
			'color':'#000'
		})

	}


	if($("#date-id option:selected").text()=="Date" ) { 

		
		$("#date-id").css({
			'color':'#9d9d9d'
		})
	}
	else  { 
		$("#date-id").css({
			'color':'#000'
		})

	}
	if($("#date-id2 option:selected").text()=="Date" ) { 

		
		$("#date-id2").css({
			'color':'#9d9d9d'
		})
	}
	else  { 
		$("#date-id2").css({
			'color':'#000'
		})

	}

	if($("#month-id option:selected").text()=="Month" ) { 


		
		$("#month-id").css({
			'color':'#9d9d9d'
		})
	}
	else  { 
		$("#month-id").css({
			'color':'#000'
		})

	}
	if($("#month-id2 option:selected").text()=="Month" ) { 


		
		$("#month-id2").css({
			'color':'#9d9d9d'
		})
	}
	else  { 
		$("#month-id2").css({
			'color':'#000'
		})

	}

	if($("#batch-id option:selected").text()=="Batch" ) { 


		
		$("#batch-id").css({
			'color':'#9d9d9d'
		})
	}
	else  { 
		$("#batch-id").css({
			'color':'#000'
		})

	}
	if($("#branch-id option:selected").text()=="Branch" ) { 


		
		$("#branch-id ").css({
			'color':'#9d9d9d'
		})
	}
	else  { 
		$("#branch-id ").css({
			'color':'#000'
		})

	}
	if($("#section option:selected").text()=="Section" ) { 


		
		$("#section").css({
			'color':'#9d9d9d'
		})
	}
	else  { 
		$("#section").css({
			'color':'#000'
		})

	}


})




// usingescapen butto  to minimize the notice page===



$(document).keyup(function(e) {

	if (e.keyCode === 27){

		$(".relevant-info, .search-container").fadeOut("fast");
		$("body").css({
			'overflow-y': 'scroll'
		})

	}   
});



// add search validation data here==========

$("#branch-id").change(function(){
	var val=$(this).val();

// change data here================

switch(val){
	case "BTECH CSE":
	$("#section").html("<option>CS-1</option><option>CS-2</option>");
	break;
	case "BTECH ECE":
	$("#section").html("<option>ECE-1</option><option>ECE-2</option>");
	break;
	case "BTECH EEE":
	$("#section").html("<option>EEE-1</option><option>EEE-2</option>");
	break;
	case "BTECH ME":
	$("#section").html("<option>ME-1</option><option>ME-2</option>");
	break;
	case "BTECH CE":
	$("#section").html("<option>CE-1</option><option>CE-2</option>");
	break;

}

})


$(".reset").click(function(){
	$("#section").html("<option value='' disabled selected hiddened>Section</option>");
})


// edit to save button=========================================

$(".edit-save,.edit-save-2,.show-icon,i.mob-save").hide();

$(".edit-save,.edit-save-2,i.mob-save").click(function(){
	$(".profile-form form").submit();
	$(".profile-form .edit-input").prop('disabled',true);

	// $(".show-icon").fadeOut();


})
$(".edit-click,i.mob-edit").click(function(){

	if($(window).width()<780){
		$(".edit-save-2").hide();
		$("i.mob-save").fadeIn("fast");
	}
	else{
		$(".edit-save-2").fadeIn();
		$("i.mob-save").hide();
	}

	$(".edit-click,i.mob-edit").hide();
	$(".edit-save").fadeIn("fast");

	$(".profile-form .edit-input").prop('disabled',false);
	$(".profile-form .edit-input").css({
		'border-bottom':'1px solid #e6c115',
		'color':'#9d9d9d'
	})
	$(".profile-form h2").css({
		'color':'#4d4d4d'
	})
	$(".show-icon").fadeIn();


})


// create notice validation script===================

var tag_value,c="";

var course_val=$("#create-course option:selected").text(),
branch_val=$("#create-branch option:selected").text(),
year_val=$("#create-year option:selected").text(),
section_val=$("#create-section option:selected").text();





tag_value=course_val + '-' + branch_val + '-' + year_val +'-' + section_val;

$("#create-course").change(function  () {
	course_val=$(this).val()

	switch(course_val){
		case "All Courses":
		$("#create-branch").html("<option selected>All Branches</option><option>CSE</option><option>IT</option><option>ECE</option><option>EE</option><option>EEE</option><option>CE</option><option>IC</option><option>MT</option><option>ME</option>")
		$("#create-year").html("<option selected>All Years</option><option >1</option><option >2</option><option >3</option><option >4</option>")
		$("#create-section").html("<option selected>All Sections</option><option>CS1</option><option>CS2</option><option>IT1</option><option>IT2</option><option>ECE1</option><option>ECE2</option><option>EE1</option><option>EE2</option><option>CE1</option><option>CE2</option><option>IC1</option><option>IC2</option><option>MT1</option><option>MT2</option><option>ME1</option><option>ME2</option>");
		break;
		case "BTech":
		$("#create-branch").html("<option selected>All Branches</option><option>CSE</option><option>IT</option><option>ECE</option><option>EE</option><option>EEE</option><option>CE</option><option>IC</option><option>MT</option><option>ME</option>")
		$("#create-year").html("<option selected>All Years</option><option >1</option><option >2</option><option >3</option><option >4</option>")
		$("#create-section").html("<option selected>All Sections</option><option>CS1</option><option>CS2</option><option>IT1</option><option>IT2</option><option>ECE1</option><option>ECE2</option><option>EE1</option><option>EE2</option><option>CE1</option><option>CE2</option><option>IC1</option><option>IC2</option><option>MT1</option><option>MT2</option><option>ME1</option><option>ME2</option>");
		break;
		case "MTech":
		$("#create-branch").html("<option selected>All Branches</option><option>CSE</option><option>IT</option>")
		$("#create-year").html("<option selected>All Years</option><option >1</option><option >2</option>")
		$("#create-section").html("<option selected>All Sections</option>");
		break;
		case "MCA":
		$("#create-branch").html("<option selected>All Branches</option>");
		$("#create-year").html("<option selected>All Years</option><option >1</option><option >2</option>")
		$("#create-section").html("<option selected>All Sections</option>");
		break;
		case "MBA":
		$("#create-branch").html("<option selected>All Branches</option>");
		$("#create-year").html("<option selected>All Years</option><option >1</option><option >2</option>")
		$("#create-section").html("<option selected>All Sections</option>");
		break;
	}
	

})
$("#create-year").change(function  () {
	year_val=$(this).val();


})

$("#create-branch").change(function  () {
	branch_val=$(this).val();
	switch(branch_val){
		case "All Branches":
		$("#create-year").html("<option selected>All Years</option><option >1</option><option >2</option><option >3</option><option >4</option>")
		$("#create-section").html("<option selected>All Sections</option><option>CSE1</option><option>CSE2</option><option>IT1</option><option>IT2</option><option>ECE1</option><option>ECE2</option><option>EE1</option><option>EE2</option><option>CE1</option><option>CE2</option><option>IC1</option><option>IC2</option><option>MT1</option><option>MT2</option><option>ME1</option><option>ME2</option>");
		break;
		case "CSE":
		$("#create-year").html("<option selected>All Years</option><option >1</option><option >2</option><option >3</option><option >4</option>")
		$("#create-section").html("<option selected>All Sections</option><option >CSE1</option><option>CSE2</option>");
			// $("#create-course").html("<option selected>All Courses</option><option >BTech</option><option >MTech</option>");
			break;
			case "IT":
			$("#create-year").html("<option selected>All Years</option><option >1</option><option >2</option><option >3</option><option >4</option>")
			$("#create-section").html("<option selected>All Sections</option><option >IT1</option><option>IT2</option>")
			// $("#create-course").html("<option selected>All Courses</option><option >BTech</option><option >MTech</option>");
			break;
			case "ECE":
			$("#create-year").html("<option selected>All Years</option><option >1</option><option >2</option><option >3</option><option >4</option>")
			$("#create-section").html("<option selected>All Sections</option><option >ECE1</option><option>ECE2</option>")
			// $("#create-course").html("<option selected>All Courses</option><option >BTech</option>");
			break;
			case "EE":
			$("#create-year").html("<option selected>All Years</option><option >1</option><option >2</option><option >3</option><option >4</option>")
			$("#create-section").html("<option selected>All Sections</option><option >EE1</option><option>EE2</option>")
			// $("#create-course").html("<option selected>All Courses</option><option >BTech</option>");
			break;
			case "CE":
			$("#create-year").html("<option selected>All Years</option><option >1</option><option >2</option><option >3</option><option >4</option>")
			$("#create-section").html("<option selected>All Sections</option><option >CE1</option><option>CE2</option>")
			// $("#create-course").html("<option selected>All Courses</option><option >BTech</option>");
			break;
			case "IC":
			$("#create-year").html("<option selected>All Years</option><option >1</option><option >2</option><option >3</option><option >4</option>")
			$("#create-section").html("<option selected>All Sections</option><option >IC1</option><option>IC2</option>")
			// $("#create-course").html("<option selected>All Courses</option><option >BTech</option>")
			break;
			case "MT":
			$("#create-year").html("<option selected>All Years</option><option >1</option><option >2</option><option >3</option><option >4</option>")
			$("#create-section").html("<option selected>All Sections</option><option >MT1</option><option>MT2</option>")
			// $("#create-course").html("<option selected>All Courses</option><option >BTech</option>")
			break;
			case "ME":
			$("#create-year").html("<option selected>All Years</option><option >1</option><option >2</option><option >3</option><option >4</option>")
			$("#create-section").html("<option selected>All Sections</option><option >ME1</option><option>ME2</option>")
			// $("#create-course").html("<option selected>All Courses</option><option >BTech</option>")
			break;
		}


	})
$("#create-section").change(function  () {
	section_val=$(this).val()
	

})


$(".create-warn-msg").hide();


$(".add").click(function () {
	
	

	if(course_val!="Course" && year_val!="Year" && branch_val!="Branch" && section_val!="Section"){


		course_val=$("#create-course option:selected").text(),
		branch_val=$("#create-branch option:selected").text(),
		year_val=$("#create-year option:selected").text(),
		section_val=$("#create-section option:selected").text();

		tag_value=course_val + '-' + branch_val + '-' + year_val +'-' + section_val;

		var tag_value_remove=tag_value.split(' ').join('');



		$("#tag-input").append("<li>"+tag_value+"&nbsp;&nbsp;&nbsp;<i class='fa fa-times'></i><input type='hidden' name='notice_for' value="+tag_value_remove+"></li>");

		$(".create-warn-msg").hide();
	}
	else{
		$(".create-warn-msg").hide().fadeIn("fast");
	}
})


// remove loader on click back button

$(window).bind('hashchange', function () {

	if (location.hash == null || location.hash == "") {
		$(".relevant-info").hide();
		$("body").css({
			'overflow-y':'scroll'
		})
	}

});

  // notice messages======
  setTimeout(function  () {
  	$(".notice-msg").animate({
  		'top':'20px',
  		'opacity':'1'
  	},700);
  },1000)


  var back_notice=function(){
  	$(".notice-msg").animate({
  		'top':'-20px',
  		'opacity':'0'
  	},700);
  }

  setTimeout(function(){
  	back_notice();

  },3000)

  $(".notice-msg-cross").click(function(){
  	back_notice();
  })

  $(".my-prompt-container").hide();

  $(".trash-notice").click(function() {
  	$(".my-prompt-container").fadeIn();
  })

  $(".no-delete").click(function() {
  	$(".my-prompt-container").fadeOut();
  })


// making footer down fixed

var stick_num=$(".form-hid input").val();
// var id=parseInt(stick_num);
var id=parseInt(stick_num);

(function sticky_footer () {

	if($(window).width()>=780 && id<=3){
		$("footer").css({
			'position':'fixed',
			'bottom':'0px',
			'width':'calc(100vw - 220px)'
		});
	}
	else{
		$("footer").css({
			'position':'relative',
			'width':'auto'
		});
	}

})();

$(".left-nav-inner ul .move-in,.button-create,.left-nav-inner ul .index-list").click(function  () {
	$("body").css({
		'opacity':'0'
	});
});


$(document).on('click', "#tag-input li i", function(){
	$(this).parent().remove();


	if($("#tag-input li").length>=1){
		$(".create-warn-msg").hide();
		enable_button();
	}else{
		$(".create-warn-msg").show();
		disable_button();
	}
})


var disable_button=function(){
	$(".create-notice-button").css({
		'opacity':'0.5',
		'cursor':'default'
	})
	$(".create-notice-button").mouseenter(function  () {
		$(this).css({
			'background':'#5d5473'
		});
	})
	$(".create-notice-button").mouseleave(function  () {
		$(this).css({
			'background':'#5d5473'
		});
	})

	$("#create-submit").prop("disabled",true);
}
var enable_button=function(){
	$(".create-notice-button").css({
		'opacity':'1',
		'cursor':'pointer'
	})
	$(".create-notice-button").mouseenter(function  () {
		$(this).css({
			'background':'#2D2251'
		})
	})
	$(".create-notice-button").mouseleave(function  () {
		$(this).css({
			'background':'#5d5473'
		})
	})
	
	$("#create-submit").prop("disabled",false);
}

$(".hidedata").css({
	'height':'0px',
	'transition':'all 0.2s ease-in-out',
	'overflow':'hidden'
});
$(".tag").css({
	'height':'0px',
	'transition':'all 0.2s ease-in-out',
	'overflow':'hidden'
});
$(".create-warn-msg").show();
disable_button();
$('.add').click(function(){
	if($("#tag-input li").length>=1){
		$(".create-warn-msg").hide();
		enable_button();
	}else{
		$(".create-warn-msg").show();
		disable_button();
	}
});


$("#entire").change(function(){
	if($(this).prop('checked')){
		$(".tag").css({
			'height':'auto',
			'transition':'all 0.2s ease-in-out',
			'overflow':'hidden'
		});
		$(".hidedata").css({
			'height':'90px',
			'transition':'all 0.2s ease-in-out',
			'overflow':'hidden'
		});
	}else{
		$(".create-warn-msg").fadeIn();
		disable_button();
		$(".hidedata").css({
			'height':'0px',
			'transition':'all 0.2s ease-in-out',
			'overflow':'hidden'
		});
		$(".tag").css({
			'height':'0px',
			'transition':'all 0.2s ease-in-out',
			'overflow':'hidden'
		});
	}
})

var should_enable_button = function(){
	if($("#fac").prop("checked") || $("#manage").prop("checked") || 
		$("#others").prop("checked") || $("#hod").prop("checked")){	
		enable_button();
		$(".create-warn-msg").fadeOut();
	}else{
		if(!$("#entire").prop('checked')){
			$(".create-warn-msg").fadeIn();
			disable_button();
		}
	}
};

$('#fac').click(function(){
	should_enable_button();
});

$('#manage').click(function(){
	should_enable_button();
});

$('#hod').click(function(){
	should_enable_button();
});

$('#others').click(function(){
	should_enable_button();
});

});


function ValidateBranch(){

  var course = document.getElementById("course").value;
  var branch = document.getElementById("branch").value;
  if (course == "BTECH" || course == "MTECH")
    {
      if (branch == "None")
      { 
        alert("Please Enter the Branch");
        return false;
      }
      else
        return true;
        alert("Please Enter the Branch")
        return false
      }
      else
        return true
    }
}
