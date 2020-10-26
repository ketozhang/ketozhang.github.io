// // $(document).ready(function () {
// //     $(".datetime").each(function (i, datetime) {
// //         let isoDate = datetime.innerHTML;
// //         localDate = new Date(isoDate);
// //         datetime.innerHTML = localDate.toLocaleString([], { formatMatcher: 'basic' });
// //     });
// // });

$(document).ready(function () {
    $("time").each(function (i, time) {
        var datetime = $(time).attr('datetime')
        if (datetime !== null) {
            var date = new Date(datetime)
            var date_string = date.toLocaleString('en-us', { year: 'numeric', month: '2-digit', day: '2-digit' })
            $(time).text(date_string)
        }
    })
})

// $(document).ready(function () {
//     const months = [
//         'January',
//         'February',
//         'March',
//         'April',
//         'May',
//         'June',
//         'July',
//         'August',
//         'September',
//         'October',
//         'November',
//         'December'
//       ]

//     $("time").each(function (i, datetime) {
//         let isoDate = $(datetime).attr('datetime') + "Z";
//         localDate = new Date(isoDate);
//         localDateString = `${months[localDate.getMonth()]} ${localDate.getDay()}, ${localDate.getFullYear()}`
//         console.log(localDate)
//         $(datetime).html(localDateString)
//         // $(datetime).html(localDate.toLocaleString([], { formatMatcher: 'basic' }));
//     });
// });