/* --- function to hide and reveal the categories --- */
var categories = document.getElementsByClassName("cat-items");
var i;
for (i = 0; i < categories.length; i++) {
  categories[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight){
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    }
  });
}
