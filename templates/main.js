let keyword = "Twitter";
const noOfTweet = 100;

//search
function compute(select) {
    keyword = document.getElementById("simple-search").value;
    document.cookie = "keyword = "+keyword;
    eel.input(keyword, noOfTweet, select);
    location.reload();
}

//getCookie
function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }

//select sentiment
function computeButton(select) {
    if (getCookie("keyword") != null) {
         keyword = getCookie("keyword");
    }
    eel.input(keyword, noOfTweet, select);
    location.reload();
}

//reload img
function updateImg() {
    var source = '/result/wc-all.png',
        timestamp = (new Date()).getTime(),
        newUrl = source + '?_=' + timestamp;
    document.getElementById("img").src = newUrl;
    setTimeout(update, 1000);
}

