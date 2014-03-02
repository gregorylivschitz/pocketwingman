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
        $.post($("#result_form").attr('action'), $('#result_form').serialize())
            .done(function(  ) {
                console.log("Did Thumbs up post");
                $.get("/pocketwingman/help_me/ajax/" + category_id, function(data){
                console.log("Did Thumbs up get");
                $("#user_name").html("<i>Submitted by " + data.user_name+"</i>");
                $("#result_category_result").html(data.category_result);
                $("#result_votes").html("Votes " + data.result_vote);
                $("#result_views").html("Views " + data.result_views);
                $("#result_form").attr("action", "/pocketwingman/help_me/" + data.category_id + "/" + data.result_id);
                });
            });
    });

    $("#thumbs-down").click(function(){
        console.log("Clicked thumbs Down!");
        category_id = $(this).attr("data-category-id");
        $("#id_votes").val("-1");
        $.post($("#result_form").attr('action'), $('#result_form').serialize())
            .done(function(  ) {
                console.log("Did Thumbs down post");
                $.get("/pocketwingman/help_me/ajax/" + category_id, function(data){
                console.log("Did Thumbs down get");
                $("#user_name").html("<i>Submitted by "+data.user_name+"</i>");
                $("#result_category_result").html(data.category_result);
                $("#result_votes").html("Votes " + data.result_vote);
                $("#result_views").html("Views " + data.result_views);
                $("#result_form").attr("action", "/pocketwingman/help_me/" + data.category_id + "/" + data.result_id);
                });
            });
    });


});