# Fake-Follower-Detection
Idea : `Fake Followers Detector for twitter` 

Algo :

>> `To check for apt profile picture.` --> `3/10`
			Check if the profile pic has a face ,using OPENCV.
			if the pfp has no face we will consider it as red flag.
			
>> `To check for Regularity of tweets`(also shows and checks retweets) --> `6/10` 
			We will fetch the data acc to:
				tweets in a day, tweets in a week and tweets in a month.
				compare it with some least active accounts(which are surely not bots).
			if the person is too inactive , we will mark it as red flag.
			if the person is too active(100 in a day), we will mark it as a red flag.
>> `Media` --> `3/10`
			Checks for dates on which a photo or anything else is posted.
			If the person less photos then too they should be more than 2 in a month.
			We will fetch the data same way as tweets but the required number will be less.
>> `Likes` --> `4/10`
			We will check the dates from here.
			if the likes in day are null or greater than 40 then we will give a red flag.
>> `Follower/Following` --> `4/10`
			Ratio should be greater > 40 --> Red Flag.
>> `Bio` --> `3/10`
			Bio should be Null. --> Red Flag.
>> `Username` --> `2/10`
			if username contains either of surname or real name --> Green Flag.
			If username is really odd i.e. greater than > 8. --> Red Flag.
>> `Twitter Bot autotweet` --> `10/10`
			should be written for sure as twitter generates it --> Red Flag.

Tech Used : 
>> `Python`,`Selenium`, `OpenCV`
To be updated.

Conclude :

>> Returns Percentage acc to red flags
>> Returns Number of red Flags.
>> Returns rating out of 10.
>> Returns JSON file which shows the juicy info.
