var React = require('react');
var ReactDOM = require('react-dom');
var Tether = require('react-tether');
var antd =  require('antd');


var Map = React.createClass({
  getInitialState: function(){
    return{
      center: {lat: 59.938043, lng: 30.337157},
      zoom: 9,
      greatPlaceCoords: {lat: 59.724465, lng: 30.080121}
    }
  },
  initMap: function () {
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: {lat: -33, lng: 151}
  });

  var image = 'images/beachflag.png';
  var beachMarker = new google.maps.Marker({
    position: {lat: -33.890, lng: 151.274},
    map: map,
    icon: image
  });
  }
  render: function() {
    return
  }
})

/* Rendering Container Form */
ReactDOM.render(
  <Map/>,
	document.getElementById('root')
)
