<script src='https://maps.googleapis.com/maps/api/js?key=&sensor=false&extension=.js'></script>

<script>
    google.maps.event.addDomListener(window, 'load', init);
    var map;
    function init() {
        var mapOptions = {
            center: new google.maps.LatLng(40.421887,-3.693645),
            zoom: 13,
            zoomControl: true,
            zoomControlOptions: {
                style: google.maps.ZoomControlStyle.DEFAULT,
            },
            disableDoubleClickZoom: true,
            mapTypeControl: true,
            mapTypeControlOptions: {
                style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR,
            },
            scaleControl: true,
            scrollwheel: true,
            panControl: true,
            streetViewControl: true,
            draggable : true,
            overviewMapControl: true,
            overviewMapControlOptions: {
                opened: false,
            },
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            styles: [{"featureType":"administrative","elementType":"all","stylers":[{"visibility":"on"},{"saturation":-100},{"lightness":20}]},{"featureType":"road","elementType":"all","stylers":[{"visibility":"on"},{"saturation":-100},{"lightness":40}]},{"featureType":"water","elementType":"all","stylers":[{"visibility":"on"},{"saturation":-10},{"lightness":30}]},{"featureType":"landscape.man_made","elementType":"all","stylers":[{"visibility":"simplified"},{"saturation":-60},{"lightness":10}]},{"featureType":"landscape.natural","elementType":"all","stylers":[{"visibility":"simplified"},{"saturation":-60},{"lightness":60}]},{"featureType":"poi","elementType":"all","stylers":[{"visibility":"off"},{"saturation":-100},{"lightness":60}]},{"featureType":"transit","elementType":"all","stylers":[{"visibility":"off"},{"saturation":-100},{"lightness":60}]}],
        }
        var mapElement = document.getElementById('sacdsfsdfsdf');
        var map = new google.maps.Map(mapElement, mapOptions);
        var locations = [
['destino', 'undefined', 'undefined', 'undefined', 'undefined', 40.4378632, -3.6863034000000425, 'https://mapbuildr.com/assets/img/markers/solid-pin-black.png'],['destino', 'undefined', 'undefined', 'undefined', 'undefined', 40.4096739, -3.6990445000000136, 'https://mapbuildr.com/assets/img/markers/solid-pin-black.png']
        ];
        for (i = 0; i < locations.length; i++) {
			if (locations[i][1] =='undefined'){ description ='';} else { description = locations[i][1];}
			if (locations[i][2] =='undefined'){ telephone ='';} else { telephone = locations[i][2];}
			if (locations[i][3] =='undefined'){ email ='';} else { email = locations[i][3];}
           if (locations[i][4] =='undefined'){ web ='';} else { web = locations[i][4];}
           if (locations[i][7] =='undefined'){ markericon ='';} else { markericon = locations[i][7];}
            marker = new google.maps.Marker({
                icon: markericon,
                position: new google.maps.LatLng(locations[i][5], locations[i][6]),
                map: map,
                title: locations[i][0],
                desc: description,
                tel: telephone,
                email: email,
                web: web
            });
link = '';     }
   var waypts = [];
      directionsService = new google.maps.DirectionsService();
      directionsDisplay = new google.maps.DirectionsRenderer({
          suppressMarkers: true
      });
      if (locations.length > 1){
          for (var i = 0; i < locations.length; i++) {
              waypts.push({
                  location:new google.maps.LatLng(locations[i][5], locations[i][6]),
                  stopover:true
              });
          };
          var request = {
              origin: new google.maps.LatLng(locations[0][5], locations[0][6]),
              destination: new google.maps.LatLng(locations[locations.length - 1][5], locations[locations.length - 1][6]),
              waypoints: waypts,
              optimizeWaypoints: true,
              travelMode: google.maps.DirectionsTravelMode.DRIVING
          };
          directionsService.route(request, function(response, status) {
              if (status == google.maps.DirectionsStatus.OK) {
                  polylineOptions = {
                      strokeColor: '#0095b6',
                      strokeWeight: '3'
                  }
                  directionsDisplay.setOptions({
                      polylineOptions: polylineOptions
                  });
                  directionsDisplay.setDirections(response);
              }
          });
          directionsDisplay.setMap(map);
       }


}
</script>
<style>
    #sacdsfsdfsdf {
        height:400px;
        width:550px;
    }
    .gm-style-iw * {
        display: block;
        width: 100%;
    }
    .gm-style-iw h4, .gm-style-iw p {
        margin: 0;
        padding: 0;
    }
    .gm-style-iw a {
        color: #4272db;
    }
</style>

<div id='sacdsfsdfsdf'></div>
