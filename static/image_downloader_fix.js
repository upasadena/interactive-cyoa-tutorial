/**
 * Image Background Fix by u/LOLLOL12344
 * 
 * Downloading the CYOA as an image may make the background white. This script
 * should restore it back to normal.
 */

//imports html2canvas...
var test = document.createElement("script")
test.src = "https://html2canvas.hertzen.com/dist/html2canvas.js"
document.body.appendChild(test)

//html2canvas... function...
function download_image(elem) {
  html2canvas(elem, {
    allowTaint: true,
    useCORS: true
  }).then(function (canvas) {
    var link = document.createElement("a");
    document.body.appendChild(link);
    link.download = "html_image.jpg";
    link.href = canvas.toDataURL();
    link.target = "_blank";
    link.click();
  });
}

//execute after loading...
document.getElementsByClassName(
  "mdi-checkbox-marked-circle-outline"
)[0].addEventListener("click", () => {
  setTimeout(() => { //need this since it takes some time to load...

    //sets background...
    var _html_copy = document.getElementsByClassName("v-card__text")[0]
      .firstChild.firstChild;
    _html_copy.style.backgroundImage = document
      .getElementsByClassName("pb-12")[0].style.backgroundImage;
    _html_copy.style.backgroundRepeat = "repeat";

    //gives new_button same look as the old_button
    _old_button = document.getElementsByClassName("v-card__text")[0]
      .parentNode.getElementsByClassName("v-btn__content")[0].parentNode;
    _new_button = document.createElement("button");
    _new_button.innerHTML = _old_button.innerHTML;
    _new_button.className = _old_button.className;
    _new_button.setAttribute("type", "button");
    _new_button.style.color = "black";

    //removes old button and inserts new button
    var _button_parent = _old_button.parentNode;
    _old_button.before(_new_button); //adds _new_button before _old_button
    _button_parent.removeChild(_old_button)

    //fixes titles not showing on images with a negative marginBottom
    _html_copy.getElementsByClassName("mb-0").forEach(v => {
      v.style.position = "relative";
      v.style.zIndex = "11";
    }); //titles
    _html_copy.getElementsByClassName("my-0").forEach(v => {
      v.style.position = "relative";
      v.style.zIndex = "11";
    }); //text
    //maybe add score as well?

    //html2canvas...
    _new_button.setAttribute(
      "onclick",
      "download_image(document.getElementsByClassName('v-card__text')[0].firstChild.firstChild)"
    )
  }, 1000)
});
