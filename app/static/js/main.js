var map, points, frame_rectangle;



function dict_to_url(dict) {
    var str = "";
    for (var key in dict) {
        if (dict.hasOwnProperty(key)) {
            str += "" + key + "=" + dict[key] + "&"
        }
    }
    return str.substring(0, str.length - 1)
}

function create_infowindow(point){
    var str = '<div id="content">'+
        '<h1 id="firstHeading" class="firstHeading">' + point.name + '</h1>'+
        '<div id="bodyContent">'+
        '<p>' +
        point.description  +
        '</p>'+
        '</div>'+
        '</div>';
    console.log(str)
    return new google.maps.InfoWindow({
        content: str,
    })
}


function marker_click(small_point, marker) {
    console.log(small_point);
    console.log(marker);
    // $.ajax({
    //     url: '/api/points/point_' + small_point.id,
    //     dataType: "json",
    //     success: function (responce) {
    //         point = responce.point;
    //         var iw = create_infowindow(point);
    //         iw.open(map, marker);
    //     } ,
    //     error: function (responce) {
    //         console.log(responce);
    //     }
    // });
    alert('test');
}

function map_changed(){
    frame_rectangle.setOptions({
        map: map,
        fillOpacity: 0,
        strokeOpacity: 0,
        bounds: map.getBounds()
    });

    params = {
        min_lat: frame_rectangle.bounds.f.f,
        max_lat: frame_rectangle.bounds.f.b,
        min_lng: frame_rectangle.bounds.b.b,
        max_lng: frame_rectangle.bounds.b.f,
    };
    $.ajax({
        url: '/api/most_rated?' + dict_to_url(params),
        dataType: "json",
        success: function (responce) {

            console.log(responce);
            var points = responce.points;
            points.forEach(function (point, i, arr) {
                var p = new google.maps.Marker({
                    map: map,
                    position: {
                        lat: point.lat,
                        lng: point.lng,
                    },
                    title: point.name,
                });
                p.addListener('click', marker_click);

                // p.addListener('click',
                //             var i_w = create_infowindow(point);
                //             i_w.open(map, p);
                //             alert('clicked');
                //         })
            });
        } ,
        error: function (responce) {
            console.log(responce);
        }
    })

}

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat:  50.4155171, lng: 30.5457314},
        // 50.4155171,30.5457314
        zoom: 11,
    });

    frame_rectangle = new google.maps.Rectangle();

    map.addListener('zoom_changed', map_changed)
    map.addListener('idle', map_changed)

}

$(document).ready(function () {
    $.ajax({
        url: '/api/most_rated',
        dataType: "json",
        success: function (responce) {

            console.log(responce);
            var points = responce.points;
            points.forEach(function (point, i, arr) {
                var p = new google.maps.Marker({
                map: map,
                position: {
                    lat: point.lat,
                    lng: point.lng,
                },
                title: point.name,
            });
            });

            // var test_point = new google.maps.Marker({
            //     map: map,
            //     position: {
            //         lat: point.lat,
            //         lng: point.lng,
            //     },
            //     title: point.name,
            // });

        } ,
        error: function (responce) {
            console.log(responce);
        }
    })

})


