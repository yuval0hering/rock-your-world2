var mymap;
var data=[];
var markers=[];
var counter = 0;
function init_map() {
    mymap = L.map('mapid').setView([51.505, -0.09], 4);
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoieXV2YWxoZXIiLCJhIjoiY2s5bGU2eGdwMDNreTNrcnR3ZWt6MDFxMiJ9.2jCmAPMv8fglHt-5kf-sGg', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'your.mapbox.access.token'
    }).addTo(mymap);
}


function add_markers(artist) {
    const Http = new XMLHttpRequest();
    //var artist = document.forms["insertArtist"]["fname"].value;
    var url = 'http://localhost:5000/artist/'+artist;
    if (artist===""){
        url = 'http://localhost:5000/artist/billy+joel'
    }
    Http.open("POST", url);
    Http.send();
    Http.onreadystatechange = (e) => {
        data= JSON.parse(Http.response);
        for (var i = 0; i < data.length; i++) {
            var place = data[i].name+"\n";
            var songs="";
            var songs_link="";
            link="";
            for(var j=0 ; j<data[i].songs.length; j++){
                link=data[i].songs[j].url;
                songs_link += `</b><a href=${link} target="_blank">${data[i].songs[j].song} - ${data[i].songs[j].artist}</a>\n`
            }
            var popup_content= "<b>"+place+" - </b>"+songs_link;
            var icon = chooseIcon();
            markers.push(L.marker([data[i].latitude,data[i].longitude],{icon: icon})
                .addTo(mymap)
                .bindPopup(popup_content).openPopup());
        }
        counter++;
    }
}

document.documentMode = undefined;

function DownloadData() {
 var json_to_download = JSON.stringify(data, 0, 4);
 json_to_download = [json_to_download];
    var blob = new Blob(json_to_download, { type: "text/plain;charset=utf-8" });
    var isIE = !!document.documentMode;
    if (isIE) {
        window.navigator.msSaveBlob(blob, "Places_in_songs.json");
    } else {
        var url = window.URL || window.webkitURL;
        link = url.createObjectURL(blob);
        var a = document.createElement("a");
        a.download = "Places_in_songs.json";
        a.href = link;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    }
}

function ClearMap() {
    data = [];
    for(var i = 0; i < this.markers.length; i++){
        this.mymap.removeLayer(this.markers[i]);
    }
}

function chooseIcon() {
    var colors = [blueIcon, greenIcon , goldIcon, redIcon, violetIcon, orangeIcon, greyIcon, blackIcon, yellowIcon];
    return colors[counter % colors.length];
}
