const button = document.getElementById("favorite");
const pk = button.getAttribute("data-pk");

function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) === ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) === 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}


function toggleFavoriteButton() {
    if (button.innerText === "Add Favorite") {
        button.innerText = "Remove Favorite";
    } else {
        button.innerText = "Add Favorite";
    }
}

async function handleFavorite() {
    const endpoint = `/beer/${pk}/favorite/`;
    const response = await fetch(endpoint, {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        }
    });
    toggleFavoriteButton();
}

button.onclick = handleFavorite;
