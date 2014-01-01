$(document).ready(function() {

    // Setup backbone sync to use csrf token.
    var CSRF_TOKEN = $('meta[name="csrf-token"]').attr('content');

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    // Synchronous get, not AJAX.
    jQuery.extend({
        getValues: function(url, data, type) {
            var result = null;
            $.ajax({
                url: url,
                type: type,
                async: false,
                data: data,
                success: function(data) {
                    result = data;
                }
            });
            return result;
        }
    });

    // Put CSRF token into jquery post.
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                xhr.setRequestHeader("X-CSRFToken", CSRF_TOKEN);
            }
        }
    });

    function csrf_post(url, data, success, error){
        $.ajax({
            type: "POST",
            url: url,
            data: data,
            success: success,
            error: error
        });
    }

    window.csrf_post = csrf_post;
});