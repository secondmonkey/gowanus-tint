var style = {
    fillColor: 'white',
    fillOpacity: 1.0,
    weight:0
}

function setColor(id) {
    style.fillColor = photos[id]["hexvalue"];
    document.body.style.background = style.fillColor;
    colorLayer.setStyle(style);
    }

function showImage(id) {
    var selector = "img#" + id.replace(/\./, "\\\\.");
    $(selector).toggleClass('hidden');
    console.log(selector);
    }

function modPage(id) {
    setColor(id);
    showImage(id);
}

var photos;
var links = [];
var datelinks = {};
var sortable_datelinks = [];
var photolinks = [];

$( document ).ready(function() {

    function getArray(){
        return $.getJSON("data/photodata/colordata.json");
    }

    getArray().done(function(json) {
        photos = json;

        var onclick = 'onclick="modPage(this.id);return false;">'

        $.each( json, function( key, val ) {
            val = val["datetime"].replace(/:/, "/").replace(/:/, "/");
            datelinks[key] = val;
            sortable_datelinks.push([key, datelinks[key]])
        });

        dates_sorted = sortable_datelinks.sort(function(a,b) {return Date.parse(a[1]) - Date.parse(b[1])});

        for (var i = 0; i < sortable_datelinks.length; i++) {
            links.push( "<li><a id='" + sortable_datelinks[i][0] + "' href='#'" + onclick + Date.parse(sortable_datelinks[i][1]).toString('M/d/yyyy hh:mm tt') + "</a></li>" );
            photolinks.push( "<img class='thumb hidden' id=" + sortable_datelinks[i][0] + " src='./data/photodata/images/" + sortable_datelinks[i][0] + "'</img>")
}

        for (var i = 0; i < links.length; i++) {
            $(".photolist").append(links[i]);
            $("#photos").append(photolinks[i]);
        }

        //$('#photos').hide();

    });

});
