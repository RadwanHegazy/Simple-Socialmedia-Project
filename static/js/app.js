$('.love-form').submit(function(e){
    e.preventDefault()
    var PostId = $(this).attr('id')

    var url = $(this).attr('action')
    var likeText = $(`.btn-${PostId}`).text()
    var TotalLikes = $.trim(likeText)
    var Likes = parseInt(TotalLikes)

    let res;
     
    $.ajax({
        url:url,
        type:"POST",
        data:{
            'postid' : PostId,
            'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(done) {
            if (done['loged'] === false) {
               window.location.href = '/login/'
            }
            else{

                if (done['liked'] === true) {
                    $(`.btn-${PostId}`).text(` ${Likes + 1}`)
                    document.querySelector(`.btn-${PostId}`).className = `fas fa-heart btn-${PostId}`
                }else {
                    $(`.btn-${PostId}`).text(` ${Likes - 1}`)
                    document.querySelector(`.btn-${PostId}`).className = `far fa-heart btn-${PostId}`
                    
                }
            }
        },
        error:function(error){
            console.log('Error', error)
        }
    })
})


