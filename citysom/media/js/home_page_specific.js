window.togl
if(typeof togl == "undefined"){togl=0;} 


var step = 10;
var timestep = 15;
var sort = 'price';
function load_events(){
	url = '/event/event_list/?view=list&tgl='+togl;
  	min_price = parseInt($("#min_price").val());
  	max_price = parseInt($("#max_price").val());
  	event_date = $(".calendar_start").attr("rel")?$(".calendar_start").attr("rel"):$(".calendar_active").attr("rel");
  	event_date_end = $(".calendar_end").attr("rel");
  	filter_time = $("#hours_range_select").val();
  	category = $("#event_type_select").val();
  	audience = $('#event_audience_select').val()
  	search_text = $("#searchtextarea").val();
	sort = $("#sort").val();
  			
  	if(!isNaN(min_price)) url +='&min_price='+min_price;
  	if(!isNaN(max_price)) url +='&max_price='+max_price;
  	if(event_date) url +='&event_date='+event_date;
  	if(event_date_end) url +='&event_date_end='+event_date_end;
	if(sort) {url +='&sort='+sort;}
  	if(filter_time){
  		var str=''
  		var st_str=''
  		var ed_str=''
  		var ctrl=''
  		if(filter_time==''){
  			str='';
  			}
  		else{
  			if(filter_time[0]==''){
  				st_str='';
	  			}
	  		else{
	  			if(filter_time[1]==''){
	  				st_str=filter_time[0]+':'+'00';
	  				}
	  			else{
	  				st_str=filter_time[0]+':'+filter_time[1];
	  				}
	  			}
	  		if(filter_time[2]==''){
	  			ed_str='';
	  			}
	  		else{
	  			if(filter_time[3]==''){
	  				ed_str=filter_time[2]+':'+'00';	
	  				}
	  			else{
	  				ed_str=filter_time[2]+':'+filter_time[3];
	  				}	
	  			}
	  		if(st_str=='' && ed_str==''){
	  			str='';
	  			}
	  		else if(st_str==''){
	  			str='&end_time='+ed_str;
	  			}
	  		else if(ed_str==''){
	  			str='&start_time='+st_str;
	  			}
	  		else{
	  			if (parseInt(filter_time[0])>=parseInt(filter_time[2])){
	  				if((parseInt(filter_time[0])==parseInt(filter_time[2])) && (parseInt(filter_time[1])>=parseInt(filter_time[3]))){
	  					/*alert("Sorry! I don't understand the time filters");*/
	  					ctrl='1';
	  					str='&start_time='+st_str+'&end_time='+ed_str+'&ctrl='+ctrl;
	  					}
	  				else if((parseInt(filter_time[0])==parseInt(filter_time[2])) && (parseInt(filter_time[1])<parseInt(filter_time[3]))){
	  					str='&start_time='+st_str+'&end_time='+ed_str;
	  					}
	  				else{
	  					/*alert("Sorry! I don't understand the time filters");*/
	  					ctrl='1';
	  					str='&start_time='+st_str+'&end_time='+ed_str+'&ctrl='+ctrl;
	  					}
	  				}
	  			else{
	  				str='&start_time='+st_str+'&end_time='+ed_str;
	  				}
	  			}
	  		}
  		
  		url +=str;
  	}
  			
  	if(category){
  		var i=0
  		var str=''
  		while(i<category.length){
  			str +='&category='+category[i];
  			i+=1;
  			}
  		url +=str;
  		}
  				
  				
  	if(audience){
  		var j=0
  		var stg=''
  		while(j<audience.length){
  			stg +='&audience='+audience[j];
  			j+=1;
  			}
  		url +=stg;
  		}
  				
  					
  	if(search_text){url +='&search_text='+search_text;}
  	
  	$.get(url,function(data){
		$("#bottom_images").html(data);
		});
}


$(document).ajaxStop(function(){
	
	$(".touchcarousel").touchCarousel({
		itemsPerMove: 3,
		scrollbar: false, 
		scrollbarAutoHide: false,     // Scrollbar autohide.
		scrollbarTheme: "dark",
		transitionSpeed: 1,
		autoplay:false,
		directionNav:true,            // Direction (arrow) navigation (true or false).
		directionNavAutoHide:false, 
		loopItems: false, 
		keyboardNav: true,
		dragUsingMouse:true,
		itemFallbackWidth: 150, 
		lockAxis: true,
		scrollToLast: false,
		});
		
});
jQuery("li.misc_pres").live("mouseover",function(){$(this).children("div.like_div").show();});
jQuery("li.misc_pres").live("mouseout",function(){$(this).children("div.like_div").hide();});
  		
/*  		
$("#min_price_down").click(function(){
	var current_price = parseInt($("#min_price").val())-step;
  	if(current_price >= 0){
  		$("#min_price").val(current_price);
  		$("#min_price_span").html(current_price);
  		load_events();}
});
  		
  		
$("#min_price_up").click(function(){
	var current_price = parseInt($("#min_price").val())+step;
  	$("#min_price").val(current_price);
  	$("#min_price_span").html(current_price);
  	load_events();
});
 		
$("#max_price_down").click(function(){
	var current_max_price = parseInt($("#max_price").val())-step;
  	if(current_max_price >= 0){
  		$("#max_price").val(current_max_price);
  		$("#max_price_span").html(current_max_price);
  		load_events();
  		}
});
  		
$("#max_price_up").click(function(){
	var current_max_price = parseInt($("#max_price").val())+step;
  	$("#max_price").val(current_max_price);
  	$("#max_price_span").html(current_max_price);
  	load_events();
});
  		
var variable_date = new Date();
variable_date.setHours(8);
variable_date.setMinutes(0);
variable_date.setSeconds(0);
var current_formatted_date;
$("#max_time_down").click(function(){
	variable_date.setMinutes(variable_date.getMinutes()-timestep);
	current_formatted_date = variable_date.getHours()+":"+variable_date.getMinutes();
	$("#max_time").val(current_formatted_date);
	$("#max_time_span").html(current_formatted_date);
	load_events();
});
$("#max_time_up").click(function()
{
	variable_date.setMinutes(variable_date.getMinutes()+timestep);
	current_formatted_date = variable_date.getHours()+":"+variable_date.getMinutes();
	$("#max_time").val(current_formatted_date);
	$("#max_time_span").html(current_formatted_date);
	load_events();
});*/
