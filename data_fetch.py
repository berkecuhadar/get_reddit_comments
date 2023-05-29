import required_config as r
import praw
import json

def getComments(subreddit : str, s_limit : int, replace_limit : int):
    reddit = praw.Reddit(
        client_id = r.id,
        client_secret = r.secret,
        user_agent = r.ue,)
    print("CONNECTED TO CLIENT.")
    print(20*"-")
    parents_dump = []
    comments_dump = []

    subreddit = reddit.subreddit(subreddit)

    hot_subreddit = subreddit.hot(limit=s_limit)
    top_subreddit = subreddit.top(limit=s_limit)
    print("INFROMATION GATHERING")
    print(20*"-")
    for submission in hot_subreddit:
        if not submission.stickied:
            parent_dump = {"Parent ID":str(submission.id), "TITLE": str(submission.title), "UPS": str(submission.ups), "DOWNS":str(submission.downs)}
            parents_dump.append(parent_dump)
            submission.comments.replace_more(limit=replace_limit)
            for comment in submission.comments.list():
                comment_dump = {"Parent ID":str(comment.parent()),"Comment ID":str(comment.id),"Comment":str(comment.body)}
                comments_dump.append(comment_dump)
    print("HOT SUBMISSION HAS BEEN COMPLETED")
    print(20*"-")
    for submission in top_subreddit:
        if not submission.stickied:
            parent_dump = {"Parent ID":str(submission.id), "TITLE": str(submission.title), "UPS": str(submission.ups), "DOWNS":str(submission.downs)}
            parents_dump.append(parent_dump)
            submission.comments.replace_more(limit=replace_limit)
            for comment in submission.comments.list():
                comment_dump = {"Parent ID":str(comment.parent()),"Comment ID":str(comment.id),"Comment":str(comment.body)}
                comments_dump.append(comment_dump)
    print("TOP SUBMISSION HAS BEEN COMPLETED")
    print(20*"-")
    print("MINING HAS BEEN COMPLETED")
    print(20*"-")
    return parents_dump,comments_dump

def json_convert(data1,data2):
    with open("json/parents_dump.json","a") as f:
        json.dump(data1,f,indent=4)
    with open("json/comments_dump.json","a") as f:
        json.dump(data2,f,indent=4)


