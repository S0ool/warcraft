import {Link} from "react-router-dom";
import style from './styles.module.css'

export const AdminHeader = () => {
    return (
        <header className={style.adminHeader + ' ' + 'header'}>
            <div className='header-content'>
                <ul className='nav-bar'>
                    <li>
                        <Link to='/Admin/images'>Панель изображений</Link>
                    </li>
                    <li>
                        <Link to='/Admin/videos'>Панель видео</Link>
                    </li>
                    <li>
                        <Link to='/Admin/maps'>Панель карт</Link>
                    </li>
                    <li>
                        <Link to='/Admin/skills'>Панель навыков</Link>
                    </li>
                    <li>
                        <Link to='/Admin/characters-or-builds'>Панель персонажей и зданий</Link>
                    </li>
                    <li>
                        <Link to='/Admin/heroes'>Панель героев</Link>
                    </li>
                    <li>
                        <Link to='/Admin/audio'>Панель аудио</Link>
                    </li>
                    <li>
                        <Link to='/Admin/upgrades'>Панель улучшений</Link>
                    </li>
                    <li>
                        <Link to='/Admin/items'>Панель предметов</Link>
                    </li>

                </ul>
            </div>
        </header>
    )
}