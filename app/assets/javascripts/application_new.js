// This is a manifest file that'll be compiled into application.js, which will include all the files
// listed below.
//
// Any JavaScript/Coffee file within this directory, lib/assets/javascripts, vendor/assets/javascripts,
// or any plugin's vendor/assets/javascripts directory can be referenced here using a relative path.
//
// It's not advisable to add code directly here, but if you do, it'll appear at the bottom of the
// compiled file.
//
// Read Sprockets README (https://github.com/rails/sprockets#sprockets-directives) for details
// about supported directives.
//
//= require jquery
//= require jquery_ujs
//= require turbolinks
//= require_tree .
// $('.dropdown-toggle').dropdown()
//
// // $( document ).ready(function() {
// //
// //
// // $('h1').hide();
// // });
//
//
//

// $(function(){
//   $('form#query_form').submit(function(){
//     $('button#query_myButton').prepend('<span class="glyphicon glyphicon-refresh spinning"></span>');
//     $('div#goatdiv').prepend('<p>Please be patient...Word Herd is scrapping the webs. In the meantime, check out some awesome videos?!?</p><ul><li><a href="https://www.youtube.com/watch?v=gEaAmUDEiGo">video 1</a></li><li><a href="https://www.youtube.com/watch?v=ELvsokKcydM">video 2</a></li><li><a href="https://www.youtube.com/watch?v=_yaTmPHdZVM">video 3</a></li></ul>')
//   });
//
//
//
// });
// $(document).ready(function() {
//     $('form#query_form').keyup(function() {
//
//         var empty = false;
//         $('.query_field input').each(function() {
//             if ($(this).val().length == 0) {
//                 empty = true;
//             }
//         });
//
//         if (empty) {
//             $('.form-group button').attr('disabled', 'disabled');
//         } else {
//             $('.form-group button').removeAttr('disabled');
//         }
//     });
// });
$(document).ready(function() {
    $('form#query_form').keyup(function() {

        var empty = false;
        $('.query_field input').each(function() {
            if ($(this).val().length == 0) {
                empty = true;
            }
        });

        if (empty) {
            $('.form-group button').attr('disabled', 'disabled');
        } else {
            $('.form-group button').removeAttr('disabled');
        }

    });





});

$('form#query_form').submit(function(){
  $('button#query_myButton').prepend('<span class="glyphicon glyphicon-refresh spinning"></span>');
  $('div#goatdiv').prepend('<p>Please be patient...Word Herd is scrapping the webs. In the meantime, check out some awesome videos?!?</p><ul><li><a href="https://www.youtube.com/watch?v=gEaAmUDEiGo">video 1</a></li><li><a href="https://www.youtube.com/watch?v=ELvsokKcydM">video 2</a></li><li><a href="https://www.youtube.com/watch?v=_yaTmPHdZVM">video 3</a></li></ul>')
});
