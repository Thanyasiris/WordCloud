let keyword = "blackpink";

function compute(select) {
    keyword = document.getElementById("simple-search").value;
    var noOfTweet=10;
    eel.input(keyword, noOfTweet, select);
}

function computeButton(select) {
    var noOfTweet=10;
    eel.input(keyword, noOfTweet, select);
}

function setValue(res) {
    document.getElementById("abc").src = res;
}
