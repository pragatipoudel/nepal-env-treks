$(function() {

    // Convert all select inputs to selectize inputs.
    $('select').selectize();

    // Make itinerary expandable.
    $('#itinerary li').click(function() {
        $(this).toggleClass('expanded');
    });
});
