function apiCall(method, path, params, cb) {
    var timeout = 300000; // 5 mins is enough

    $.ajax({
        timeout: timeout,
        url: "api/" + path,
        method: method,
        cache: false,
        data: params,
        success: function(data) {
            cb(jQuery.parseJSON(data));
        },
        error: function(xhr, status, data) {
            if (status == "timeout") {
                return cb({ error: "Query timeout after " + (timeout / 1000) + "s" });
            }
            cb(jQuery.parseJSON(xhr.responseText));
        }
    });
}

$(function() {
  var container = document.getElementById('visualization');

  apiCall("post", "get_jnfdc", null, function(data) {
    var items = new Array();
    $.each(data.rows, function(i, row){
      var item = {};
      item.x = row.date;
      item.y = row.signnum;
      var label = {'content' : row.signnum.toString()};
      item.label = label;
      items.push(item);
    });

    var options = {
    };
    var dataset = new vis.DataSet(items);
    var graph2d = new vis.Graph2d(container, dataset, options);
  });
});
