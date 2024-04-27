import { Selector } from 'testcafe';
import BasePage from './basePage';
import Server from './componenets/server';

export class ServerListPage extends BasePage {
    /** the div container of the serverlist page */
    serverListContainer: Selector = Selector("#serverContainer");

    /** @description override this with any selector that is representative of the component loading */
    examplePageBlerb: Selector = this.serverListContainer;

    /** the search bar */
    searchBar: Selector = Selector("#serversSearch")

    /** the submit btn */
    specificPrimaryBtn: Selector = Selector("#serverSearchBtn")

    async search(query){
        await this.expectAndClickAndType(this.searchBar, query);
        await this.expectAndClick(this.specificPrimaryBtn);
    }

    /**
     * @description return an array of the displayed servers
     */
    async getDisplayedServers(){
        let server = new Server();
        let servers:Server[] = [];
        let numberOfShownServers = await server.serverDesc.count;
        for (let index = 0; index < numberOfShownServers; index++) {
            let server = new Server(index);
            servers.push(server);
        }
        return servers;
    }
}