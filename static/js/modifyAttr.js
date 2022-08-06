// remove attribut
function removeAttr(attr) {
  document.getElementById('navbar').classList.remove(attr);
}
// add attribut
function addAttr(attr) {
  document.getElementById('navbar').classList.add(attr);
}
// toggle attribut
function toggleAttr(attr) {
  document.getElementById('navbar').classList.toggle(attr);
}
// change nav to white mode
function nav_white(){
  removeAttr('text-white');
  addAttr('text-blue-1');
  addAttr('bg-white');
}
// btn menus action
function btnChangeColor() {
  if (window.scrollY == 0){
    nav_white();
  }
  toggleAttr('rounded-b-[16px]');
  toggleAttr('shadow-lg');
}