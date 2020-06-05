var data1=[{
    "__type__": "Place",
    "name": "Saigon",
    "songs": [
        {
            "__type__": "Song",
            "song": "Born in the U.S.A.",
            "artist": "Bruce Springsteen",
            "lyrics": "[Verse 1]\nBorn down in a dead man's town\nThe first kick I took was when I hit the ground\nYou end up like a dog that's been beat too much\n'Til you spend half your life just coverin' up\n\n[Chorus]\nBorn in the U.S.A\nI was born in the U.S.A\nI was born in the U.S.A\nBorn in the U.S.A\n\n[Verse 2]\nGot in a little hometown jam\nSo they put a rifle in my hand\nSent me off to a foreign land\nTo go and kill the yellow man\n\n[Chorus]\nBorn in the U.S.A\nI was born in the U.S.A\nI was born in the U.S.A\nI was born in the U.S.A\n\n[Verse 3]\nCome back home to the refinery\nHiring man says, \"Son if it was up to me\"\nWent down to see my V.A. man\nHe said, \"Son, don't you understand\"\n\n[Verse 4]\nI had a brother at Khe Sanh\nFighting off the Viet Cong\nThey're still there, he's all gone\nHe had a woman he loved in Saigon\nI got a picture of him in her arms now\n\n[Verse 5]\nDown in the shadow of the penitentiary\nOut by the gas fires of the refinery\nI'm ten years burning down the road\nNowhere to run ain't got nowhere to go\n\n[Chorus]\nBorn in the U.S.A\nI was born in the U.S.A. now\nBorn in the U.S.A\nI'm a long gone Daddy in the U.S.A. now\nBorn in the U.S.A\nBorn in the U.S.A\nBorn in the U.S.A\nI'm a cool rockin' Daddy in the U.S.A. now",
            "url": "https://genius.com/Bruce-springsteen-born-in-the-usa-lyrics"
        }
    ],
    "latitude": 10.7758439,
    "longitude": 106.7017555
},{
    "__type__": "Place",
    "name": "USA",
    "songs": [
        {
            "__type__": "Song",
            "song": "Born in the U.S.A.",
            "artist": "Bruce Springsteen",
            "lyrics": "[Verse 1]\nBorn down in a dead man's town\nThe first kick I took was when I hit the ground\nYou end up like a dog that's been beat too much\n'Til you spend half your life just coverin' up\n\n[Chorus]\nBorn in the U.S.A\nI was born in the U.S.A\nI was born in the U.S.A\nBorn in the U.S.A\n\n[Verse 2]\nGot in a little hometown jam\nSo they put a rifle in my hand\nSent me off to a foreign land\nTo go and kill the yellow man\n\n[Chorus]\nBorn in the U.S.A\nI was born in the U.S.A\nI was born in the U.S.A\nI was born in the U.S.A\n\n[Verse 3]\nCome back home to the refinery\nHiring man says, \"Son if it was up to me\"\nWent down to see my V.A. man\nHe said, \"Son, don't you understand\"\n\n[Verse 4]\nI had a brother at Khe Sanh\nFighting off the Viet Cong\nThey're still there, he's all gone\nHe had a woman he loved in Saigon\nI got a picture of him in her arms now\n\n[Verse 5]\nDown in the shadow of the penitentiary\nOut by the gas fires of the refinery\nI'm ten years burning down the road\nNowhere to run ain't got nowhere to go\n\n[Chorus]\nBorn in the U.S.A\nI was born in the U.S.A. now\nBorn in the U.S.A\nI'm a long gone Daddy in the U.S.A. now\nBorn in the U.S.A\nBorn in the U.S.A\nBorn in the U.S.A\nI'm a cool rockin' Daddy in the U.S.A. now",
            "url": "https://genius.com/Bruce-springsteen-born-in-the-usa-lyrics"
        }
    ],
    "latitude": 39.7837304,
    "longitude": -100.4458825
}];


init();
function init() {
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
        console.log(data.length);
        var song = data[i].songs[0].song;
        var marker = L.marker([data[i].latitude,data[i].longitude])
                .addTo(mymap)
                .bindPopup(song).openPopup();
 //           options = { index: i };
 //       marker.on("click", onMarkerClickFixedChart, options); // 3rd argument will be passed to 'this' object, when click event occures
    }
    // L.marker([48.2082, 16.3738]).addTo(mymap)
    //     .bindPopup("<b>Vienna</b><br />Vienna - Billy Joel").openPopup();
    // L.marker([10.7758439, 106.7017555]).addTo(mymap)
    //     .bindPopup("<b>Saigon</b><br />Born in the USA - Bruce Springsteen").openPopup();
}