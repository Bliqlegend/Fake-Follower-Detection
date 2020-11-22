import 'dart:convert';
import 'dart:convert';
import 'dart:ui';
import 'package:fake_follower_detector/result.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:http/http.dart' as http;

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}
var username = TextEditingController();
bool load = false;
String msg='';
int percent = 0;
var result;
class _HomeState extends State<Home> {
  GlobalKey<ScaffoldState> _scaffoldkey = GlobalKey<ScaffoldState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: _scaffoldkey,
      body: load ? Container(child: Center(child: CircularProgressIndicator(backgroundColor: Colors.black,),),color: Colors.blue,height: double.infinity,width: double.infinity,)
          :AnnotatedRegion<SystemUiOverlayStyle>(
        value: SystemUiOverlayStyle.light,
        child: Stack(
            children: <Widget>[
              Container(
                height: double.infinity,
                width: double.infinity,
                decoration: BoxDecoration(
                    gradient: LinearGradient(colors: [
                      Colors.blue.shade200, Colors.blue.shade800
                    ], begin: Alignment.topCenter, end: Alignment.bottomCenter)
                ),
              ),
              Container(
                  height: double.infinity,
                  child: SingleChildScrollView(
                    physics: AlwaysScrollableScrollPhysics(),
                    padding: EdgeInsets.symmetric(
                      horizontal: 40.0,
                      vertical: 120.0,
                    ),
                    child: Column(
                      children: [
                        Text("Twitter Bot detector", style: TextStyle(
                          color: Colors.white,
                          fontSize: 50,
                          fontFamily: 'Billabong',),),
                        SizedBox(height: 60,),
                        TextField(
                          controller: username,
                          decoration: InputDecoration(
                            prefixIcon: Icon(
                              Icons.person, color: Colors.white,),
                            hintText: "Enter twitter Username",
                            labelText: "Username",
                            contentPadding: EdgeInsets.only(top: 15),
                            hintStyle: TextStyle(color: Colors.black),
                            labelStyle: TextStyle(color: Colors.white),
                          ),
                        ),
                        SizedBox(
                          height: 40,
                        ),
                        Container(
                          width: double.infinity,
                          child: RaisedButton(
                              color: Colors.white,
                              shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(30)),
                              elevation: 5,
                              onPressed: () {
                                print('working');
                                apicall(username.text);
                                username.text = '';
                                //Navigator.of(context).push(MaterialPageRoute(builder: (context)=>Result()));

                              },
                              child: Text("Search", style: TextStyle(
                                  color: Colors.blue, letterSpacing: 1.5),)),
                        ),
                        SizedBox(height: 50,),
                        if(msg!='')
                        RaisedButton(child: Text('Click to view the result',style: TextStyle(color: Colors.white),),
                            onPressed:(){Navigator.of(context).push(MaterialPageRoute(builder: (context)=>Result()));}
                        ,color:Colors.red)
                      ],
                    ),
                  ))
            ]
        ),
      ),
    );
  }

  void apicall(String username) async {
    setState(() {
      load = true;
    });
    try {
    http.Response res = await http.get(
        'http://192.168.1.209:5000/apicall?Query=' + username);
    setState(() {
      result = json.decode(res.body);
    });
    print(result);
    if (result['status'] == 'failure') {
      setState(() {
        load = false;
        msg='';
      });
      _scaffoldkey.currentState.showSnackBar(SnackBar(
        content: Text("No account exist",),
        duration: Duration(seconds: 8),
        backgroundColor: Colors.red,));
    }
    else {
      if (result['source'] == 'twitter bot autotweet') {
        setState(() {
          percent = 100;
        });
      }
      else {
        setState(() {
          percent = 20 * int.parse(result['flags'].toString());
        });
      }
      print(percent);
      if(percent>=60){
        msg=username+' account is a bot';
      }
      else{
        setState(() {
          msg=username+" account is not a bot";
        });
      }
    }
    }
    catch (Exception) {
      setState(() {
        msg='';
      });
    }
    setState(() {
      load=false;
    });
  }
}
