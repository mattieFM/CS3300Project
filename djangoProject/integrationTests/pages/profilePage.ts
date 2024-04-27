import { Selector } from 'testcafe';
import { NavBar } from './componenets/navBar';
import { UserDetailsPage } from './userPage';
import BasePage from './basePage';

export class ProfilePage extends UserDetailsPage implements BasePage {
    navBar: NavBar;
    examplePageBlerb: Selector;

    constructor(){
        super();
        BasePage.call(this);
    }

    /** the div container of the home page */
    profileContainer: Selector = Selector("#userProfileContainer");

    /** @description override this with any selector that is representative of the component loading */
    exampleComponentBlerb: Selector = this.profileContainer;

    async pageLoaded() {
        await BasePage.prototype.pageLoaded.call(this)
    }
    async isOnPage() {
        await BasePage.prototype.isOnPage.call(this)
    }
}