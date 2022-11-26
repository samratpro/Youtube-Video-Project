#pip install google-api-python-client
#https://console.cloud.google.com/apis/api/youtube.googleapis.com/credentials


from googleapiclient.discovery import build
def youtubevid(self):
    youtube = build('youtube', 'v3', developerKey='AIzaSyCd9r6YUMPcJk9wMxxg4spI6ATySesPXBo')
    # Print the total number of results
    try:
      request = youtube.search().list(q=self, part='snippet', type='video', maxResults=1)
      res = request.execute()
      id = res['items'][0]['id']['videoId']
      youtube_url = '<!-- wp:html --><figure  style="text-align: center"><iframe width="640" height="360" src="https://www.youtube.com/embed/' + id + '?rel=0&amp;enablejsapi=1"></iframe></figure><!-- /wp:html --><!-- wp:separator {"align":"center"} --><hr class="wp-block-separator aligncenter"/><!-- /wp:separator -->'
    except:
      youtube_url = ''
      print('Youtube API Has Been Finished')
    return youtube_url


print(youtubevid('funny video'))
