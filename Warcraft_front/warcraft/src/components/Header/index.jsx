import {Link} from "react-router-dom";
import {DownloadButton} from "../../UI/DownloadButton/index.jsx";
import '../../../public/main.css';
import {useDispatch, useSelector} from "react-redux";
import {logout} from "../../store/authSlice.js";

export const Header = () => {
    const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);
    const dispatch = useDispatch();

    const handleLogout = () => {
        dispatch(logout());
    };
    const title = `Скачать неофициальную\n версию Warcraft 3 на windows`;

    return (
        <header className='header'>
            <div className='header-content'>
                <ul className='nav-bar'>
                    <li>
                        <Link to='/Main'>Главная</Link>
                    </li>
                    <li>
                        <Link to='/About'>Об игре</Link>
                    </li>
                    <li>
                        <Link to='/Screenshots'>Изображения</Link>
                    </li>
                    <li>
                        <Link to='/Videos'>Видео</Link>
                    </li>
                    <li>
                        <Link to='/Entities'>Персонажи и здания</Link>
                    </li>
                    <li>
                        <Link to='/Maps'>Карты</Link>
                    </li>
                    <li>
                        <Link to='/Admin'>Админ панель</Link>
                    </li>
                    {isAuthenticated ? (
                        <>
                            <li>
                                <Link to='/Profile'>Профиль</Link>
                            </li>
                            <li>
                                <a onClick={() => handleLogout()}>Выход</a>
                            </li>
                        </>
                    ) : (
                        <>
                            <li>
                                <Link to='/Login'>Login</Link>
                            </li>
                            <li>
                                <Link to='/Register'>Register</Link>
                            </li>
                        </>
                    )}
                </ul>
            </div>

            <div className='download-btn-container'>
                <DownloadButton/>
                <DownloadButton title={title}
                                url='https://wc3.info/files/file/1-warcraft-3-the-frozen-throne/?&do=download&r=1
                                &confirm=1&t=1&csrfKey=8d5a0ab37cf3cdaf5590d483055ab97e'/>
            </div>
        </header>
    );
};
