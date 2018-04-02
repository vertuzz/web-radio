// TODO: refactor to MVC or to use Vue.js

var textarea = $("#current_playlist");


$(document).ready(function () {

    getPlaylist();

    $("#updatePlaylist").click(setPlaylist)

});



function showPlaylist(data) {

    var playlist = '';

    $.each(data, function (index, val) {
        playlist += val['file'] + '\n'
    });

    textarea.val(playlist);
}


function getPlaylist() {
    $.ajax({
      dataType: "json",
      url: '/get_curr_playlist',
      success: function (data) {
          showPlaylist(data)
      }
    });
}

function setPlaylist() {
    var data = textarea.val();

    data = data.split('\n');

    $.each(data, function (i, v) {
        if (v.length === 0) {
            data.splice(i, 1)
        }
    });

    $.ajax({
      dataType: "json",
      url: '/set_playlist',
      method: "POST",
      data: JSON.stringify(data),
      success: function (res) {
          console.log(res)
      }
    });
}
