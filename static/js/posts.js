/////////////////////////////
// JavaScript for Posts page
/////////////////////////////

$(function() {
    // Executed when js-menu-icon js clicked
    $('.js-menu-icon').click(function() {
        // $(this) : Self element, namely div.js-menu-icon
        // next() : Next to div.js-menu-icon, namely div.menu
        // toggle() : Switch show and hide
        $(this).next().toggle();


    })
})

$(function() {
   // Executed when like js-like js clicked
   $('.like js-like').click(function() {
       // $(this) : Self element, namely div.like js-like
       // next() : Next to div.like js-like, namely div.icon-list
       // toggle() : Switch show and hide
       $(this).next().toggle();
   })
})