import { Selector, t } from 'testcafe';
import { HomePage } from '../pages/homePage';
import { NavBar } from '../pages/componenets/navBar';
import { UserListPage } from '../pages/UserListPage';
import { ServerListPage } from '../pages/ServerListPage';

const homePage = new HomePage();
const navBar = new NavBar()
const serverPage = new ServerListPage();
const userPage = new UserListPage();

fixture(`Search Tests`).beforeEach(
    async ()=>{
       
    }
).page("http://localhost:8000/")

// Tests

let searchableObjs = [
    {page:serverPage,name:"server",navFunc:()=>navBar.navigateServersList(),getObjListFunc:()=>serverPage.getDisplayedServers()},
    {page:userPage,name:"user",navFunc:()=>navBar.navigateUsersList(),getObjListFunc:()=>userPage.getDisplayedObjs()},
]

//search tests
searchableObjs.forEach(obj=>{
    const objName = obj.name;
    const pageObj = obj.page
    const navFunc = obj.navFunc;
    const getObjListFunc = obj.getObjListFunc;
    test(`can see some ${objName}`, async t => {
        await navFunc();
        let servers = await getObjListFunc();
        await t.expect(servers.length > 1).ok();
    });
    
    test(`Can filter ${objName} with search term`, async t => {
        await navFunc();
        let serversBeforeSearch = await getObjListFunc();
        await t.expect(serversBeforeSearch.length > 1).ok();
        await pageObj.search("something");
        let serversAfterSearch = await getObjListFunc();
        await t.expect(serversBeforeSearch.length > serversAfterSearch.length).ok();
    });
    
    test(`can find ${objName} by name`, async t => {
        await navFunc();
        let serversBeforeSearch = await getObjListFunc();
        await t.expect(serversBeforeSearch.length > 1).ok();
        await pageObj.search(await serversBeforeSearch[0].mainId.innerText);
        let serversAfterSearch = await getObjListFunc();
        await t.expect(serversBeforeSearch.length > serversAfterSearch.length).ok();
        await t.expect(serversAfterSearch.length == 1).ok();
        await t.expect(await serversAfterSearch[0].mainId.innerText == await serversBeforeSearch[0].mainId.innerText).ok();
    });
    
    
})

