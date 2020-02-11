var best_bg_ever = function (urlArray, element) {
    var backgroundImage = "";
    var backgroundSize = "";
    var backgroundPosition = "";

    var totalWidth = element.width();
    var bgCount = urlArray.length;

    for (var i = 0; i < bgCount - 1; i++) {
        backgroundImage = backgroundImage + "url(" + urlArray[i] + "), ";
        backgroundSize = backgroundSize + "auto 100%, ";
        backgroundPosition = backgroundPosition + (totalWidth / bgCount * (bgCount - i - 1)) + "px top, ";
    }

    backgroundImage = backgroundImage + "url(" + urlArray[i] + ")";
    backgroundSize = backgroundSize + "auto 100%";
    backgroundPosition = backgroundPosition + (totalWidth / bgCount * (bgCount - i - 1)) + "px top";

    element.css({
        "background-image": backgroundImage,
        "background-size": backgroundSize,
        "background-position": backgroundPosition,
        "background-repeat": "no-repeat",
    });
};
