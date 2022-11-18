let keyword = "blackpink";
// let edit_save = document.getElementById("img");
// edit_save.src = "./result/wc-all.png"; 

//search
function compute(select) {
    keyword = document.getElementById("simple-search").value;
    var noOfTweet=10;
    eel.input(keyword, noOfTweet, select);
    // edit(select);
    location.reload();
}

//select sentiment
function computeButton(select) {
    var noOfTweet=10;
    eel.input(keyword, noOfTweet, select);
    // edit(select);
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

// function edit(select)
// {   
//     var inputs = document.myform;
//     inputs[4] = "./result/wc-all.png";
//     inputs[1] = "./result/wc-pos.png";
//     inputs[3] = "./result/wc-neu.png";
//     inputs[2] = "./result/wc-neg.png";

//     edit_save.src = inputs[select];                              
// }
