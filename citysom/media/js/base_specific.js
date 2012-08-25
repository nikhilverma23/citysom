
jQuery(document).ready(function() {
	var loc = window.location.toString()
	var page = loc.substring(loc.indexOf('/', 8), loc.length);
	$('#topnavigation>ul>li>a[href="' + page + '"]').parent().addClass("current");
	if(page =='/myprofile/home/'){$('#topnavigation>ul>li>a[href="/"]').parent().addClass("current");}
	
	var mouse_is_inside=false;
	
	$('.login_top_div').hover(function(){
		mouse_is_inside=true;
		}, function(){
			mouse_is_inside=false;
		});
	
	$(document).mouseup(function(){
		if(!mouse_is_inside) $('.login_top_div').hide();	
	});

	jQuery("#menu > li a").click(function(e) {

		jQuery("#everything1, #categories, #concerts, #more").hide();

		jQuery(this).parent().addClass('active');
		jQuery(jQuery(this).attr('href')).show();
		return false;
	});
	

	
	//jQuery("#topnavigation > ul li").click(function(){
	//	jQuery(this).addClass("current");
	//});

	jQuery("#bottom_images").jScrollPane({
		showArrows : true
	});

	$(".search_link").click(function() {
		$("#searchtextarea").val("Search Here...");
		$("#searchtextarea").focus();
		$("#searchtextarea").click(function() {
			$(this).val('');
		});
	});
	$(".login_top_link").click(function(){
		$(".login_top_div").toggle();
	});
	
	$(document).ready(function(){
        $(".login_content input[type=text],.login_content input[type=checkbox],.login_content input[type=radio],.login_content input[type=password], .login_content textarea, .login_content select").uniform();
    });
});


$(".timepicker").timepicker(
	{
		timeFormat:"hh:mm",
		stepMinute: 5
	}
);
