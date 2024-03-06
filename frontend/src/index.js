import 'foundation-sites'
import 'waypoints/lib/jquery.waypoints';
import 'waypoints/lib/shortcuts/infinite';

import './scss/app.scss';

// TODO: Import photoswipe
// import './js/gallery';

$(document).foundation();

const _infinite = new Waypoint.Infinite({
    element: $('.infinite-container')[0],
    onBeforePageLoad: function () {
        $('.loading-posts').show();
    },
    onAfterPageLoad: function ($items) {
        $('.loading-posts').hide();
    }
})