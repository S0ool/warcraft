import React, {useEffect, useRef, useState} from 'react';
import '../../public/User/profile.css';
import avatarPlaceholder from '../../public/user/avatar.jpg';
import {changeAvatar, getUserProfile} from "../axios/User.jsx";
import {useNavigate} from "react-router-dom";
import {useSelector} from "react-redux";

export const Profile = () => {
    const [profileImage, setProfileImage] = useState();
    const [user, setUser] = useState();
    const [avatar, setAvatar] = useState(avatarPlaceholder);

    const allObj = useRef(null);
    const modal = useRef(null);
    const profileAvatar = useRef(null);
    const profileImageRef = useRef(null);

    useEffect(() => {
        const fetchData = async () => {
            const data = await getUserProfile();
            data.avatar = undefined;
            console.log(data);
            if (data) {
                if (data.avatar) {
                    const imageUrl = `http://localhost:8000${data.avatar}`;
                    setProfileImage(imageUrl);
                }
                setUser(data.user);
            } else {
                console.error("Failed to fetch user profile");
            }
        };
        fetchData();
    }, []);

    useEffect(() => {
        setAvatar(profileImage || avatarPlaceholder);
    }, [profileImage]);

    const handleAvatarChange = (event) => {
        if (event.target.files && event.target.files[0]) {
            const newAvatar = URL.createObjectURL(event.target.files[0]);
            setAvatar(newAvatar);
        }
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        modal.current.style.display = 'none';
        allObj.current.style.display = 'block';
    };

    const addHoverEffect = (element) => {
        element.current.style.transform = 'scale(1.2)';
        element.current.style.border = '1px solid #0097ff';
        element.current.style.boxShadow = '0 0 10px #0097ff';
    };

    const removeHoverEffect = (element) => {
        element.current.style.transform = 'scale(1)';
        element.current.style.border = 'none';
        element.current.style.boxShadow = 'none';
    };

    const profileEnter = () => {
        profileAvatar.current.style.zIndex = 10;
        addHoverEffect(profileImage);
        addHoverEffect(profileAvatar);
    };

    const profileLeave = () => {
        profileAvatar.current.style.zIndex = 0;
        removeHoverEffect(profileImage);
        removeHoverEffect(profileAvatar);
    };

    const profileClick = () => {
        modal.current.style.display = 'block';
        allObj.current.style.display = 'none';
    };
    const hideModal = () => {
        modal.current.style.display = 'none';
        allObj.current.style.display = 'block';
    };
    const navigate = useNavigate();
    const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);

    useEffect(() => {
        if (!isAuthenticated) {
            navigate('/main');
        }
        console.log(isAuthenticated)
    }, [isAuthenticated, navigate]);
    const changeAvatarFun = async (event) => {
        event.preventDefault();
        await changeAvatar(event);
        handleSubmit(event)
    };
    return (
        <>
            <div className="modal" ref={modal}>
                <div className="modalContent" onClick={hideModal}></div>
                <div id="modal_avatar"></div>
                <form onSubmit={(event) => changeAvatarFun(event)} encType="multipart/form-data" action=""
                      className='model_form'>
                    <input
                        type="file"
                        name="avatar"
                        id="image_input"
                        accept="image/*"
                        onChange={handleAvatarChange}
                    />
                    <button type="submit">Изменить аватар</button>
                </form>

            </div>

            <div className="all_obj" ref={allObj}>
                <div className="all_profile" onMouseEnter={profileEnter}
                     onMouseLeave={profileLeave}
                     onClick={profileClick}>
                    <div
                        className="profile_avatar"
                        ref={profileAvatar}

                    >
                        Выбрать новую аватарку
                    </div>
                    <img
                        src={avatar}
                        alt="Profile Avatar"
                        className="profile_image"
                        ref={profileImageRef}
                    />
                </div>
                <div className='profile_data'>
                    <div className="greeting_text reg_txt" id="profile" style={{margin: '2% 20%'}}>Profile</div>
                    <div className="greeting_text nick">Ник: {user?.username || 'Никнейм не указан'}</div>
                </div>
            </div>
        </>
    );
};
