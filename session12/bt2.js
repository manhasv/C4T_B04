function search() {
    var search_bar = document.getElementById("song_container");
    console.log(search_bar.id);
};
var deleteButtons = document.getElementsByClassName("btnd");
for (var i = 0;i < deleteButtons.length;i++) {
    deleteBtn = deleteButtons[i];
    deleteBtn.addEventListener('click', function(e) {
        var btn = e.target;
        var div = btn.parentNode;
        div.remove();
    });
}
var editButtons = document.getElementsByClassName("btnd");
for (var a = 0; a < editButtons.length; a++) {
    editBtn = editButtons[a];
    editBtn.addEventListener('click', function(e) {
        var btn2 = e.target;
        var div = btn2.parentNode;
        console.log(div[song_id])
    } );
}