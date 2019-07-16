
# Project: COMechBot
# Authors: /u/KeebsAndTrees and /u/mechanically_minded

import praw
import re
import time
import os
# create the objects from the importsd modules

# Reddit api login


def bot_login():
    try:
        print('Logging in...')
        r = praw.Reddit(client_id='wqppgR-ndAYbWQ',
                        client_secret='fdqOswWb-8ydPKhkYWLV0lyjCX4',
                        username='ColoradoMechBot',
                        password='colorado',
                        user_agent="keebsandtrees' CO Mech Meet bot v0.1",)
        print('Login Successful\n')
        return r
    except Exception as e:
        print(e)
        # os.system('/home/pi/Desktop/RedditBot/pushbullet.sh "MechBot crashed. Error message is: "' + e.message)
        # fix that directory to get updates through pb.
        time.sleep(60)


def find_users(subreddit_name, contacted_list):
    print('Sorting through 500 most recent submissions.\n')
    for submission in subreddit_name.new(limit=500):
        if "[US-CO]" in submission.title and submission.author not in contacted_list:
            redditor_username = ("\n" + str(submission.author))
            contacted_list.append(submission.author)
            r.redditor(redditor_username).message('Colorado Mech Meetup!','Hey I noticed you are from Colorado. Did you know /u/KeebsAndTrees hosts a monthly CO Keyboard meet!? Come check out our [discord](https://discord.gg/FACZyp9) for more info.', from_subreddit=None)
            with open("contacted_list.txt", "a") as f:
                f.write(str(submission.author) + "\n")
                print("User: ", submission.author, " added to contacted list.\n")
                # os.system('/home/pi/Desktop/RedditBot/pushbullet.sh "Contact added: "' + str(submission.author))
                # fix that directory to get updates through pb.
    print("No results found \nSleeping for 30 minutes.")
    time.sleep(1800)
    # os.system('/home/pi/Desktop/RedditBot/pushbullet.sh "No contacts found: Retrying in 30mins "')
    # fix that directory to get updates through pb

def main(r):
    subreddit = r.subreddit('MechMarket')
    contacted_list = get_contacted_list()
    try:
        find_users(subreddit, contacted_list)
    except praw.exceptions.APIException as e:
        if e.error_type == "RATELIMIT":
            print(e.message)
            delay = re.search("(\d+) minutes?", e.message)
            if delay:
                delay_seconds = float(int(delay.group(1)) *60)
                print("Sleeping for " + ((str)(delay_seconds/60)) + " minutes")
                time.sleep(delay_seconds)
            else:
                delay_seconds = float(delay.group(1))
                delay = re.search("(\d+) seconds" , e.message)
                print("Sleeping for " + ((str)(delay_seconds)) + " seconds")
                time.sleep(delay_seconds)
                
         
def get_contacted_list():
    if not os.path.isfile("contacted_list.txt"):
        contacted_list = []
        print("List unable to be found")
    else: 
        with open("contacted_list.txt", "r") as f:
            contacted_list = f.read()
            contacted_list = contacted_list.split("\n")
            print("Contact list verified\n")
            # contacted_list = filter(None, contacted_list)
        
    return contacted_list

    
if __name__ == '__main__':
    
    while True:
        try:
            r = bot_login()
            main(r)
        
        except Exception as e:
            print(e)
            # os.system('/home/pi/Desktop/RedditBot/pushbullet.sh "MechBot crashed. Error message is: "' + e.message)
            # fix that directory to get updates through pb.
            time.sleep(60)
