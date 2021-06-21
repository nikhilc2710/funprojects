import { Component } from '@angular/core';
import { AngularFirestore } from '@angular/fire/firestore';
import { Observable } from 'rxjs';
import firebase from 'firebase';
import 'firebase/firestore';
import { async } from '@angular/core/testing';
import { NONE_TYPE } from '@angular/compiler';
import {NgControl, FormControl} from '@angular/forms';
import { Router } from '@angular/router'; 



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./style.scss']
})
export class AppComponent {
  title = 'E-Com-Admin';
  items: Observable<any[]>;

 
  
  constructor(afs: AngularFirestore,private router:Router) {}//constructor ends
  ngOnInit() {
   
  
  }//oninit ends


 
}//Appcomonent ends
