var style = {
    fillColor: 'white',
    fillOpacity: 1.0,
    weight:0
}

function setColor(id) {
    style.fillColor = photos[id]["hexvalue"];
    colorLayer.setStyle(style);
    }

function getArray(){
    return $.getJSON("data/photodata/colordata.js");
}

var photos;

getArray().done(function(json) {
    photos = json;
});

$( document ).ready(function() {

    $.getJSON("data/photodata/colordata.js", function( data ) {

    var items = [];

    var onclick = 'onclick="setColor(this.id);return false;">'
    
    console.log(onclick);

    $.each( data, function( key, val ) {
        items.push( "<li><a id='" + key + "' href='#'" + onclick + val["datetime"] + "</a></li>" );
    });

    for (var i = 0; i < items.length; i++) {
        console.log(items[i]);
        $("ul").append(items[i]);
        }

    });

});

