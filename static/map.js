function showPosition(position){
	var map=new BMap.Map("content");
	var point = new BMap.Point(position.coords.longitude, position.coords.latitude);
	map.centerAndZoom(point, 15);
	map.addControl(new BMap.NavigationControl()); 
}


function getLocation(){

//require location authentication
	if(navigator.geolocation){
		navigator.geolocation.getCurrentPosition(showPosition);
	}else{
		alert("geolocation is not supported");
	}    
}
