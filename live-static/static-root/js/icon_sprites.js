ymaps.ready(init);

function init () {
    var myMap = new ymaps.Map('map', {
            center: [53.916249, 27.579519],
            zoom: 16
        }),

        myPlacemark1 = new ymaps.Placemark([53.916249, 27.579519], {
            balloonContent: 'Travel Lab'
        }, {
            iconLayout: 'default#image',
            iconImageClipRect: [[0,0], [26, 47]],
            iconImageSize: [15, 27],
            iconImageOffset: [-15, -27],
        });

    myMap.geoObjects.add(myPlacemark1)
}
