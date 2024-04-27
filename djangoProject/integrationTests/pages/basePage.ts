import { Selector, t } from "testcafe";
import BaseComponent from "./componenets/BaseComponent";


export default class BasePage extends BaseComponent {
    /** @description override this with any selector that is representative of the page loading */
    examplePageBlerb: Selector = Selector('#nothing');

    /**
     * @description check that the component exists and is visible
     */
    async pageLoaded(){
        await t.expect(this.examplePageBlerb.visible).eql(true);
    }

    /** alias of pageLoaded */
    async isOnPage(){
        await this.pageLoaded()
    }

    

}