
init();
function init() {
    var data=[{"bug":'bug'}];
    const Http = new XMLHttpRequest();
    const url = 'http://localhost:5000/get_places';
    Http.open("GET", url,false);
    Http.send();
    data= JSON.parse(Http.response);
    var mymap = L.map('mapid').setView([51.505, -0.09], 13);
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoieXV2YWxoZXIiLCJhIjoiY2s5bGU2eGdwMDNreTNrcnR3ZWt6MDFxMiJ9.2jCmAPMv8fglHt-5kf-sGg', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'your.mapbox.access.token'
    }).addTo(mymap);

    for (var i = 0; i < data.length; i++) {

        var songs="";
        for(var j=0 ; j<data[i].songs.length; j++){
            songs+= "\n"+ data[i].songs[j].song+" - "+data[i].songs[j].artist+"\n";
        }
        var place = data[i].name+"\n";
        var marker = L.marker([data[i].latitude,data[i].longitude])
                .addTo(mymap)
                .bindPopup(`<b>${place} - </b>${songs}`).openPopup();
    }
}