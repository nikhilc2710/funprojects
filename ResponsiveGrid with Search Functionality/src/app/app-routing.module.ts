import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomepageComponent } from './homepage/homepage.component';
import {LoginComponent} from './login/login.component';
import {RegistrationComponent} from './registration/registration.component';

const routes: Routes = [
  {path:"homepage", 
  component:HomepageComponent,
  children:[
    {path:'registration',
      component:RegistrationComponent
    },
    {path:'',
      component:RegistrationComponent
    },
    {path:'advertising',
      component:HomepageComponent
    } ,
    {path:'complaints',
    component:HomepageComponent
  } ,
  ]
  },
  {path:"", component:LoginComponent},
  {path:"cats",component: HomepageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
