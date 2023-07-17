def create_youtube_video(description,title):
	new_youtube_video={"title":title,"description":description,"likes":0,"dislikes":0,"comments":{}}
	return new_youtube_video


def likes (new_youtube_video):
	if "likes" in new_youtube_video :
		new_youtube_video['likes']+=1
	
	return new_youtube_video


   
def dislikes (new_youtube_video):
	if "dislikes" in new_youtube_video:
		new_youtube_video['dislikes']+=1	
	return new_youtube_video
	

def add_comment(video,username,comment_text):
	video['comments'][username] = comment_text
	return video


video = create_youtube_video("des", "title")
print(add_comment(video, 'jihad', 'says Hi'))
