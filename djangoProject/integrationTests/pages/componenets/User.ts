import { Selector } from "testcafe";
import BaseListComponent from "./BaseListComponent";

export default class User extends BaseListComponent {
    kickPlayerBtn: Selector = Selector("#kickPlayerBtn");
    viewUserBtn: Selector = Selector("#viewUserBtn");
    userBio: Selector = Selector("#userBio")
    userName: Selector = Selector("#userName")
    mainId: Selector = this.userName;
    otherIds: Selector[] = [this.kickPlayerBtn, this.viewUserBtn, this.userBio, this.userName];
}