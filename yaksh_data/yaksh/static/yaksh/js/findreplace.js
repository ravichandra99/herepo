$(document).ready(function(){
    $("body").children().each(function () {
        $(this).html( $(this).html().replace("Summary","Question") );
        $(this).html( $(this).html().replace("Points","Marks") );
    });
});