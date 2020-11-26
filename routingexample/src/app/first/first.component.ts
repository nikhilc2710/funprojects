import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'; 

@Component({
  selector: 'app-first',
  templateUrl: './first.component.html',
  styleUrls: ['./first.component.css']
})
export class FirstComponent implements OnInit {

  constructor(private router:Router) { }

  ngOnInit(): void {
  }
   somemethod(){
    console.log("Click works")
    var a="s";
    var b="z";
    if (a=='z' && b=='z'){
      this.router.navigate(['/xx' ]); 

    }
    else{
      var i= document.getElementById('a');
      i.style.display='block'
    }
  }
}
