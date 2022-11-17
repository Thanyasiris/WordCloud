let keyword = "blackpink";

//search
function compute(select) {
    keyword = document.getElementById("simple-search").value;
    var noOfTweet=10;
    eel.input(keyword, noOfTweet, select);
    location.reload();
}

//select sentiment
function computeButton(select) {
    var noOfTweet=10;
    eel.input(keyword, noOfTweet, select);
    location.reload();
}

function updateImg() {
    var source = '/result/wc-all.png',
        timestamp = (new Date()).getTime(),
        newUrl = source + '?_=' + timestamp;
    document.getElementById("img").src = newUrl;
    setTimeout(update, 1000);
}
