function showPosition(){
	alert("position");
//	alert("Latitude: " + position.coords.latitude + "<br>Longitude: " + position.coords.longitude);
}

$(
/**
 * load when init page
 */
function(){
	
	//load local settings
	if(localStorage && localStorage.theme){
		themeCode = localStorage.theme;
		$("#pageone").removeClass( "ui-page-theme-a ui-page-theme-b" ).addClass( "ui-page-theme-" + themeCode );
		$("#header").removeClass( "ui-page-theme-a ui-page-theme-b" ).addClass( "ui-page-theme-" + themeCode );
		$("#footer").removeClass( "ui-page-theme-a ui-page-theme-b" ).addClass( "ui-page-theme-" + themeCode );
	}
	
	//require location authentication
	if(navigator.geolocation){
		navigator.geolocation.getCurrentPosition(showPosition);
	}else{
		alert("geolocation is not supported");
	}
	
	
	/**
	 * theme switch
	 */
	$("select#theme").change(
			function(){
				theme = $("select#theme").val();
				themeCode = "a";
				if(theme == "on"){
					themeCode = "b";
				}
				//store current theme
				if(localStorage){
					localStorage.theme = themeCode; 
				}
				
				$("#pageone").removeClass( "ui-page-theme-a ui-page-theme-b" ).addClass( "ui-page-theme-" + themeCode );
				$("#header").removeClass( "ui-page-theme-a ui-page-theme-b" ).addClass( "ui-page-theme-" + themeCode );
				$("#footer").removeClass( "ui-page-theme-a ui-page-theme-b" ).addClass( "ui-page-theme-" + themeCode );

			}
	);
			
});



