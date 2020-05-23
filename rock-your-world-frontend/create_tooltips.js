var _ = require("lodash")


let tooltips = [];
let json_places = JSON.parse( [{
        "__type__": "Place",
        "name": "USA",
        "songs": [
            {
                "__type__": "Song",
                "song": "Born in the U.S.A.",
                "artist": "Bruce Springsteen"
            }
        ],
        "latitude": 39.7837304,
        "longitude": -100.4458825
    },
    {
        "__type__": "Place",
        "name": "Saigon",
        "songs": [
            {
                "__type__": "Song",
                "song": "Born in the U.S.A.",
                "artist": "Bruce Springsteen"
            }
        ],
        "latitude": 10.7758439,
        "longitude": 106.7017555
    }]);
places= _.chunk(json_places,1)
// for (let i in json_places) {
// tooltips.push(L.marker([places[i].latitude, places[i].longitude]).addTo(mymap)
// .bindPopup("<b></b>places[i].name<br />Vienna - Billy Joel").openPopup());
// }
