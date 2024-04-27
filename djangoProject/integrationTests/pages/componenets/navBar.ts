import { ServerListPage } from "../ServerListPage";
import { UserListPage } from "../UserListPage";
import { HomePage } from "../homePage";
import { LoginPage } from "../loginPage";
import { ProfilePage } from "../profilePage";
import { Selector, t } from 'testcafe';
import BaseComponent from "./BaseComponent";

export class NavBar extends BaseComponent {
    /** the logo btn */
    navLogo: Selector = Selector("#navLogo")
    /** the server list btn */
    navServers: Selector = Selector("#navServers")
    /** the users list btn */
    navUsers: Selector = Selector("#navUsers")
    /** the profile btn */
    navProfile: Selector = Selector("#navProfile")
    /** the register btn */
    navRegister: Selector = Selector("#navRegister")
    /** the logout btn */
    navLogout: Selector = Selector("#navLogout")
    /** the login btn */
    navLogin: Selector = Selector("#navLogin")

    /** @description override this with any selector that is representative of the component loading */
    exampleComponentBlerb: Selector = this.navLogo;


    /** @description navigate to the home page */
    async navigateHome(){
        this.expectAndClick(this.navLogo);
        let homePage = new HomePage();
        await homePage.pageLoaded();
        return homePage;
    }

    /** @description navigate to the servers list page */
    async navigateServersList(){
        await this.expectAndClick(this.navServers);
        let serverPage = new ServerListPage();
        await serverPage.pageLoaded();
        return serverPage;
    }

    /** @description navigate to the users list page */
    async navigateUsersList(){
        this.expectAndClick(this.navUsers);
        let page = new UserListPage();
        await page.pageLoaded();
        return page;
    }

    /** @description navigate to the profile page */
    async navigateProfile(){
        this.expectAndClick(this.navProfile);
        let page = new ProfilePage();
        await page.pageLoaded();
        return page;
    }

    /** @description click the logout btn */
    async clickLogout(){
        this.expectAndClick(this.navLogout);
        await t.expect(this.navLogin.exists).ok()
    }

    /** @description click the logout btn */
    async navigateToLogin(){
        this.expectAndClick(this.navLogin);
        let page = new LoginPage();
        await page.pageLoaded();
        return page;
    }
    
}