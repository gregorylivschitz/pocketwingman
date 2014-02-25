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
    $("#thumbs-up").click(function(){
        console.log("Clicked thumbs up!");
        category_id = $(this).attr("data-category-id");
        $("#id_votes").val("1");
        $.post($("#result_form").attr('action'), $('#result_form').serialize());

        $.get("/pocketwingman/help_me/ajax/" + category_id, function(data){
            $("#user_name").html("<i>Submitted by "+data.user_name+"</i>");
            $("#result_category_result").html(data.category_result);
            $("#result_votes").html(data.result_vote);

        });
    });

    $("#thumbs-down").click(function(){
        console.log("Clicked thumbs Down!");
        category_id = $(this).attr("data-category-id");
        $("#id_votes").val("-1");
        $.post($("#result_form").attr('action'), $('#result_form').serialize());

        $.get("/pocketwingman/help_me/ajax/" + category_id, function(data){
            $("#user_name").html("<i>Submitted "+data.user_name+"</i>");
            $("#result_category_result").html(data.category_result);
            $("#result_votes").html(data.result_vote);
        });
    });

});