import { Link, useParams } from "react-router-dom";
import styles from "./styles.module.css";
import { getImageAxios } from "../../../axios/AdminAxios/Images.jsx";
import { AdminHeader } from "../AdminHeader/index.jsx";
import {useEffect, useRef, useState} from "react";
import {CreateUpdateImage} from "./CreateUpdateImage.jsx";

export const ImageDetail = ({is_admin=true}) => {
    const { id } = useParams();
    const [image, setImage] = useState(null);
    const imgDescRef = useRef(null);
    const [lastScrollY, setLastScrollY] = useState(window.scrollY);
    const [isModalOpen, setIsModalOpen] = useState(false);

    useEffect(() => {
        const fetchImage = async () => {
            try {
                const data = await getImageAxios(id);
                setImage(data);
            } catch (error) {
                console.error("Error fetching image:", error);
            }
        };
        fetchImage();
    }, [id]);


  useEffect(() => {
    setTimeout(() => {
        const container = imgDescRef.current;

        if (!container) {
            console.log("Container ref not available after delay");
            return;
        }

        const handleScroll = () => {
            const currentScrollY = container.scrollTop;

            if (currentScrollY > lastScrollY) {
                container.classList.remove("scrollUp");
                container.classList.add("scrollDown");

            } else if (currentScrollY < lastScrollY) {
                container.classList.remove("scrollDown");
                container.classList.add("scrollUp");

            }

            setLastScrollY(currentScrollY);
        };

        container.addEventListener("scroll", handleScroll);

        return () => {
            container.removeEventListener("scroll", handleScroll);
            container.classList.remove("scrollDown", "scrollUp");
        };
    }, 100);
}, [lastScrollY, imgDescRef.current]);
    const openModal = () => {
        setIsModalOpen(!isModalOpen);
    };
    return (
        <>
            <AdminHeader />
            {is_admin && (
                <button className={styles.update} onClick={openModal}>
                    {isModalOpen ? "Закрыть" : "Редактировать изображение"}
                </button>
            )}
            <div className={styles.imageContent}>
                {
                    isModalOpen ?(<CreateUpdateImage action='update' openModal={openModal} imageData={image} />):(<>
                <h2 className={styles.img_id}>Image ID: {id}</h2>
                <h3 className={styles.img_name}>
                    {image?.name || "Нет имени"}
                </h3>
                {image?.image ? (
                    <div className={styles.image_container}>
                        <div className={styles.image_overlay}></div>
                        <img
                            className={styles.img_img}
                            src={image.image}
                            alt={image.name}/>

                    </div>

                ) : (
                    <p>Изображение не найдено</p>
                )}
                <p className={styles.img_desc} ref={imgDescRef}>
                    {image?.description || "Нет описания"}
                </p>
            </>)}
            </div>
        </>
    );
};

