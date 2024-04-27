import { Selector } from "testcafe";
import BaseListComponent from "./BaseListComponent";



export default class Server extends BaseListComponent {
    serverTitle: Selector = Selector("#serverTitle")
    /** connection key of the server */
    serverKey: Selector = Selector("#serverKey")
    mainId: Selector = this.serverTitle;
    serverDesc: Selector = Selector("#serverDesc")
    serverStartDate: Selector = Selector("#serverStartDate")
    serverEndDate: Selector = Selector("#serverEndDate")

    constructor(nth:number=-1){
        super();
        if(nth!=-1){
            this.serverTitle = this.serverTitle.nth(nth);
            this.serverKey = this.serverKey.nth(nth);
            this.serverDesc = this.serverDesc.nth(nth);
            this.serverStartDate = this.serverStartDate.nth(nth);
            this.serverEndDate = this.serverEndDate.nth(nth);
        }
    }
}