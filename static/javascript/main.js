function addClassFunc (element, nameClass) {
  element.classList.add(nameClass);
}

// console.log(window.location)
pointArrowDOM = document.getElementsByClassName('number_point_arrow');
if ( window.location.pathname === '/home' || window.location.pathname === '/home/1' ) {
  addClassFunc(pointArrowDOM[0], 'a1')
} else {
  currentPage = parseInt(window.location.pathname.replace('/home/', ''));
  // console.log(currentPage);
  addClassFunc(pointArrowDOM[currentPage-1], 'a1')
}

let headerRight = document.getElementById("header_right")
let btnSwitch1 = headerRight.getElementsByTagName("a")[0]
let btnSwitch2 = headerRight.getElementsByTagName("a")[1]
if(window.location.pathname === '/home'){
  addClassFunc(btnSwitch2,"left")
}
// console.log(window.location.pathname)
else if(window.location.pathname === '/'){
  addClassFunc(btnSwitch1,"left")
}

function onClickHandler(){
  addClassFunc(btnSwitch1,"left")
  btnSwitch2.className = `login text_style`
}

function onClickHandler2(){
  addClassFunc(btnSwitch2,"left")
  // console.log(window.location.pathname)
  btnSwitch1.className = `login text_style`

}

// hightlightBottomDom = document.getElementsByClassName('active');
// if()









