// var counter = 1;
// function duplicate(parent, repeat, loop = 4) {

//   if (counter < loop){
//     const node = document.getElementById(repeat);
//     const clone = node.cloneNode(true);
//     document.getElementById(parent).appendChild(clone);

//     counter++;
//   }
// }

function containsNumber(str) {
  // Regular expression to check if the string contains a number
  var regex = /\d/;
  
  // Return true if the string contains a number, otherwise false
  return regex.test(str);
}


var count = 1
function duplicate(parent, repeat, loop = 4) {
  if (count < loop){
    // Create a new element
    var newElement = document.createElement('div');
    newElement.innerHTML = document.getElementById(repeat).innerHTML;
    var parentElement = document.getElementById(parent);
    


    var inp  = document.getElementsByTagName("input");
    var arr = Array.from(inp)
    var c = 1;
    var test = 0;
    for (var i = 0; i < arr.length; i++) {
      
      var value = arr[i].getAttribute("name")
      if (containsNumber(value)){
        arr.slice(i, 1)
      }
      else {
        value += c
        arr[i].setAttribute('name', value)
        test++;
      }

      if (test == 3)
        c++;
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