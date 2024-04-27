import { Selector } from 'testcafe';
import { ServerListPage } from './ServerListPage';

export class HomePage extends ServerListPage {
    /** the div container of the home page */
    homeContainer: Selector = Selector("#serverContainer");

    /** @description override this with any selector that is representative of the component loading */
    examplePageBlerb: Selector = this.homeContainer;
}