document.addEventListener("DOMContentLoaded", function () {
    const friendBubbles = document.querySelectorAll(".friendBubble");
    const nav = document.querySelector("nav");

    friendBubbles.forEach(bubble => {
        const random_left = Math.floor(Math.random() * (window.innerWidth - bubble.offsetWidth));
        const random_top = Math.floor(Math.random() * (window.innerHeight - bubble.offsetHeight - nav.offsetHeight)) + nav.offsetHeight;
        const random_color_1 = Math.floor(Math.random() * 255)
        const random_color_2 = Math.floor(Math.random() * 255)
        const random_color_3 = Math.floor(Math.random() * 255)
        const width = bubble.offsetWidth;
        bubble.style.height = (width - bubble.style.fontSize - bubble.children[0].offsetHeight) + "px";
        bubble.style.top = random_top + "px";
        bubble.style.left = random_left + "px";
        bubble.style.backgroundColor = `rgba(${random_color_1}, ${random_color_2}, ${random_color_3})`
        // bubble.style.color = `rgba(${random_color_1/2}, ${random_color_2/2}, ${random_color_3/2})`
        bubble.style.boxShadow = `0px 0px 10px 0px rgba(${random_color_1}, ${random_color_2}, ${random_color_3}, 1)`
    });
});

// position random

// color random 