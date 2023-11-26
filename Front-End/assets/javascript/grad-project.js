var counter = 1;
function duplicate(parent, repeat, loop = 4) {

  if (counter < loop){
    const node = document.getElementById(repeat);
    const clone = node.cloneNode(true);
    document.getElementById(parent).appendChild(clone);

    counter++;
  }
}




function display(show) {
  var x = document.getElementById(show);
  if (x.style.display === "none") {
    x.style.display = "block";
  }
  else {
    x.style.display = "none";
  }


}

function alert_msg(mas){
  window.alert(mas);
}