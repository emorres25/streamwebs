let map;
const path = "m 0,0 c -7.08163,-14.59707 -5.50487,-20.97294 5.18667,-20.97294 " +
           "10.69154,0 12.2683,6.37587 5.18667,20.97294 -2.4156,4.97919 " +
           "-4.74961,9.05306 -5.18667,9.05306 -0.43706,0 -2.77107,-4.07387 " +
           "-5.18667,-9.05306 z";

const initialize = function initialize() {
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: new google.maps.LatLng(site_location.y, site_location.x),
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: false,
        draggable: true,
        clickableIcons: false,
    });

    new google.maps.Marker({
        map: map,
        position: new google.maps.LatLng(site_location.y, site_location.x),
        title: site_name,
        icon: {
          path: path,
          fillColor: "#FF0000",
          fillOpacity: 1,
          strokeColor: "#000000",
          strokeWeight: 2,
        },
    });

    $(window).on('hashchange', listUpdate);
    listUpdate();
};

const listUpdate = function listUpdate() {
    const list = $('#data-sheet-list');
    let page = parseInt(window.location.hash.slice(1), 10) || 1;
    const page_data = JSON.parse(JSON.stringify(sheet_data.slice((page-1)*10, page*10)));

    list.html('');
    for (let datum of page_data) {
        list.append(
            $('<li></li>')
            .addClass('collection-item')
            .append(
                $('<a></a>')
                .attr('href', `/sites/${site_slug}/${datum.uri}/${datum.id}`)
                .text(`${datum.type} data: ${datum.date}`)
            )
        );
    }

    if (page === 1) {
        $('#first-page').removeClass('wave-effects').addClass('disabled');
    } else {
        $('#first-page').addClass('wave-effects').removeClass('disabled');
    }

    if (page === page_count) {
        $('#last-page').removeClass('wave-effects').addClass('disabled');
    } else {
        $('#last-page').addClass('wave-effects').removeClass('disabled');
    }

    $('.page-select').removeClass('active').addClass('wave-effects');
    $(`#page-${page}`).addClass('active').removeClass('wave-effects');
};

$(document).ready(function () {
    initialize();
});
