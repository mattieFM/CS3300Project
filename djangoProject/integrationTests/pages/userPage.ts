import { Selector } from 'testcafe';
import User from './componenets/User';

export class UserDetailsPage extends User {
    /** the div container of the serverlist page */
    userDetailsPageContainer: Selector = Selector("#userDetailsPage");

    /** @description override this with any selector that is representative of the component loading */
    examplePageBlerb: Selector = this.userDetailsPageContainer;
}