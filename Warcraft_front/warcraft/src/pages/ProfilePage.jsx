import React, { useEffect, useRef, useState } from 'react';
import  '../../public/User/profile.css';
import avatarPlaceholder from '../../public/user/avatar.jpg';
import {changeAvatar, getUserProfile} from "../axios/User.jsx";
import {useNavigate} from "react-router-dom";
import {useSelector} from "react-redux";

export const Profile = () => {
    const [profileImage, setProfileImage] = useState();
    const [user, setUser] = useState();
    const [avatar, setAvatar] = useState(avatarPlaceholder);

    const all_obj = useRef(null);
    const modal = useRef(null);
    const profile_avatar = useRef(null);
    const profile_image = useRef(null);

    useEffect(() => {
        const fetchData = async () => {
            const data = await getUserProfile();
            console.log(data)
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
        all_obj.current.style.display = 'block';
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
        profile_avatar.current.style.zIndex = 10;
        addHoverEffect(profile_image);
        addHoverEffect(profile_avatar);
    };

    const profileLeave = () => {
        profile_avatar.current.style.zIndex = 0;
        removeHoverEffect(profile_image);
        removeHoverEffect(profile_avatar);
    };

    const profileClick = () => {
        modal.current.style.display = 'block';
        all_obj.current.style.display = 'none';
    };
    const hideModal = () => {
        modal.current.style.display = 'none';
        all_obj.current.style.display = 'block';
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
        changeAvatar(event)
        handleSubmit(event)
    }
    return (
        <>
            <div className="modal" ref={modal}>
                <div className="modalContent" onClick={hideModal}>
                </div>
                    <div id="modal_avatar"></div>
                    <form onSubmit={(event) => changeAvatarFun(event)} encType="multipart/form-data" action="" className='model_form'>
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

            <div className="all_obj" ref={all_obj}>
                <div className="all_profile" onMouseEnter={profileEnter}
                     onMouseLeave={profileLeave}
                     onClick={profileClick}>
                    <div
                        className="profile_avatar"
                        ref={profile_avatar}

                    >
                        Выбрать новую аватарку
                    </div>
                    <img
                        src={avatar}
                        alt="Profile Avatar"
                        className="profile_image"
                        ref={profile_image}
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
