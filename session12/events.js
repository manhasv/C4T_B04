function bodyLoaded() {
    console.log("body loaded")
};
function onMouseover() {
    console.log("mouse over")
};
function test1() {
    document.getElementById("this").style.color = "red";

}
var el = document.getElementById("search1")
console.log(el)
var divs = document.getElementsByTagName("div");
for(var i = 0; i < divs.length; i++) {
    console.log(divs[i]);
}