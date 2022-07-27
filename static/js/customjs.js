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

/* type animation */
const carouselText = [
  {text: "Widi Afandi"},
  {text: "Data Enthusiasts"}
]
$( document ).ready(async function() {
  carousel(carouselText, "#feature-text")
});
async function typeSentence(sentence, eleRef, delay = 100) {
  const letters = sentence.split("");
  let i = 0;
  while(i < letters.length) {
    await waitForMs(delay);
    $(eleRef).append(letters[i]);
    i++
  }
  return;
}
async function deleteSentence(eleRef) {
  const sentence = $(eleRef).html();
  const letters = sentence.split("");
  let i = 0;
  while(letters.length > 0) {
    await waitForMs(100);
    letters.pop();
    $(eleRef).html(letters.join(""));
  }
}
async function carousel(carouselList, eleRef) {
    var i = 0;
    while(true) {
      await typeSentence(carouselList[i].text, eleRef);
      await waitForMs(1500);
      await deleteSentence(eleRef);
      await waitForMs(500);
      i++
      if(i >= carouselList.length) {i = 0;}
    }
}
function waitForMs(ms) {
  return new Promise(resolve => setTimeout(resolve, ms))
}