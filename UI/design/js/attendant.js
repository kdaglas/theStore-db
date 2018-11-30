/* --- function to change the tab for the attendants --- */
function openAttendant(evt, attendantName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(attendantName).style.display = "block";
    evt.currentTarget.className += " active";
}
  
/* --- this gives a default to one of the divs to alwyas show on loading --- */
document.getElementById("defaultOpen").click();
