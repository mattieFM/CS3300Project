import { ClientFunction, Selector, t } from "testcafe";

/**
 * @description a base component class that all components and pages MUST extend
 */
export default class BaseComponent {

    /** @description override this with any selector that is representative of the page loading */
    exampleComponentBlerb: Selector = Selector('#nothing');

    /** bootstrap primary button selector */
    genericPrimaryBtn: Selector = Selector("btn btnPrimary").nth(0);

    genericSecondaryBtn: Selector = Selector("btn btn-secondary").nth(0);

    /** if defined generic submit will use this button specifically instead of finding one */
    specificPrimaryBtn?: Selector = undefined;

    /**
     * @description check that the component exists and is visible
     */
    async componentShown(){
        await this.componentExists();
        await t .expect(this.exampleComponentBlerb.visible).eql(true);
    }

    /**
     * @description check that the component exists
     */
    async componentExists(){
        await t .expect(this.exampleComponentBlerb.exists).eql(true);
    }

    /**
     * @description press the first btn btn-primary key on the page if one exists
     */
    async genericSubmit(){
        if(typeof this.specificPrimaryBtn != 'undefined')
            await this.expectAndClick(this.specificPrimaryBtn);
        else
            await this.expectAndClick(this.genericPrimaryBtn);
    }

    /**
     * @description expect that an element exists then click it
     * @param {Selector} element 
     */
    async expectAndClick(element:Selector){
        await t
            .expect(element.exists).ok()
            .click(element);
    }

    /**
     * @description expect that an element exists then click it then type text into it
     * @param {Selector} element 
     */
    async expectAndClickAndType(element:Selector, text:string){
        await t
            .expect(element.exists).ok()
            .click(element)
            .typeText(element, text);
    }
}