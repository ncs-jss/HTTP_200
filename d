[1mdiff --git a/HTTP_200/settings.py b/HTTP_200/settings.py[m
[1mindex 0207c36..85942ae 100644[m
[1m--- a/HTTP_200/settings.py[m
[1m+++ b/HTTP_200/settings.py[m
[36m@@ -105,24 +105,24 @@[m [mWSGI_APPLICATION = 'HTTP_200.wsgi.application'[m
 # Database[m
 # https://docs.djangoproject.com/en/1.8/ref/settings/#databases[m
 [m
[31m-# DATABASES = {[m
[31m-#    'default': {[m
[31m-#        'ENGINE': 'django.db.backends.sqlite3',[m
[31m-#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),[m
[31m-#    }[m
[31m-# }[m
[31m-[m
 DATABASES = {[m
[31m-    'default': {[m
[31m-        'ENGINE': 'django.db.backends.mysql', [m
[31m-        'NAME': config_keys.DATABASE_NAME,[m
[31m-        'USER': config_keys.MYSQL_USERNAME,[m
[31m-        'PASSWORD': config_keys.MYSQL_PASSWORD,[m
[31m-        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on[m
[31m-        'PORT': '3306',[m
[31m-    }[m
[32m+[m[32m   'default': {[m
[32m+[m[32m       'ENGINE': 'django.db.backends.sqlite3',[m
[32m+[m[32m       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),[m
[32m+[m[32m   }[m
 }[m
 [m
[32m+[m[32m# DATABASES = {[m
[32m+[m[32m#     'default': {[m
[32m+[m[32m#         'ENGINE': 'django.db.backends.mysql',[m[41m [m
[32m+[m[32m#         'NAME': config_keys.DATABASE_NAME,[m
[32m+[m[32m#         'USER': config_keys.MYSQL_USERNAME,[m
[32m+[m[32m#         'PASSWORD': config_keys.MYSQL_PASSWORD,[m
[32m+[m[32m#         'HOST': 'localhost',   # Or an IP Address that your DB is hosted on[m
[32m+[m[32m#         'PORT': '3306',[m
[32m+[m[32m#     }[m
[32m+[m[32m# }[m
[32m+[m
 # Internationalization[m
 # https://docs.djangoproject.com/en/1.8/topics/i18n/[m
 [m
[36m@@ -222,7 +222,7 @@[m [mACCOUNT_EMAIL_VERIFICATION = "none"[m
 ACCOUNT_LOGOUT_ON_GET = True[m
 [m
 STATIC_URL = '/static/'[m
[31m-STATIC_ROOT = os.path.join(APP_DIR, 'static')[m
[32m+[m[32m# STATIC_ROOT = os.path.join(APP_DIR, 'static')[m
 [m
 STATICFILES_DIRS = ([m
     os.path.join(APP_DIR, 'static'),[m
[1mdiff --git a/HTTP_200/static/css/main.css b/HTTP_200/static/css/main.css[m
[1mindex 3cd9c59..6cf1acb 100644[m
[1m--- a/HTTP_200/static/css/main.css[m
[1m+++ b/HTTP_200/static/css/main.css[m
[36m@@ -677,12 +677,19 @@[m [mfooter h4{[m
 	transition:all 0.2s ease-in-out;[m
 [m
 }[m
[32m+[m[32m.bold-light{[m
[32m+[m	[32mcolor: #4d4d4d;[m
[32m+[m	[32mfont-family: 'Roboto Medium'[m
[32m+[m[32m}[m
[32m+[m[32m.index-author{[m
[32m+[m	[32mcolor: #9d9d9d;[m
[32m+[m[32m}[m
 .pad-list a:hover{[m
 	background: #ddd;[m
 	[m
 }[m
 .date-index{[m
[31m-	text-align: center;[m
[32m+[m	[32mtext-align: left;[m
 	color: #9d9d9d;[m
 	font-family: 'Roboto Medium';[m
 	transition:all 0.2s ease-in-out;[m
[36m@@ -763,7 +770,7 @@[m [mfooter h4{[m
 	color: #E6C115;[m
 }[m
 .auth-index{[m
[31m-		text-align: center;[m
[32m+[m		[32mtext-align: left;[m
 [m
 }[m
 .left-nav-inner-index{[m
[36m@@ -1076,13 +1083,142 @@[m [mbutton.no-delete:hover{[m
 	background: #403469;[m
 	border: 2px solid #403469;[m
 }[m
[32m+[m[32m.about-container{[m
[32m+[m	[32mpadding: 0px 70px 20px 70px;[m
[32m+[m	[32mcolor: #4d4d4d;[m
[32m+[m	[32mfont-family: 'Roboto';[m
[32m+[m	[32mline-height: 19px;[m
[32m+[m[32m}[m
[32m+[m[32m/*contact us====================*/[m
 [m
[31m-.empty-notices {[m
[32m+[m[32m.contact-container{[m
 	text-align: center;[m
[31m-	font-family: 'Roboto Medium';[m
[31m-	color: #4D4D4D;[m
 }[m
[32m+[m[32m.contact-container h3{[m
[32m+[m	[32mfont-size: 1em;[m
[32m+[m[32m}[m
[32m+[m[32m.contact-container form{[m
[32m+[m	[32mwidth: 500px;[m
[32m+[m	[32mpadding-top: 40px;[m
[32m+[m	[32mtext-align: center;[m
[32m+[m	[32mmargin-right: auto;[m
[32m+[m	[32mmargin-left: auto;[m
[32m+[m	[32mmargin-bottom: 40px;[m
[32m+[m[32m}[m
[32m+[m[32m.contact-container form textarea{[m
[32m+[m	[32mheight: 100px;[m
[32m+[m[32m}[m
[32m+[m[32m.contact-container form input{[m
[32m+[m	[32mmargin-top: 0px;[m
[32m+[m	[32mcolor: #252525;[m
[32m+[m[32m}[m
[32m+[m[32m.reset-contact,.submit-contact{[m
[32m+[m	[32mdisplay: inline;[m
[32m+[m	[32mpadding: 10px 17px;[m
[32m+[m	[32mbackground: #403469;[m
[32m+[m	[32mborder-radius: 20px;[m
[32m+[m	[32moutline: 0;[m
[32m+[m	[32mbox-shadow: 0px;[m
[32m+[m	[32mborder: 0px;[m
[32m+[m	[32mcursor: pointer;[m
[32m+[m	[32mtransition:all 0.2s ease-in-out;[m
[32m+[m	[32mcolor: #fff;[m
[32m+[m	[32mfloat: right;[m
[32m+[m	[32mmargin-top: 10px;[m
[32m+[m[32m}[m
[32m+[m[32m.change-password form{[m
[32m+[m	[32mmargin-top: -20px;[m
[32m+[m[32m}[m
[32m+[m[32m .submit-contact:hover{[m
[32m+[m	[32mbackground: #2d2251;[m
[32m+[m[32m}[m
[32m+[m[32m.change-warning{[m
[32m+[m	[32mmargin-top: 20px;[m
[32m+[m	[32mtext-align: left;[m
[32m+[m[32m}[m
[32m+[m[32m.change-warning i{[m
[32m+[m	[32mcolor: #e6c115;[m
[32m+[m[32m}[m
[32m+[m[32m.reset-contact[m
[32m+[m[32m{float: left;[m
[32m+[m	[32mcolor: #4d4d4d;[m
[32m+[m	[32mpadding: 8px 15px;[m
[32m+[m	[32mbackground: transparent;[m
[32m+[m	[32mborder: 2px solid #9d9d9d;[m
[32m+[m[32m}[m
[32m+[m[32m.reset-contact:hover{[m
[32m+[m	[32mcolor: #fff;[m
[32m+[m	[32mbackground: #403469;[m
[32m+[m	[32mborder: 2px solid #403469;[m
[32m+[m
[32m+[m[32m}[m
[32m+[m
[32m+[m[32m/*coming soon========*/[m
[32m+[m
[32m+[m[32m.coming-soon{[m
[32m+[m	[32mtext-align: center;[m
[32m+[m	[32mmargin-top: 40px;[m
[32m+[m	[32mmargin-bottom: 40px;[m
[32m+[m[32m}[m
[32m+[m[32m.coming-soon h2{[m
[32m+[m	[32mcolor: #252525;[m
[32m+[m	[32mfont-family: 'Roboto Medium'[m
[32m+[m[32m}[m
[32m+[m[32m.coming-soon h3{[m
[32m+[m	[32mcolor: #4d4d4d;[m
[32m+[m	[32mmargin-top: 5px;[m
[32m+[m
[32m+[m[32m}[m
[32m+[m[32m/*loader==============*/[m
[32m+[m
[32m+[m[32m.loader-container{[m
[32m+[m	[32mz-index: 200;[m
[32m+[m	[32mposition: fixed;[m
[32m+[m	[32mwidth: 100vw;[m
[32m+[m	[32mheight: 100vh;[m
[32m+[m	[32mbackground: #fff;[m
 [m
[32m+[m[32m}[m
[32m+[m[32m.loader{[m
[32m+[m	[32mdisplay: inline-block;[m
[32m+[m	[32mposition: absolute;[m
[32m+[m	[32mmargin-right: auto;[m
[32m+[m	[32mmargin-left: auto;[m
[32m+[m	[32mleft: 0px;[m
[32m+[m	[32mright: 0px;[m
[32m+[m	[32m/*border: 1px solid red;*/[m
[32m+[m	[32mwidth: 70px;[m
[32m+[m	[32mheight: 70px;[m
[32m+[m	[32mmargin-top: 250px;[m
[32m+[m	[32manimation-name:rotate-loader;[m
[32m+[m	[32manimation-duration:8s;[m
[32m+[m	[32manimation-iteration-count:infinite;[m
[32m+[m	[32manimation-direction:linear;[m
[32m+[m	[32manimation-timing-function: linear;[m
[32m+[m[32m}[m
[32m+[m[32m@keyframes rotate-loader{[m
[32m+[m	[32mfrom{[m
[32m+[m		[32mtransform:rotate(0deg);[m
[32m+[m	[32m}[m
[32m+[m	[32mto{[m
[32m+[m		[32mtransform:rotate(720deg);[m
[32m+[m	[32m}[m
[32m+[m[32m}[m
[32m+[m[32m.load-text{[m
[32m+[m	[32mposition: absolute;[m
[32m+[m	[32mbottom: 40px;[m
[32m+[m	[32mmargin-right: auto;[m
[32m+[m	[32mmargin-left: auto;[m
[32m+[m	[32mleft: 0px;[m
[32m+[m	[32mright: 0px;[m
[32m+[m	[32mtext-align: center;[m
[32m+[m	[32mfont-family: 'Roboto Medium';[m
[32m+[m	[32mcolor: #4d4d4d;[m
[32m+[m
[32m+[m[32m}[m
[32m+[m[32m.loader img{[m
[32m+[m	[32mwidth: 100%;[m
[32m+[m[32m}[m
 @media(max-width: 950px){[m
 	.pad-list a{[m
 		padding:18px 30px 18px 30px[m
[36m@@ -1116,94 +1252,98 @@[m [mbutton.no-delete:hover{[m
 	margin-left: -250px;[m
 	width: 220px;[m
 	height: 100vh;[m
[31m-	background: #2d2251;[m
[32m+[m	[32m/*background: #2d2251;*/[m
 	[m
[31m-}[m
[31m-.relevant-page{[m
[31m-	padding-left: 0px;[m
[31m-}[m
[31m-.search{[m
[31m-	display: none;[m
[31m-}[m
[31m-.mobile-menu{[m
[31m-	cursor: pointer;[m
[31m-	display: inline-block;[m
[31m-	margin-right: 10px;[m
[31m-}[m
[31m-.left-nav-inner {[m
[31m-   [m
[31m-    height: calc(100% - 116px);[m
[31m-   [m
[31m-}[m
[31m-.footer-links div{[m
[31m-	padding-top: 4px;[m
[31m-}[m
[31m-.index-header{[m
[31m-	width: 100%;[m
[31m-}[m
[31m-.date-index,.auth-index{[m
[31m-	text-align: center;[m
[31m-	margin-top: 5px;[m
[31m-}[m
[31m-.head-index-links{[m
[31m-	display: block;[m
[31m-}[m
[31m-.jss-logo span{[m
[31m-	display: none;[m
[31m-}[m
[31m-.date-index{[m
[31m-	text-align: right;[m
[31m-}[m
[31m-.auth-index{[m
[31m-	text-align: left;[m
[31m-}[m
[31m-.index-head{[m
[31m-	border-bottom:1px solid #9d9d9d;[m
[31m-}[m
[32m+[m	[32m}[m
[32m+[m	[32m.relevant-page{[m
[32m+[m		[32mpadding-left: 0px;[m
[32m+[m	[32m}[m
[32m+[m	[32m.search{[m
[32m+[m		[32mdisplay: none;[m
[32m+[m	[32m}[m
[32m+[m	[32m.mobile-menu{[m
[32m+[m		[32mcursor: pointer;[m
[32m+[m		[32mdisplay: inline-block;[m
[32m+[m		[32mmargin-right: 10px;[m
[32m+[m	[32m}[m
[32m+[m	[32m.left-nav-inner {[m
[32m+[m[41m	   [m
[32m+[m	[32m    height: calc(100% - 116px);[m
[32m+[m[41m	   [m
[32m+[m	[32m}[m
[32m+[m	[32m.footer-links div{[m
[32m+[m		[32mpadding-top: 4px;[m
[32m+[m	[32m}[m
[32m+[m	[32m.index-header{[m
[32m+[m		[32mwidth: 100%;[m
[32m+[m	[32m}[m
[32m+[m	[32m.date-index,.auth-index{[m
[32m+[m		[32mtext-align: center;[m
[32m+[m		[32mmargin-top: 5px;[m
[32m+[m	[32m}[m
[32m+[m	[32m.head-index-links{[m
[32m+[m		[32mdisplay: block;[m
[32m+[m	[32m}[m
[32m+[m	[32m.jss-logo span{[m
[32m+[m		[32mdisplay: none;[m
[32m+[m	[32m}[m
[32m+[m	[32m.date-index{[m
[32m+[m		[32mtext-align: right;[m
[32m+[m	[32m}[m
[32m+[m	[32m.auth-index{[m
[32m+[m		[32mtext-align: left;[m
[32m+[m	[32m}[m
[32m+[m	[32m.index-head{[m
[32m+[m		[32mborder-bottom:1px solid #9d9d9d;[m
[32m+[m	[32m}[m
 [m
[31m-.index-logo{[m
[31m-	height: 50px;[m
[31m-}[m
[31m-.index-welcome{[m
[31m-	text-align: left;[m
[31m-}[m
[31m-.left-nav-inner-index{[m
[31m-	height:calc(100% - 152px);[m
[31m-}[m
[31m-.edit-profile-text{[m
[32m+[m	[32m.index-logo{[m
[32m+[m		[32mheight: 50px;[m
[32m+[m	[32m}[m
[32m+[m	[32m.index-welcome{[m
[32m+[m		[32mtext-align: left;[m
[32m+[m	[32m}[m
[32m+[m	[32m.left-nav-inner-index{[m
[32m+[m		[32mheight:calc(100% - 152px);[m
[32m+[m	[32m}[m
[32m+[m	[32m.edit-profile-text{[m
 		margin-right: 40px;[m
 		width: 100px;[m
 		margin-top: 2px;[m
 	}[m
[31m-h3.profile-head{[m
[31m-	font-size: 26px;[m
[31m-[m
[31m-	margin-top: 12px;[m
[31m-   [m
[31m-   [m
[31m-}[m
[31m-.profile-header{[m
[31m-	height: 89px;[m
[31m-}[m
[31m-.my-icons{[m
[31m-	text-align: right;[m
[31m-}[m
[31m-ul li.my-notice-list {[m
[31m-		padding: 0px 20px 20px 20px;[m
[31m-}[m
[31m-ul li.my-notice-list  .my-notice-pad{[m
[31m-	padding:20px 20px 0px 0px;[m
[31m-}[m
[31m-.my-mobile{[m
[31m-	display: block !important;[m
[32m+[m	[32mh3.profile-head{[m
[32m+[m		[32mfont-size: 26px;[m
[32m+[m		[32mmargin-top: 12px;[m
 	}[m
[31m-.my-mobile .pagination{[m
[31m-		display: inline-block;[m
[31m-		padding:0px;[m
[32m+[m	[32m.profile-header{[m
[32m+[m		[32mheight: 89px;[m
[32m+[m	[32m}[m
[32m+[m	[32m.my-icons{[m
[32m+[m		[32mtext-align: right;[m
[32m+[m	[32m}[m
[32m+[m	[32mul li.my-notice-list {[m
[32m+[m			[32mpadding: 0px 20px 20px 20px;[m
[32m+[m	[32m}[m
[32m+[m	[32mul li.my-notice-list  .my-notice-pad{[m
[32m+[m		[32mpadding:20px 20px 0px 0px;[m
 	}[m
[32m+[m	[32m.my-mobile{[m
[32m+[m		[32mdisplay: block !important;[m
[32m+[m		[32m}[m
[32m+[m	[32m.my-mobile .pagination{[m
[32m+[m			[32mdisplay: inline-block;[m
[32m+[m			[32mpadding:0px;[m
[32m+[m		[32m}[m
 	.my-desktop{[m
 		display: none;[m
 	}[m
[32m+[m	[32m.about-container{[m
[32m+[m		[32mpadding: 20px;[m
[32m+[m	[32m}[m
[32m+[m	[32m.loader{[m
[32m+[m[41m		[m
[32m+[m		[32mmargin-top: 190px;[m
[32m+[m	[32m}[m
 }[m
 [m
 [m
[36m@@ -1236,7 +1376,9 @@[m [mul li.my-notice-list  .my-notice-pad{[m
 h3.create-head{[m
 	font-size: 22px;[m
 }[m
[31m-[m
[32m+[m[32m.contact-container form{[m
[32m+[m	[32mwidth: 300px;[m
[32m+[m[32m}[m
 }[m
 @media(max-width: 480px){[m
 	.jss-logo{[m
[1mdiff --git a/HTTP_200/static/js/main.js b/HTTP_200/static/js/main.js[m
[1mindex 15f5cc4..dcc6e88 100644[m
[1m--- a/HTTP_200/static/js/main.js[m
[1m+++ b/HTTP_200/static/js/main.js[m
[36m@@ -1,5 +1,21 @@[m
 $(document).ready(function () {[m
 [m
[32m+[m	[32m$("body").css({[m
[32m+[m	[32m'overflow-y':'hidden'[m
[32m+[m[32m})[m
[32m+[m[32m$(".loader-container").fadeIn();[m
[32m+[m	[32m$(window).load(function  () {[m
[32m+[m		[32m$(".loader-container").delay(1000).fadeOut();[m
[32m+[m		[32msetTimeout(function(){[m
[32m+[m			[32m$("body").css({[m
[32m+[m				[32m'overflow-y':'scroll'[m
[32m+[m			[32m})[m
[32m+[m		[32m},1000)[m
[32m+[m[41m		[m
[32m+[m	[32m})[m
[32m+[m
[32m+[m
[32m+[m
 	$(".left-nav-inner ul li").click(function () {[m
 		$(this).addClass("active").siblings().removeClass("active");[m
 		$(this).find("span").addClass("active_number");[m
[36m@@ -103,7 +119,7 @@[m [m$(document).ready(function () {[m
 [m
 	$(".relevant-info").hide();[m
 [m
[31m-	$(".sec, .preview").click(function () {[m
[32m+[m	[32m$(".sec, .preview,.pad-list").click(function () {[m
 		$(".relevant-info").hide().fadeIn();[m
 		var index = $(".relevant-content ul li").index(this);[m
 		var id = $(this).attr('id');[m
[1mdiff --git a/HTTP_200/templates/index.html b/HTTP_200/templates/index.html[m
[1mindex 773033e..ef53ff6 100644[m
[1m--- a/HTTP_200/templates/index.html[m
[1m+++ b/HTTP_200/templates/index.html[m
[36m@@ -11,6 +11,51 @@[m
   <link rel="stylesheet" href="{% static "css/font-awesome.css"%}">[m
 </head>[m
 <body>[m
[32m+[m
[32m+[m
[32m+[m[32m<div class="loader-container">[m
[32m+[m[32m    <div class="loader">[m
[32m+[m[32m      <img src="{% static "images/connect.gif"%}">[m
[32m+[m[32m    </div>[m
[32m+[m[41m    [m
[32m+[m[32m  </div>[m
[32m+[m
[32m+[m
[32m+[m[32m  <div class="relevant-info">[m
[32m+[m[32m    <div class="info-header">[m
[32m+[m
[32m+[m[32m      <h2>[m
[32m+[m[32m        Relevant[m
[32m+[m[32m      </h2>[m
[32m+[m
[32m+[m[32m    </div>[m
[32m+[m[32m    <div class="head-info">[m
[32m+[m[32m      <h3>Title</h3>[m
[32m+[m[32m      ajshsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss[m
[32m+[m[32m    </div>[m
[32m+[m[32m    <div class="content-info">[m
[32m+[m[32m      <h3>Details</h3>[m
[32m+[m[32m      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer ornare nisi urna, sit amet posuere odio posuere a. Pellentesque sed purus finibus, sollicitudin libero quis, porttitor velit. Maecenas mollis convallis elementum. Aliquam dictum est felis, feugiat laoreet diam tincidunt ac. Curabitur lacus justo, dapibus luctus finibus ac, venenatis at libero. Suspendisse dignissim eget sem vitae dictum. Pellentesque lacinia urna ligula, sit amet porta nibh volutpat eget. Duis rutrum orci a eros maximus faucibus. Vivamus maximus magna sit amet iaculis rhoncus. Ut nec suscipit ex. Nunc tristique ex vel eros rhoncus, nec pharetra enim porttitor.[m
[32m+[m[32m        <br>[m
[32m+[m[32m        <br> Morbi varius, nisi et scelerisque congue, dolor orci egestas ligula, at imperdiet tortor tortor efficitur orci. Vestibulum ex elit, egestas ac orci sed, euismod aliquet elit. Aliquam varius magna non lacus aliquam sollicitudin. Donec ante sapien, luctus vel rutrum nec, pharetra eget metus. In imperdiet libero ligula. Vivamus dui massa, tempus et aliquam quis, commodo pellentesque turpis. Ut sed auctor quam, vel molestie nunc. Nullam pulvinar pulvinar libero, at dictum nunc placerat at. Praesent ac sollicitudin orci. Sed consequat nibh vitae fermentum bibendum. Duis rutrum eget arcu at vestibulum. Quisque porttitor, ex nec euismod malesuada, turpis mi sagittis mauris, eu interdum purus risus pretium diam. Pellentesque non efficitur leo, vitae egestas felis. Sed mattis sed libero ac condimentum. Pellentesque tortor ante, aliquet eget dui ut, euismod rhoncus lorem. Nulla sed purus eget diam ultricies mollis eu sit amet sem. Quisque mollis non dui vel aliquam. Donec pretium diam eu semper scelerisque. Nullam tellus velit, ultrices at eros a, aliquet ornare quam. Nam in pretium elit. Sed risus ante, lobortis in tortor ut, commodo interdum turpis. Praesent consequat dignissim ligula, vitae consectetur nisi pharetra quis. Nullam a dolor eleifend mauris facilisis suscipit sed a tellus. Quisque nec consectetur massa, nec aliquam nulla. Curabitur egestas convallis lacus ac dignissim. Morbi varius, nisi et scelerisque congue, dolor orci egestas ligula, at imperdiet tortor tortor efficitur orci. Vestibulum ex elit, egestas ac orci sed, euismod aliquet elit. Aliquam varius magna non lacus aliquam sollicitudin. Donec ante sapien, luctus vel rutrum nec, pharetra eget metus. In imperdiet libero ligula. Vivamus dui massa, tempus et aliquam quis, commodo pellentesque turpis. Ut sed auctor quam, vel molestie nunc. Nullam pulvinar pulvinar libero, at dictum nunc placerat at. Praesent ac sollicitudin orci. Sed consequat nibh vitae fermentum bibendum. Duis rutrum eget arcu at vestibulum. Quisque porttitor, ex nec euismod malesuada, turpis mi sagittis mauris, eu interdum purus risus pretium diam. Pellentesque non efficitur leo, vitae egestas felis. Sed mattis sed libero ac condimentum. Pellentesque tortor ante, aliquet eget dui ut, euismod rhoncus lorem. Nulla sed purus eget diam ultricies mollis eu sit amet sem. Quisque mollis non dui vel aliquam. Donec pretium diam eu semper scelerisque. Nullam tellus velit, ultrices at eros a, aliquet ornare quam. Nam in pretium elit. Sed risus ante, lobortis in tortor ut, commodo interdum turpis. Praesent consequat dignissim ligula, vitae consectetur nisi pharetra quis. Nullam a dolor eleifend mauris facilisis suscipit sed a tellus. Quisque nec consectetur massa, nec aliquam nulla. Curabitur egestas convallis lacus ac dignissim.Morbi varius, nisi et scelerisque congue, dolor orci egestas ligula, at imperdiet tortor tortor efficitur orci. Vestibulum ex elit, egestas ac orci sed, euismod aliquet elit. Aliquam varius magna non lacus aliquam sollicitudin. Donec ante sapien, luctus vel rutrum nec, pharetra eget metus. In imperdiet libero ligula. Vivamus dui massa, tempus et aliquam quis, commodo pellentesque turpis. Ut sed auctor quam, vel molestie nunc. Nullam pulvinar pulvinar libero, at dictum nunc placerat at. Praesent ac sollicitudin orci. Sed consequat nibh vitae fermentum bibendum. Duis rutrum eget arcu at vestibulum. Quisque porttitor, ex nec euismod malesuada, turpis mi sagittis mauris, eu interdum purus risus pretium diam. Pellentesque non efficitur leo, vitae egestas felis. Sed mattis sed libero ac condimentum. Pellentesque tortor ante, aliquet eget dui ut, euismod rhoncus lorem. Nulla sed purus eget diam ultricies mollis eu sit amet sem. Quisque mollis non dui vel aliquam. Donec pretium diam eu semper scelerisque. Nullam tellus velit, ultrices at eros a, aliquet ornare quam. Nam in pretium elit. Sed risus ante, lobortis in tortor ut, commodo interdum turpis. Praesent consequat dignissim ligula, vitae consectetur nisi pharetra quis. Nullam a dolor eleifend mauris facilisis suscipit sed a tellus. Quisque nec consectetur massa, nec aliquam nulla. Curabitur egestas convallis lacus ac dignissim.Morbi varius, nisi et scelerisque congue, dolor orci egestas ligula, at imperdiet tortor tortor efficitur orci. Vestibulum ex elit, egestas ac orci sed, euismod aliquet elit. Aliquam varius magna non lacus aliquam sollicitudin. Donec ante sapien, luctus vel rutrum nec, pharetra eget metus. In imperdiet libero ligula. Vivamus dui massa, tempus et aliquam quis, commodo pellentesque turpis. Ut sed auctor quam, vel molestie nunc. Nullam pulvinar pulvinar libero, at dictum nunc placerat at. Praesent ac sollicitudin orci. Sed consequat nibh vitae fermentum bibendum. Duis rutrum eget arcu at vestibulum. Quisque porttitor, ex nec euismod malesuada, turpis mi sagittis mauris, eu interdum purus risus pretium diam. Pellentesque non efficitur leo, vitae egestas felis. Sed mattis sed libero ac condimentum. Pellentesque tortor ante, aliquet eget dui ut, euismod rhoncus lorem. Nulla sed purus eget diam ultricies mollis eu sit amet sem. Quisque mollis non dui vel aliquam. Donec pretium diam eu semper scelerisque. Nullam tellus velit, ultrices at eros a, aliquet ornare quam. Nam in pretium elit. Sed risus ante, lobortis in tortor ut, commodo interdum turpis. Praesent consequat dignissim ligula, vitae consectetur nisi pharetra quis. Nullam a dolor eleifend mauris facilisis suscipit sed a tellus. Quisque nec consectetur massa, nec aliquam nulla. Curabitur egestas convallis lacus ac dignissim. Donec at orci et tortor sodales efficitur. In lobortis lacus non mauris accumsan cong</p>[m
[32m+[m[32m    </div>[m
[32m+[m[32m    <div class="head-info download">[m
[32m+[m[32m      <a href="#" download><h3>Download Attachment</h3>&nbsp;[m
[32m+[m[32m      <i class="fa fa-download"></i></a>[m
[32m+[m[32m    </div>[m
[32m+[m[32m    <div class="date-author-info">[m
[32m+[m[32m      Posted By Akash Jain on 03-March-2016[m
[32m+[m[32m    </div>[m
[32m+[m
[32m+[m[32m    <div class="cross">[m
[32m+[m[32m      <i class="fa fa-times"></i>[m
[32m+[m
[32m+[m[32m    </div>[m
[32m+[m
[32m+[m[32m  </div>[m
[32m+[m
[32m+[m
[32m+[m
   <div class="overlay-dark">[m
     <div class="cross-mobile"><i class="fa fa-times"></i></div>[m
   </div>[m
[36m@@ -33,16 +78,16 @@[m
         <!-- <li>[m
           <a class="search2"><i class="fa fa-search"></i> &nbsp;Search</a>[m
         </li> -->[m
[31m-        <li><a href="http://jssaten.ac.in">[m
[31m-          <i class="fa fa-globe"></i> &nbsp;JSS Website</a>[m
[32m+[m[32m        <li><a href="{% url "about" %}" >[m
[32m+[m[32m          <i class="fa fa-globe"></i> &nbsp;About</a>[m
         </li>[m
           <li>[m
[31m-            <a href="{% url "about" %}">[m
[31m-            <i class="fa fa-user"></i> &nbsp;About</a>[m
[32m+[m[32m            <a href="{% url "contact" %}">[m
[32m+[m[32m            <i class="fa fa-user"></i> &nbsp;Contact</a>[m
           </li>[m
           <li>[m
[31m-            <a href="{% url "contact" %}">[m
[31m-            <i class="fa fa-phone"></i> &nbsp;Contact</a>[m
[32m+[m[32m            <a href="http://jssaten.ac.in" target="_blank">[m
[32m+[m[32m            <i class="fa fa-phone"></i> &nbsp;JSS Website</a>[m
           </li>[m
           [m
 [m
[36m@@ -100,16 +145,16 @@[m
         <ul>[m
         {% for notice in notices %}[m
           <li class="pad-list">[m
[31m-            <a href="{% url "notice-show" pk=notice.pk %}">[m
[32m+[m[32m            <a>[m
             <div class="col col-7">[m
               {{ notice.title }}[m
             </div>[m
             <div class="date-index col col-5">[m
               <div class="row">[m
[31m-                <div class="auth-index col sm-col-5">[m
[32m+[m[32m                <div class="auth-index col sm-col-6">[m
                   <i class="fa fa-user"></i> &nbsp;{{ notice.faculty }}[m
                 </div>[m
[31m-                <div class="date-index col sm-col-7">[m
[32m+[m[32m                <div class="date-index col sm-col-6">[m
                   <i class="fa fa-calendar"></i> &nbsp;{{ notice.modified }}[m
                 </div>[m
               </div>[m
[36m@@ -128,13 +173,18 @@[m
         <ul>[m
         {% for trend in trending %}[m
           <li class="pad-list">[m
[31m-            <a href="{{ trend.url }}">[m
[31m-            <div class="col col-9">[m
[31m-            <b>{{ trend.title }}</b> - {{ trend.small_description}}[m
[32m+[m[32m            <a>[m
