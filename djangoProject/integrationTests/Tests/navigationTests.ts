import { Selector, t } from 'testcafe';
import { HomePage } from '../pages/homePage';
import { NavBar } from '../pages/componenets/navBar';
import { UserListPage } from '../pages/UserListPage';
import { ServerListPage } from '../pages/ServerListPage';
import User from '../pages/componenets/User';
import { UserDetailsPage } from '../pages/userPage';
import Server from '../pages/componenets/server';

const homePage = new HomePage();
const navBar = new NavBar()
const userPage = new UserListPage();
const userDetailsPage = new UserDetailsPage();
const serverPage = new ServerListPage();

fixture(`From Home page navigation tests`).beforeEach(
    async ()=>{
       
    }
).page("http://localhost:8000/")

// Tests
test('Home Page Loads', async t => {
    await homePage.isOnPage();
});

test('Servers List Navigation Test', async t => {
    await navBar.navigateServersList();
});

test('Login Navigation Test', async t => {
    await navBar.navigateToLogin();
});

test('Users List Navigation Test', async t => {
    await navBar.navigateUsersList();
});

test('Can View First User', async t => {
    await navBar.navigateUsersList();
    let users:User[] = await userPage.getDisplayedObjs() as User[];
    await userPage.expectAndClick(users[0].viewUserBtn);
    await userDetailsPage.componentShown();
});

test('Can View Last User', async t => {
    await navBar.navigateUsersList();
    let users:User[] = await userPage.getDisplayedObjs() as User[];
    await userPage.expectAndClick(users[users.length-1].viewUserBtn);
    await userDetailsPage.componentShown();
});


test('Can View First Server', async t => {
    await navBar.navigateUsersList();
    let servers:Server[] = await serverPage.getDisplayedServers() as Server[];
    await userPage.expectAndClick(servers[0].genericSecondaryBtn);
    await userDetailsPage.componentShown();
});

test('Can View Last Server', async t => {
    await navBar.navigateUsersList();
    let servers:Server[] = await serverPage.getDisplayedServers() as Server[];
    await userPage.expectAndClick(servers[servers.length-1].genericSecondaryBtn);
    await userDetailsPage.componentShown();
});


// test('Profile Navigation Test', async t => {
//     await navBar.navigateProfile();
// }) //this will fail without logging in first