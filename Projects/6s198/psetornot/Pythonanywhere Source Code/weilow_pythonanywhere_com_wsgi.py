HELLO_WORLD = """<html>
<head>
    <title>Python Anywhere hosted web application</title>
</head>
<body>
<h1>Hello, World!</h1>
<p>

</p>
<p>
    Find out more about how to configure your own web application
    by visiting the <a href="https://www.pythonanywhere.com/web_app_setup/">web app setup</a> page
</p>
</body>
</html>"""

"""url parameters are stored in the environ variable
PATH_INFO is the URL, so in root looks like /
-------------------------------------------------------------"""

def application(environ, start_response):
    param = environ.get('PATH_INFO')[1:]
    problemset, lat, lon = param.split("/")
    if param:
        status = '200 OK'
        content = """
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Psetters In Your Area</title>

    <!-- Map Page Layout Style -->
    <style>
      html, body, #map-canvas {
        height: 100%;
        margin: 0px;
        padding: 0px
      }
    </style>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
    <!-- Google Maps API Reference, including Wei Low's browser API Key -->
    <script type="text/javascript"
      src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDM8urGiP100_mibDOn1ZwVJid2oPzC1Mc">
    </script>
    <!-- Google Maps API Reference, including my browser API Key -->
    <script>
    //The map will always be centered on the user's location
    var myCenter = new google.maps.LatLng("""+lat+""", """+lon+""")

    //The initialize function
    function initialize() {
          var mapOptions = {
            zoom: 17,
            center: myCenter
            }
          var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
          setUser(map);
          queryTable(map);
          layer.setMap(map);
        }

    function setUser(map){
        img = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'

        var myLatLng = new google.maps.LatLng("""+lat+""", """+lon+""");
        var marker = new google.maps.Marker({
            position: myLatLng,
            map: map,
            size: new google.maps.Size(10,10),
            icon: img
          });
        }

    //Function that queries the FusionTable and displays only the most relevant data
    //to the app user
    //TODO: add ability to filter by a certain class based on the user's pset class
    //TODO: something like the yahoo query that lets app send user kerberos and pset location
    //[can then use to start psetting]

    function queryTable(map){
          var layer = new google.maps.FusionTablesLayer({
          query: {
              select: 'Geocodable location',
              from: '1icaZHY14U93g_Ya9tJQ5I1LUM9_ElfLVufKGvrT8',
              where: "pset = '"""+problemset+"""'"
            },
          //available colors: small_yellow, small_red, small_purple, small_green
          //small_blue, measle_turquoise, measle_brown, measle_white,

          styles: [
                  {where: "time >= 120",
                    markerOptions: {iconName: 'small_red'}
                  },

                  {where: "time < 120",
                    markerOptions: {iconName: 'small_purple'}
                  },

                  {where: "time < 60",
                   markerOptions: {iconName: 'small_yellow'}
                  },

                  {where: "time < 30",
                   markerOptions: {iconName: 'small_blue'}
                  },

                  {where: "time <= 10",
                   markerOptions: {iconName: 'small_green'}
                  }
            ]});
            layer.setMap(map);

          }


    google.maps.event.addDomListener(window, 'load', initialize);
    </script>
    <!--<script src=askmap.js></script> -->
  </head>
  <body>
    <div id="map-canvas"></div>
  </body>
</html>
"""
    else:
        status = '404 NOT FOUND'
        content = 'Page not found.'
    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(content)))]
    start_response(status, response_headers)
    yield content.encode('utf8')

