document.addEventListener("DOMContentLoaded",()=>{
    const board = document.getElementById("board")

    board.addEventListener("click", ()=>{
        //show input field
        //create new note in database
        const noteObj = {
            post: button.parentElement.children[1].value,
            id: postId,
          }
        
        console.log(postObj)
        const JSONpostObj = JSON.stringify(postObj);
    
        fetch('/edit', {
        method: 'POST',
        body: JSONpostObj
        })
        .then(resp => resp.json())
        .then(result => {console.log(result);
        });

        //or////////////////////////////////////////////////////////////////

        const likeObj = {
            post_id: postId,
            user_id: user_id.innerHTML
        }

        const JSONlikeObj = JSON.stringify(likeObj)

        fetch('/like', {
            method: "POST",
            body: JSONlikeObj
        })
        .then(resp => resp.json())
        .then(result => {
            if (result.success) {  
                console.log(result);

                button.parentElement.children[0].innerHTML = `Likes: <span id="count_likes">${result.new_likes_count}</span>`
                button.parentElement.children[1].innerHTML = result.like_btn_value
            }
        });

    })
})