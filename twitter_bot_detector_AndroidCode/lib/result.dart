import 'package:fake_follower_detector/home.dart';
import 'package:flutter/material.dart';
class Result extends StatefulWidget {
  @override
  _ResultState createState() => _ResultState();
}

class _ResultState extends State<Result> {
  TextStyle style=TextStyle(color: Colors.blue,fontSize: 18);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: Container(
        padding: EdgeInsets.all(30),
        child: ListView(
          children: [
            SizedBox(height: 20,),
            Center(child: Text(msg,style: TextStyle(color: percent>=60?Colors.red:Colors.green,fontSize: 25),)),
            SizedBox(height: 30,),
            Text('Account Created:   '+result['account_create'],style: style,),
            SizedBox(height: 15,),
            Text('Cover Photo:   '+result['cover_photo'],style: style,),
            SizedBox(height: 15,),
            Text('Frequency of tweets:  '+result['dates_tweet'],style: style,),
            SizedBox(height: 15,),
            Text('Frequency of retweets:   '+result['dates_retweet'],style: style,),
            SizedBox(height: 15,),
            Text('Follower/Following:  '+result['follower_following'],style: style,),
            SizedBox(height: 15,),
            Text("Likes:   "+result['likes'],style: style,),
            SizedBox(height: 15,),
            Text('Profile photo:  '+result['profile_photo'],style: style,),
            SizedBox(height: 15,),
            Text('Source:  '+result['source'],style: style,),
            SizedBox(height: 15,),
            Text('Url in description: ',style: style,),
            if(result['url_linked'].length!=0)
              Text(result['url_linked'][0],style: style,),
            SizedBox(height: 15,),
          ],
        ),
      ),
    );
  }
}
