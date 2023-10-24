let userId = "{{user.id}}";
    let board = document.querySelector("#board");
    function buildFriends(){
        let url = `http://localhost:8000/api/users/${userId}`

        fetch(url)
        .then((resp)=>resp.json())
        .then(function(data){
            let list = data['friends']
            list.forEach(function(url){
                fetch(url)
                .then((resp)=>resp.json())
                .then(function(friend){
                    const nav = document.querySelector("nav");
                    anchorBubble = document.createElement('a')
                    anchorBubble.href = `http://localhost:8000/friends/${friend.id}`
                    anchorBubble.classList.add('friendBubble')
                    textBubble = document.createElement('p')
                    textBubble.innerHTML = `${friend.first_name} ${friend.last_name}`
                    anchorBubble.appendChild(textBubble)
                    board.appendChild(anchorBubble)
                    
                    const random_left = Math.floor(Math.random() * (window.innerWidth - anchorBubble.offsetWidth));
                    const random_top = Math.floor(Math.random() * (window.innerHeight - anchorBubble.offsetHeight - nav.offsetHeight)) + nav.offsetHeight;
                    
                    const width = anchorBubble.offsetWidth;
                    const height = anchorBubble.offsetHeight;
                    const bubbleText = anchorBubble.children[0].offsetHeight
                    anchorBubble.style.height = (width - bubbleText) + "px";
                    anchorBubble.style.top = random_top + "px";
                    anchorBubble.style.left = random_left + "px";
                    const rgb = [255, 0, 0];
                    rgb[0] = Math.round(Math.random() * 255);
                    rgb[1] = Math.round(Math.random() * 255);
                    rgb[2] = Math.round(Math.random() * 255);
                    const brightness = Math.round(((parseInt(rgb[0]) * 299) +
                                        (parseInt(rgb[1]) * 587) +
                                        (parseInt(rgb[2]) * 114)) / 1000);
                    const textColour = (brightness > 125) ? 'black' : 'white';
                    const backgroundColour = 'rgb(' + rgb[0] + ',' + rgb[1] + ',' + rgb[2] + ')';
                    anchorBubble.style.backgroundColor = backgroundColour
                    anchorBubble.style.color = textColour
                    anchorBubble.style.boxShadow = `0px 0px 10px 0px ${backgroundColour}`
                })

            })
        })
    }
    buildFriends()