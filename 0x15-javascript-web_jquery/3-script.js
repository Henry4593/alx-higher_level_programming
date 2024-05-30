/* adds the class red to the <header> element when the user clicks on the tag
 DIV#red_header
*/

'use strict';
$(() => {
  $('DIV#red_header').click(() => {
    if (!$('header').hasClass('red')) {
      $('header').addClass('red');
    }
  });
});
