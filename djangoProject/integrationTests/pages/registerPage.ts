import { Selector } from 'testcafe';
import BasePage from './basePage';

export class RegisterPage extends BasePage {
    /** the div container of the home page */
    registerContainer: Selector = Selector("#registerContainer");

    /** @description override this with any selector that is representative of the component loading */
    examplePageBlerb: Selector = this.registerContainer;
}