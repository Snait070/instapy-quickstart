# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'borge_seb'
insta_password = 'gtasan21070'

comments = ['Nice shot! @{}',
        'I love your profile! @{}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
  """ Activity flow """		
  # general settings		
  session.set_dont_include(["jorge20", "tialucia", "morangos"])		
  
  # activity		
  session.like_by_tags(["casas"], amount=10)

  # Joining Engagement Pods
  session.set_do_comment(enabled=True, percentage=35)
  session.set_comments(comments)
  session.join_pods(topic='sports', engagement_mode='no_comments')
