document.addEventListener("DOMContentLoaded", function () {
    
    const friendBubbles = document.querySelectorAll(".friendBubble");
    const nav = document.querySelector("nav");
    friendBubbles.forEach(bubble => {
        const random_left = Math.floor(Math.random() * (window.innerWidth - bubble.offsetWidth));
        const random_top = Math.floor(Math.random() * (window.innerHeight - bubble.offsetHeight - nav.offsetHeight)) + nav.offsetHeight;
        const width = bubble.offsetWidth;
        const height = bubble.offsetHeight;
        const bubbleText = bubble.children[0].offsetHeight
        bubble.style.height = (width - bubbleText) + "px";
        bubble.style.top = random_top + "px";
        bubble.style.left = random_left + "px";
        const rgb = [255, 0, 0];
        rgb[0] = Math.round(Math.random() * 255);
        rgb[1] = Math.round(Math.random() * 255);
        rgb[2] = Math.round(Math.random() * 255);
        const brightness = Math.round(((parseInt(rgb[0]) * 299) +
                            (parseInt(rgb[1]) * 587) +
                            (parseInt(rgb[2]) * 114)) / 1000);
        const textColour = (brightness > 125) ? 'black' : 'white';
        const backgroundColour = 'rgb(' + rgb[0] + ',' + rgb[1] + ',' + rgb[2] + ')';
        bubble.style.backgroundColor = backgroundColour
        bubble.style.color = textColour
        bubble.style.boxShadow = `0px 0px 10px 0px ${backgroundColour}`
    });
});