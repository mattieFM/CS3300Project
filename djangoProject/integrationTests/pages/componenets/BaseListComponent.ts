import { Selector } from "testcafe";
import BaseComponent from "./BaseComponent";

export default class BaseListComponent extends BaseComponent {
    mainId:Selector = Selector("#serverTitle")
    otherIds:Selector[];

    constructor(nth:number=-1){
        super();
        if(nth!=-1){
            this.mainId = this.mainId.nth(nth);
        }
        if(this.otherIds)
        this.otherIds.forEach(element=>{
            element = element.nth(nth);
        })
    }
}