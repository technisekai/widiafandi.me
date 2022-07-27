const attr = ['bg-white', 'text-blue-1', 'shadow-lg']
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
// btn menus action
function btnChangeColor() {
  attr.forEach(removeAttr);
  removeAttr('text-white');
  toggleAttr('rounded-b-[20px]');
  attr.forEach(toggleAttr);
}