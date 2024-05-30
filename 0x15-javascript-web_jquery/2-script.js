// updates the text color of <header> element when user clicks
// on the tag DIV#red_header

'use strict';
$(() => {
  $('DIV#red_header').click(() => {
    $('header').css('color', '#FF0000');
  });
});
