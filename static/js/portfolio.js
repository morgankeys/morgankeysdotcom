$( document ).ready(function() {
    //Google analytics, using jQuery Event API v1.3
    //ga('send', 'event', [category], [action], [label]);

    //Twitter
	$('#twitter_link').on('click', function() {
		ga('send', 'event', 'link', 'click', 'twitter');
	});
	//LinkedIn
	$('#linkedin_link').on('click', function() {
		ga('send', 'event', 'link', 'click', 'linkedin');
	});
	//Resume
	$('#resume_link').on('click', function() {
		ga('send', 'event', 'link', 'click', 'resume');
	});
});

function askme(topic){
	var subject;
	//console.log($(this));
	if (topic == null){
		//var topic = '?subject=Regarding your experience with '+ $(this).children('h3').text();
		//console.log($(this));
		subject = null;
	}else{
		subject = '?subject=Regarding your experience with '+ topic
	}
	window.location.href='mailto:morgankeys+portfolio@gmail.com'+subject;
}


