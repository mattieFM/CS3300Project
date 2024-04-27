import { Selector } from 'testcafe';
import BasePage from './basePage';
import BaseListComponent from './componenets/BaseListComponent';

export class GenericSearchPage extends BasePage {
    /** the div container of the serverlist page */
    serverListContainer: Selector = Selector("#serverContainer");

    /** @description override this with any selector that is representative of the component loading */
    examplePageBlerb: Selector = this.serverListContainer;

    /** the search bar */
    searchBar: Selector = Selector("#serversSearch")

    /** the submit btn */
    specificPrimaryBtn: Selector = Selector("#serverSearchBtn")

    /** @description overriden by parent for what component this list is of */
    model:any = BaseListComponent;

    async search(query){
        await this.expectAndClickAndType(this.searchBar, query);
        await this.expectAndClick(this.specificPrimaryBtn);
    }

    /**
     * @description return an array of the displayed servers
     */
    async getDisplayedObjs(){
        let server = new this.model();
        let servers:BaseListComponent[] = [];
        let numberOfShownServers = await server.mainId.count;
        for (let index = 0; index < numberOfShownServers; index++) {
            let server = new this.model(index);
            servers.push(server);
        }
        return servers;
    }
}