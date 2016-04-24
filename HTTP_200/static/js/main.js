$(document).ready(function () {

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

		// if ($(window).scrollTop() > 20){
		// 	$(".dot-menu-links").css({
		// 		'position':'fixed',
		// 		'margin-top':'0px'
		// 	})
		// }
		// else{
		// 	$(".dot-menu-links").css({
		// 		'position':'absolute',
		// 		'margin-top':'20px'
		// 	})
		// }
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
			$(this).parent().removeClass("active_star");

		} else {
			$(this).parent().addClass("active_star");

		}

	})

	// info-display page======

	$(".relevant-info").hide();

	$(".sec").click(function () {
		var index = $(".relevant-content ul li").index(this);

		$(".relevant-info ").hide().fadeIn();

		$("body").css({
			'overflow': 'hidden'
		})
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
	if($(window).width()<=780){

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
	





	// $(".dot-menu-links").click(function(){
	// 	$(this).fadeOut();
		
	// })

	// responsive list in mobile
	var win_width=$(window).width();

	if(win_width<=640){
		$(".head-links-resize").removeClass("sm-col-8").addClass("sm-col-2");
		$(".heading-small").removeClass("sm-col-4").addClass("sm-col-8");
	$(".relevant-content ul li .post_head").removeClass("sm-col-8").addClass("sm-col-12");
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
  	
		$(".relevant-info").fadeOut("fast");
		$("body").css({
			'overflow-y': 'scroll'
		})
	
  }   // esc
});

// validation for search box===========

var val_branch=$("#branch-id option:selected").text();


setInterval(function(){
	val_branch= $("#branch-id option:selected").text();
},0);



setInterval(function(){

	
switch(val_branch){
	case "BTECH CSE":
		$("#section").html("<option val='' disabled selected hiddened>Section</option><option>CS-1</option><option>CS-2</option>");
		break;
	
}


},0);

});
