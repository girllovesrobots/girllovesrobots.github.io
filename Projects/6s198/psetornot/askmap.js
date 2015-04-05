//FRONT END JS
//Currently empty, but will contain script commands to pull Fusion Table Data
//to make pins for each location on the map


//Below are temporary arrays that store basic data about the user and the other psetters.
//Each array is currently filled with dummy data for the prototype stage of the application
//Optimally the arrays would be filled with information obtained from the Fusion Table
//Arrays store information in the format of ['Name', Lat, Long]

var userloc = [['My Location', 42.361648260887, -71.0905194348]];
var otherloc = [
    ['Person1', 42.361281194679,-71.090739104637],
    ['Person2', 42.361109910589,-71.091929775975],
    ['Person3', 42.359195019987, -71.088351164953],
    ['Person4', 42.358919686655, -71.094675498372],
    ['Person5', 42.362328, -71.091643]
  ];

//The map will always be centered on the user's location
var myCenter = new google.maps.LatLng(userloc[0][1], userloc[0][2])

//This array contains the user and all relevant psetter's data
var places = userloc.concat(otherloc);

//The initialize function
function initialize() {
      var mapOptions = {
        zoom: 16,
        center: myCenter
        }
      var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
      setMarkers(map, places);
      queryTable(map);
      layer.setMap(map);
      map.fitBounds(bounds);
    }

function setMarkers(map, locations){
      for (var i=0; i<locations.length; i++) {
        img = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
        if (i==0) {
          img = 'http://maps.google.com/mapfiles/ms/icons/yellow-dot.png'
        }
        var mark = locations[i];
        var myLatLng = new google.maps.LatLng(mark[1], mark[2]);
        var marker = new google.maps.Marker({
            position: myLatLng,
            map: map,
            size: new google.maps.Size(10,10),
            icon: img
          });

        }
      }

//Function that queries the FusionTable and displays only the most relevant data
//to the app user
//TODO: add ability to filter by a certain class based on the user's pset class
//TODO: something like the yahoo query that lets app send user kerberos and pset location
//[can then use to start psetting]

function queryTable(map){
      var layer = new google.maps.FusionTablesLayer({
      query: {
          select: '\'Geocodable location\'',
          from: '1icaZHY14U93g_Ya9tJQ5I1LUM9_ElfLVufKGvrT8',
        },
      //available colors: small_yellow, small_red, small_purple, small_green
      //small_blue, measle_turquoise, measle_brown, measle_white,


      styles: [
              {where: 'shown == true' && "'time' >= 120",
                markerOptions: {iconName: 'measle_brown'}
              },

              {where: 'shown == true' && "'time' < 120",
                markerOptions: {iconName: 'small_yellow'}
              },

              {where: 'shown == true' && "'time' < 60",
               markerOptions: {iconName: 'small_purple'}
              },

              {where: 'shown == true' && "'time' < 30",
               markerOptions: {iconName: 'measle_turquoise'}
              },

              {where: 'shown == true' && "'time' <= 10",
               markerOptions: {iconName: 'small_purple'}
              }
        ]});
        layer.setMap(map);
      }


google.maps.event.addDomListener(window, 'load', initialize);
