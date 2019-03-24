const addClassFunc = (element, nameClass) => {
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

// hightlightBottomDom = document.getElementsByClassName('active');
// if()









