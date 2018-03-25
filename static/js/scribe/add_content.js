


$(document).ready(function() {
  $.getJSON('http://127.0.0.1:8000/scribe/transitrouteform/',
            function(data) {
                alert('Fetched ' + data.length + ' items!');
            });

    
});






















