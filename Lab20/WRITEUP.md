# 1. The timeout Trap 
# A timeout doesnt mean that the server failed. A timeout just measn that the client # has stopped waiting. The server is still running all the grading in the background, # and will finish its task even though the client timedout. 
# 2. Naming your intent 
# If the key was random ever time, the retries would never accually do anything, and # prevent duplicate grading like it supposed to. This would happen becasue the server # thinks ever request is a new one. A stable ID however will work perfectly fine     # because it has the same requests ever time.
# 3. Synce vs. Async
# API should be using sync when the rsult is coming fast, and is ready very quickly. # They should use async when the task is a little longer, or could possibly timeout. # This is becasue async lets the server respond quickly, while it just finished the  # task in the background. 
# 4. Hidden state 
# The hidden state that I expierenced in this lab was the server still being able to # work even when the client timed out. Even though this was happening in the         # background, we couldn't see it until we did the work and added logs ane job        # tracking. What we did, adding the jobs and logs tracking, is what makes the hidden # state, all the work, visible so we can see it. 