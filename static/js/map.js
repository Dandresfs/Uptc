var uptc = new google.maps.LatLng(5.7058054, -72.9415968);
var lab1 = new google.maps.LatLng(5.7044993, -72.9411913);
var lab2 = new google.maps.LatLng(5.7051806, -72.942096);
var marker;
var marker2;
var map;

var contentStringLab1 = '<div id="content">'+
      '<div>'+
        '<h3 class="text-center" style="color:black">Laboratorio de Manufactura</h3>'+
        '<img src="/static/imagenes/laboratorio1.jpg" width="256" class="img-responsive center-block" style="margin:0 auto">'+
        '<p style="color:black;padding:10px;">Aca va una descripcion del laboratorio de manufactura de la universidad pedagogica y tecnologica de colombia</p>'+
      '</div>';

  var infowindowlab1 = new google.maps.InfoWindow({
      content: contentStringLab1
  });


var contentStringLab2 = '<div id="content">'+
      '<div>'+
        '<h3 class="text-center" style="color:black">Laboratorio de Producción</h3>'+
        '<img src="/static/imagenes/laboratorio2.jpg" width="256" class="img-responsive center-block" style="margin:0 auto">'+
        '<p style="color:black;padding:10px;">Aca va una descripcion del laboratorio de producción de la universidad pedagogica y tecnologica de colombia</p>'+
      '</div>';

  var infowindowlab2 = new google.maps.InfoWindow({
      content: contentStringLab2
  });


function initialize(){
  var mapOptions = {
    zoom: 17,
    center: uptc
  };

  map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

  marker = new google.maps.Marker({
    map:map,
    draggable:false,
    animation: google.maps.Animation.DROP,
    position: lab1,
  });

  google.maps.event.addListener(marker, 'click', function(){
      infowindowlab1.open(map,marker);
  });

  marker2 = new google.maps.Marker({
    map:map,
    draggable:false,
    animation: google.maps.Animation.DROP,
    position: lab2
  });
  google.maps.event.addListener(marker2, 'click', function(){
      infowindowlab2.open(map,marker2);
  });
}

google.maps.event.addDomListener(window, 'load', initialize);