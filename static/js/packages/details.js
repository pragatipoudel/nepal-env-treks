$(function() {
    // Make itinerary expandable.
    $('#itinerary li').click(function() {
        $(this).toggleClass('expanded');
    });
});
