import {createRoot} from 'react-dom/client'
import {BrowserRouter, Route, Routes} from "react-router-dom";
import {MainPage} from "./pages/MainPage.jsx";
import {AboutPage} from "./pages/AboutPage.jsx";
import {ScreenshotsPage} from "./pages/ScreenshotsPage.jsx";
import {VideosPage} from "./pages/VideosPage.jsx";
import {EntitiesPage} from "./pages/EntitiesPage.jsx";
import {Register} from "./pages/Register.jsx";
import {Header} from "./components/Header/index.jsx";
import {Profile} from "./pages/ProfilePage.jsx";
import {Login} from "./pages/Login.jsx";
import './index.css'
import {Provider} from "react-redux";
import store from "./store/store.js";
import {MapsPage} from "./pages/MapsPage.jsx";
import {AdminPage} from "./pages/AdminPage.jsx";
import {ImageDetail} from "./components/AdminPanel/Images/Image.jsx";

createRoot(document.getElementById('root')).render(
    <Provider store={store}>
        <BrowserRouter>
            <Header/>
            <Routes>
                <Route path="/*" element={<MainPage/>}/>
                <Route path="/About" element={<AboutPage/>}/>
                <Route path="/Screenshots" element={<ScreenshotsPage/>}/>
                <Route path="/Videos" element={<VideosPage/>}/>
                <Route path="/Entities" element={<EntitiesPage/>}/>


                <Route path="/Admin/" element={<AdminPage page=''/>}/>

                <Route path="/Admin/images" element={<AdminPage page='images'/>}/>
                <Route path="/Admin/videos" element={<AdminPage page='videos'/>}/>
                <Route path="/Admin/maps" element={<AdminPage page='maps'/>}/>
                <Route path="/Admin/skills" element={<AdminPage page='skills'/>}/>
                <Route path="/Admin/characters-or-builds" element={<AdminPage page='characters-or-builds'/>}/>
                <Route path="/Admin/audio" element={<AdminPage page='audio'/>}/>
                <Route path="/Admin/upgrades" element={<AdminPage page='upgrades'/>}/>
                <Route path="/Admin/items" element={<AdminPage page='items'/>}/>

                <Route path="/Admin/images/:id" element={<ImageDetail/>}/>
                <Route path="/Admin/videos/:id" element={<AdminPage/>}/>
                <Route path="/Admin/maps/:id" element={<AdminPage/>}/>
                <Route path="/Admin/skills/:id" element={<AdminPage/>}/>
                <Route path="/Admin/characters-or-builds/:id" element={<AdminPage/>}/>
                <Route path="/Admin/audio/:id" element={<AdminPage/>}/>
                <Route path="/Admin/upgrades/:id" element={<AdminPage/>}/>
                <Route path="/Admin/items/:id" element={<AdminPage/>}/>


                <Route path="/Login" element={<Login/>}/>
                <Route path="/Register" element={<Register/>}/>
                <Route path="/Profile" element={<Profile/>}/>
                <Route path="/Maps" element={<MapsPage/>}/>
            </Routes>
        </BrowserRouter>
    </Provider>
);
