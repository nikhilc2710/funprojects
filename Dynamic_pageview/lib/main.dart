import 'package:flutter/material.dart';

void main() => runApp(new MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return new MaterialApp(
      title: 'Flutter Demo',
      theme: new ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: new MyHomePage(swap: false),
    );
  }
}

class MyHomePage extends StatefulWidget {
  final bool swap;

  MyHomePage({Key key, this.swap}) : super(key: key);

  @override
  _MyHomePageState createState() => new _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  TextEditingController _uri = TextEditingController();
  bool flag = false;

  bool swap = false;

  @override
  void initState() {
    swap = widget.swap;
    super.initState();
  }
  int pages=1;
  @override
  Widget build(BuildContext context) {
    Widget swapWidget;
    if (swap) {
        swapWidget = PageView.builder(
          itemCount: pages,
          onPageChanged: _onPageViewChange,
          controller: PageController(viewportFraction: 0.95),
          itemBuilder: (_, i) {
            return Transform.scale(
              scale: 1,
              child: Card(
                elevation: 6,
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(20)),
                child: Center(
                  child: Text(
                    "Card ${i + 1}",
                    style: TextStyle(fontSize: 32),
                  ),
                ),
              ),
            );
          },
        );
    } else {
      swapWidget = new Card(child: Text('Nothing To show'));
    }

    var swapTile =swapWidget;

    return new Scaffold(
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
                // test();
                setState((){
                  if (!flag){
                  swap = !swap;
                  flag=true;}
                });
              },
              child: Icon(Icons.search),
              shape: CircleBorder(side: BorderSide(color: Colors.transparent)),
            ),
          ],
        ),
      body:swapTile);
  }



  void _onPageViewChange(int page) {
    print("Current Page: " + page.toString());
    int previousPage = page;
    if(page != 0) previousPage--;
    else previousPage = 2;
    if (pages-1 == page){
      setState(() {
        pages++;
      });

    }
    print("Previous page: $previousPage");
  }
}
