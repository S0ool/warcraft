import { createRoot } from 'react-dom/client'
import {BrowserRouter, Route, Routes} from "react-router-dom";
import {MainPage} from "./pages/MainPage.jsx";
import {AboutPage} from "./pages/AboutPage.jsx";
import {ScreenshotsPage} from "./pages/ScreenshotsPage.jsx";
import {VideosPage} from "./pages/VideosPage.jsx";
import {EntitiesPage} from "./pages/EntitiesPage.jsx";
import {AdminPage} from "./pages/AdminPage.jsx";
import {Register} from "./pages/Register.jsx";
import {Header} from "./components/Header/index.jsx";
import {Profile} from "./pages/ProfilePage.jsx";
import {Login} from "./pages/Login.jsx";
import './index.css'
import {Provider} from "react-redux";
import store from "./store/store.js";
import {MapsPage} from "./pages/MapsPage.jsx";
createRoot(document.getElementById('root')).render(
    <Provider store={store}>
      <BrowserRouter>
          <Header />
          <Routes>
              <Route path="/*" element={<MainPage/>} />
              <Route path="/About" element={<AboutPage/>} />
              <Route path="/Screenshots" element={<ScreenshotsPage/>} />
              <Route path="/Videos" element={<VideosPage/>} />
              <Route path="/Entities" element={<EntitiesPage/>} />
              <Route path="/Admin" element={<AdminPage/>} />
              <Route path="/Login" element={<Login/>} />
              <Route path="/Register" element={<Register/>} />
              <Route path="/Profile" element={<Profile/>} />
              <Route path="/Maps" element={<MapsPage/>} />
          </Routes>
      </BrowserRouter>
    </Provider>
        )
