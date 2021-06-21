import { Component, OnInit,  ViewEncapsulation } from '@angular/core';

import firebase from 'firebase';
import 'firebase/firestore';

import { FormControl} from '@angular/forms';
import { Router } from '@angular/router'; 
firebase.initializeApp({
  // Firebase Config here
});
var db=firebase.firestore();
var res:object;
var fakedata:object;

export { fakedata};
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./style.scss']
})
export class LoginComponent implements OnInit {
  username=new FormControl();
  Password=new FormControl();


  constructor(private router:Router) { }

  ngOnInit(): void {


//   var dataref = db.collection("shopOwners").doc("Fakedata");
//   dataref.get().then(function(doc) {
//       if (doc.exists) {
//        fakedata=doc.data()
//     } else {
//         // doc.data() will be undefined in this case
//         console.log("No such document!");
//     }
// }).catch(function(error) {
//     console.log("Error getting document:", error);

// });

  
  }// oninit ends
  login_handler(){
    if (this.username.value =="Admin" && this.Password.value  == "123"){
      this.router.navigate(['/homepage' ]); 
    }
    else{
      var lolelm=document.getElementById('lol');
      lolelm.style.display="block"
    }
    
  }

}
