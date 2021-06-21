import { Component, OnInit , ViewEncapsulation } from '@angular/core';
import 'firebase/firestore';
import { AngularFirestore  } from '@angular/fire/firestore';
import { Observable } from 'rxjs';


@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css'],
  encapsulation: ViewEncapsulation.None
})



export class RegistrationComponent implements OnInit {
item: Observable<any>;
rejectsx=[];
searchText;

  constructor(private afs: AngularFirestore ) {
}

  ngOnInit(): void { 
    this.item = this.afs.collection('users').valueChanges({ idField: 'customId' });
    this.item.subscribe(
      val => {
        this.rejectsx=val
        console.log(this.rejectsx)
    }
    );
   
  }
  removeCard(index){
    console.log(this.rejectsx[index].email);
    this.rejectsx.splice(index,1)
  }
}

