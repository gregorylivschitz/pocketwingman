$(document).ready(function(){

    $("[name='my-checkbox']").bootstrapSwitch();

    $('#enable-easy-mode-switch').on('switchChange', function (e, data) {
        var $element = $(data.el),
        value = data.value;
        console.log(e, $element, value);
        if (value) {
            console.log("In hard mode");
            $.get("/pocketwingman/hard_mode");
        }
        else {
            console.log("In easy mode");
            $.get("/pocketwingman/easy_mode");
        }

    });
});