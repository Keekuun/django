// 当网页向下滑动 50px 出现"返回顶部" 按钮
window.onscroll = function () {
    scrollFunction()
};

function scrollFunction() {
    // console.log(121);
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        document.getElementById("totop").style.display = "block";
    } else {
        document.getElementById("totop").style.display = "none";
    }
}

// 点击按钮，返回顶部
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}


