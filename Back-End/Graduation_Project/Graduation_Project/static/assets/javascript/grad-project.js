// var counter = 1;
// function duplicate(parent, repeat, loop = 4) {

//   if (counter < loop){
//     const node = document.getElementById(repeat);
//     const clone = node.cloneNode(true);
//     document.getElementById(parent).appendChild(clone);

//     counter++;
//   }
// }


var count = 1
function duplicate(parent, repeat, loop = 4) {
  if (count < loop){
    // Create a new element
    var newElement = document.createElement('div');
    newElement.innerHTML = document.getElementById(repeat).innerHTML;

    var parentElement = document.getElementById(parent);


    var inp = document.getElementsByTagName("input");
    for (var i = 0; i < inp.length; i++) {
        
        var value = inp[i].getAttribute("name")
        inp[i].setAttribute('name', value+count)
    }

    parentElement.appendChild(newElement);
    count++;
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