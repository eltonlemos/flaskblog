$(function(){
	var postid="{{post.id}}"
	$('button').click(function(){
		$.ajax({
            url: "{{ url_for('posts.like_post', post_id=post.id) }}",
            type: 'post',
            data: {postid:postid,type:1},
            dataType: 'json',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
