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

class _MyHomePageState extends State<MyHomePage> {
  List <String> articles =new List();
  ScrollController _scrollController= new ScrollController();


  @override
  void initState(){
  super.initState();
  fetchfive();
  _scrollController.addListener(() {
    if (_scrollController.position.pixels==_scrollController.position.maxScrollExtent){
      fetchfive();
    }
  });
  }

  @override
  void dispose(){
    _scrollController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor:  Color(0xff000000),
      
      appBar: AppBar(
        title: const Text('AppBar Demo'),
        backgroundColor:   Color(0xff121212),
      ),
      
      body: SafeArea(
        child:ListView.builder(
            controller: _scrollController,
            itemCount: articles.length,
            itemBuilder: (BuildContext context,int index){
              return Container(
                constraints: BoxConstraints.tightFor(height:500.0),
                child:Card(
                color: Color(0xff121212),
                   shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(30.0),
        ),
        child:Column(
          children: <Widget>[
          Text(articles[index],style:TextStyle(fontSize: 30.5,fontWeight:FontWeight.bold,color:Color(0xff01A0C7)))
          ],
        )

         
                )
              );

            }) ,
    )
    );
    
  }
  fetch () async {
   final response= await http.get("http://10.0.2.2:8000");
   if (response.statusCode == 200){
     setState(() {
       articles.add((json.decode(response.body)['key']));
     });
    
   }
    else{
       throw Exception('Error');
     }
  }
  fetchfive(){
    for (int i=0;i<5;i++){
      fetch();
    }
  }
}
