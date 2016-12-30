var React = require('react');
var ReactDOM = require('react-dom');
var Tether = require('react-tether');
var antd =  require('antd');
var GoogleMap = require('google-map-react');


var Map = React.createClass({
  getInitialState: function(){
    return{
      center: {lat: 59.938043, lng: 30.337157},
      zoom: 9,
      greatPlaceCoords: {lat: 59.724465, lng: 30.080121}
    }
  },
  render: function() {
    return
       <GoogleMap
        defaultCenter={this.props.center}
        defaultZoom={this.props.zoom}>
        <MyGreatPlace lat={59.955413} lng={30.337844} text={'A'} /* Kreyser Avrora */ />
        <MyGreatPlace {...this.props.greatPlaceCoords} text={'B'} /* road circle */ />
      </GoogleMap>
  }
})

/* Rendering Container Form */
ReactDOM.render(
  <Map/>,
	document.getElementById('root')
)
