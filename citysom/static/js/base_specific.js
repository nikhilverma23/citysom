
jQuery(document).ready(function() {
	
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
	
	$("#change_location").click(function(){
		$("#city_change_div").toggle();
	});
	
	$(document).ready(function(){
        //$(".login_content input[type=text],.login_content input[type=checkbox],.login_content input[type=radio],.login_content input[type=password], .login_content textarea, .login_content select").uniform();
    });
});


$(".timepicker").timepicker(
	{
		timeFormat:"hh:mm",
		stepMinute: 5
	}
);

function geolocation() {
// Try HTML5 geolocation
if(navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(function(position) {
	codeLatLng(position.coords.latitude, position.coords.longitude);
  }, function() {
    
  });
} else {
  // Browser doesn't support Geolocation
}
}
function codeLatLng(lat,lng) {
var latlng = new google.maps.LatLng(lat, lng);
geocoder = new google.maps.Geocoder();
geocoder.geocode({'latLng': latlng}, function(results, status) {
  if (status == google.maps.GeocoderStatus.OK) {
    if (results[1]) {
	set_city(results[1].address_components[2].long_name);
    }
  }
});
}

function set_city(city)
{
	url = '/event/update_city/?city='+city;
	$.get(
		url,
		function(data)
		{
			$("#city_div").html(data);
			load_events();
		}
	);
	$("#city_change_div").hide();
}