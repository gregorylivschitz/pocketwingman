$(document).ready(function(){

    $("#enable-hard-mode").click(function(){
        $.get("/pocketwingman/hard_mode");
    });

     $("#enable-easy-mode").click(function(){
        $.get("/pocketwingman/easy_mode");
    });
});