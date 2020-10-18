import praw

reddit = praw.Reddit(
    client_id = "tRLX1U8HSRXogA",
    client_secret = "v-7bizF5h9_sWCtRe6X8rhkB2A4",
    user_agent = "joke-of-the-day:v.1 (by /u/deCastillon)"
)

for post in reddit.subreddit("jokes").top("day", limit = 1):

    title = post.title
    body = post.selftext

    print(title + "\n" + body)