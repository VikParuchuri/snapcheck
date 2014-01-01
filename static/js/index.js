$(document).ready(function() {
    var checkURL = "/check/";

    var check = function(event) {
        event.preventDefault();
        var l = Ladda.create($('#info-submit-button')[0]);
        l.start();
        $.ajax({
            type: "POST",
            url: checkURL,
            data: {
                username: $("#username").val(),
                number: $("#phoneNumber").val()
            },
            success: function(data){
                $("#username").empty();
                $("#phoneNumber").empty();
                var infoMessage = $("#info-message");
                var obj = JSON.parse(data);
                if(obj.found == true){
                    infoMessage.removeClass("green");
                    infoMessage.addClass("red");
                } else {
                    infoMessage.removeClass("red");
                    infoMessage.addClass("green");
                }
                infoMessage.html("<p>" + obj.message + "</p>");
            },
            error: function(){
                var infoMessage = $("#info-message");
                infoMessage.removeClass("green");
                infoMessage.addClass("red");
                infoMessage.html("<p>There was an error checking your info.  Please try again later.</p>");
            }
        }).always(function(){
                l.stop();
            });
    };

    $("#info-submit-button").click(check)
});
