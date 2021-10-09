import { Component, HostListener } from '@angular/core';
import { OffersService } from './offers.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'AdvertisementsAPP';
  original_data: any
  data: any
  item_details: any
  filterValue: any
  
  constructor(private offer:OffersService){
    this.offer.getData().subscribe(data=>{
      console.warn(data)
      this.data=data;
      this.original_data=data;
    })
  }
  public details(item: any) {
    alert('ID: ' + item.id + '\nTitle: ' + item.title + '\nPrice: ' + item.price + '\nCategory ID: ' + item.category_id)
  }

  public applyFilter() {
    this.filterValue = (<HTMLInputElement>document.getElementById('myInput')).value;
    this.data = this.original_data
    if(this.filterValue !== ''){
      this.data = this.data.filter((item: any) => item.category_id as string == this.filterValue)
    }
  }
}
