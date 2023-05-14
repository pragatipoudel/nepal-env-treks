// function convertToRangeSlider(
//     sliderQuerySelector,
//     inputQuerySelector,
//     min,
//     max,
//     prefix='',
//     step=1,
// ) {
//     const valuesString = $(inputQuerySelector).val();
//     const values = (valuesString === 'Any') ? [min, max] : valuesString.split(' to ').map((v, index) => {
//         if (v === 'Any') {
//             return (index === 0) ? min : max;
//         }
//         return +v.replace(prefix, '')
//     });

//     $(sliderQuerySelector).slider({
//         range: true,
//         min, max,
//         values, step,
//         slide: function (event, ui) {
//             const minVal = (ui.values[0] === min) ? 'Any' : `${prefix}${ui.values[0]}`;
//             const maxVal = (ui.values[1] === max) ? 'Any' : `${prefix}${ui.values[1]}`;
//             if (minVal === maxVal) {
//                 $(inputQuerySelector).val(minVal);
//             } else {
//                 $(inputQuerySelector).val(`${minVal} to ${maxVal}`);
//             }
//         },
//     });
// }

// $(function() {
//     // Days and price range sliders.
//     convertToRangeSlider(
//         'aside .slider.days',
//         'aside .slider-input.days',
//         0, 200, '', 10
//     );
//     convertToRangeSlider(
//         'aside .slider.price',
//         'aside .slider-input.price',
//         0, 3000, '$', 200,
//     );
// });
