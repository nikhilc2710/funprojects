import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        backgroundColor: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);
  final String title;
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class Respfromserver {
  final String server_response;

  Respfromserver({this.server_response});

  factory Respfromserver.fromJson(Map<String, dynamic> json) {
    return Respfromserver(
      server_response: json['response'],
    );
  }
}

class _MyHomePageState extends State<MyHomePage> {
  TextEditingController _uri = TextEditingController();
  String x = "Nothing To show";
  String y = "Try Entering Valid URL";

  Future<Respfromserver> result(String url) async {
    final http.Response response = await http.post(
      'http://68f681c83ef5.ngrok.io',
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(<String, String>{
        'url': url,
      }),
    );
    if (response.statusCode == 200) {
      setState(() {
        x = jsonDecode(response.body)['Title'];
        y = jsonDecode(response.body)['Summary'];
      });
      return Respfromserver.fromJson(jsonDecode(response.body));
    } else {
      print('beep boop');
    }
  }

  @override
  Widget build(BuildContext context) {
    var size = MediaQuery.of(context).size;
    final double itemHeight = (size.height - kToolbarHeight - 24) / 2;
    final double itemWidth = size.width;
    return Scaffold(
      backgroundColor: Color(0xff010409),
      resizeToAvoidBottomInset: false,
      appBar: AppBar(
        title: TextField(
          controller: _uri,
          decoration: InputDecoration(
              hintText: 'Enter URL', prefixIcon: Icon(Icons.search)),
        ),
        actions: <Widget>[
          FlatButton(
            textColor: Colors.white,
            onPressed: () {
              test();
            },
            child: Icon(Icons.search),
            shape: CircleBorder(side: BorderSide(color: Colors.transparent)),
          ),
        ],
      ),
      body: SafeArea(
          child: Column(children: <Widget>[

          Text(
        x,
          style: TextStyle(
              color: Color(0xff58a6ff), fontWeight: FontWeight.bold, fontSize: 30),
        ),
        new Expanded(
          // flex:2,
          child: new SingleChildScrollView(
              scrollDirection: Axis.vertical,
              child: Text(
             y,
                style: TextStyle(color: Colors.white, fontSize: 24),
              )),
        ),
      ])),
    );
  }

  test() {
    setState(() {
      result(_uri.text);
      _uri.text = "";
    });
  }
}
