$(document).ready(function() {
    $('.button-collapse').sideNav();
    $('select').material_select();
    $('.collapsible').collapsible();

    $("#bul").submit(function( event ) {
    event.preventDefault(); //prevent submit action here

    //Condition on checkbox
    if($( "input[name='bank-check']:checked" )){
        $('#bul').click(); //handle submit if condition true
    }
});
  });
