// collapse div
const toggleBtn1 = document.querySelector('#toggleBtn1');
const collapseDiv1 = document.querySelector('#collapseDiv1');
toggleBtn1.addEventListener('click', function() {
  collapseDiv1.classList.remove('collapse');
  collapseDiv1.classList.toggle('collapse');
});

const toggleBtn2 = document.querySelector('#toggleBtn2');
const collapseDiv2 = document.querySelector('#collapseDiv2');
toggleBtn2.addEventListener('click', function() {
  collapseDiv2.classList.remove('collapse');
  collapseDiv2.classList.toggle('collapse');
});

const toggleBtn3 = document.querySelector('#toggleBtn3');
const collapseDiv3 = document.querySelector('#collapseDiv3');
toggleBtn3.addEventListener('click', function() {
  collapseDiv3.classList.remove('collapse');
  collapseDiv3.classList.toggle('collapse');
});
