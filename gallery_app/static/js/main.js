// const butt = document.getElementById('add-to-favorite')
// console.log(butt.innerText)

$('.favorite').click(function (e) {
    e.preventDefault();
    const pictureId = $(this).data('picture')
    if (this.innerText == 'Favorite') {
        this.innerText = 'UnFavorite'
    } else {
        this.innerText = 'Favorite'
    }
    $.ajax({
        url:  `/api/add_to_favorite/${pictureId}`,
        type: "POST",
        data: {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            if (data.result === 'added') {
                console.log('hello')
            } else {
                console.log('Deleted')
            }

        },
        error: function (data) {
            console.log('error')
        }
    });
})