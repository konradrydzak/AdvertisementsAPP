import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'
@Injectable({
    providedIn: 'root'
})
export class OffersService {
    constructor(private http:HttpClient) { }

    getData()
    {
        let api_url="http://host.docker.internal:8001/offers?format=json";
        return this.http.get(api_url);
    }
}