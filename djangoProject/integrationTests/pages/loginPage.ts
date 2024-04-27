import { Selector } from 'testcafe';
import BasePage from './basePage';

export class LoginPage extends BasePage {
    /** the div container of the home page */
    loginContainer: Selector = Selector("#loginPageContainer");

    /** @description override this with any selector that is representative of the component loading */
    examplePageBlerb: Selector = this.loginContainer;
}