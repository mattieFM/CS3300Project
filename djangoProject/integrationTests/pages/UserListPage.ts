import { Selector } from 'testcafe';
import User from './componenets/User';
import { GenericSearchPage } from './genericSearchPage';

export class UserListPage extends GenericSearchPage {
    /** the div container of the serverlist page */
    userListContainer: Selector = Selector("#userListContainer");

    /** @description override this with any selector that is representative of the component loading */
    examplePageBlerb: Selector = this.userListContainer;

    /** the search bar */
    searchBar: Selector = Selector("#userSearchBox")

    /** the submit btn */
    specificPrimaryBtn: Selector = Selector("#userSearchBtn")

    model=User;
}